import splunklib.client as client
import splunklib.results as results
import time
import json


def login():
    HOST = "rest-splunk.fnfis.com"
    PORT = 443
    USERNAME = 'e5687265'
    PASSWORD = 'Thorsaidhellov@1d'
    service = client.connect(
        host=HOST,
        port=PORT,
        username=USERNAME,
        password=PASSWORD,
        
    )
    session_token = service.token
    print(session_token)
    print("Connected to Splunk")
    return service

def exe(s_query,service):
    job = service.jobs.create(s_query,exec_mode="normal")

    while not job.is_done():
        time.sleep(2)

    results_list = []
    
    for result in results.ResultsReader(job.results()):
        results_list.append(result)
    return results_list

def get_timezone(service):
    tz_query = """
    search index = paypal_ist_switch_prod host=vlppauepwso201 earliest=-1m latest=now
    | eval CurrentTimeZone=strftime(_time,"%Z") 
    |stats count by CurrentTimeZone
    """
    result_list = exe(tz_query,service)
    
    current_timezone = result_list[0]["CurrentTimeZone"] 
    print("Your Time zone : ",current_timezone)  
    
def get_Query(service):
    Start_time = "06/13/2024:18:10:00"
    End_time = "06/13/2024:18:13:12"
    search_query = """
    search index = intuit_ist_switch host=vlinus*pwso20* sourcetype=prod_intuit_ist_switch_carbon_log source="/data/wso2/wso2am-3.2.0/repository/logs/wso2carbon*.log"
    earliest="""+Start_time+ """ latest="""+End_time+ """
    "OUT_MESSAGE" AND "responseMessage" AND "hostResponseCode" |rex "hostResponseCode\\"\:\\"(?<sucess_hostResponseCode>\d+)"
    | eval date=strftime(_time, "%Y-%m-%d") | dedup UUID |stats count(sucess_hostResponseCode) as success_count by date

    """
    result= exe(search_query, service)
    print("Query output:\n",result)
    # Results to a JSON file
    with open('results.json', 'w') as file:
        json.dump(result, file, indent=4)


service = login()
get_timezone(service)
get_Query(service)
