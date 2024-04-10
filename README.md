AVG response
index = paypal_ist_switch_prod (host=vlppauepwso201 OR host=vlppauepwso202 OR host=vlppauspwso201 OR host=vlppauspwso202 sourcetype=prod_paypal_ist_switch_carbon_log source="/data/wso2/wso2am-3.2.0/repository/logs/wso2carbon.log" ("OUT_MESSAGE" AND "responseMessage") OR ("IN_MESSAGE" AND "transaction")) OR (host=vlppauepistsap01 OR host=vlppauepistsap02 OR host=vlppauspistsap01 OR host=vlppauspistsap02 sourcetype=prod_paypal_ist_switch_eftpos_log source="/home/istadm/pdir/log/debug/eftpos.debug" ("bytes to EFTPOS*" ("/m0200/" OR "/m0100/" OR "/m0400/")) OR ("L-EFTPOS-1212:" AND ("m0210" OR "m0110" OR "m0410")) )
| rex "UUID.*(?<Transaction_ID>[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}+)"
| eval date1=strptime(date,"%Y-%m-%dT%H:%M:%S.%3Q"),time1=strptime(time,"%y.%m.%d %H:%M:%S.%9Q")
| stats min(date1) as start max(date1) as end min(time1) as start_pos max(time1) as end_pos values(date_mday) as date_mday by Transaction_ID
| eval diff_carbon=end - start, diff_pos=end_pos - start_pos, time_taken = diff_carbon - diff_pos
| stats avg(time_taken) as time_taken by date_mday
| fields time_taken date_mday

Success count

index = paypal_ist_switch_prod host=vlppauepwso201 OR host=vlppauepwso202 OR host=vlppauspwso201 OR host=vlppauspwso202     sourcetype=prod_paypal_ist_switch_carbon_log source="/data/wso2/wso2am-3.2.0/repository/logs/wso2carbon.log"     "OUT_MESSAGE" AND "responseMessage" AND "hostResponseCode" |rex "hostResponseCode\"\:\"(?<sucess_hostResponseCode>\d+)" | eval date=strftime(_time, "%Y-%m-%d") |stats count(sucess_hostResponseCode) as success_count by date

Failure


index = paypal_ist_switch_prod host=vlppauepwso201 OR host=vlppauepwso202 OR host=vlppauspwso201 OR host=vlppauspwso202
sourcetype=prod_paypal_ist_switch_carbon_log source="/data/wso2/wso2am-3.2.0/repository/logs/wso2carbon.log" ("{\"responseMessage\":\"message timeout\"}") OR (("statusCode\":\"2" OR "statusCode\":\"12\"") "OUT_MESSAGE" AND "responseMessage" AND (NOT hostResponseCode OR \"hostResponseCode\"\:\"E*) AND (NOT \"responseCode\"\:\"61\"))
| eval date=strftime(_time, "%Y-%m-%d")
| stats count as failure_count by date
