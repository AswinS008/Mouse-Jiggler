import splunklib.client as client
import splunklib.results as results
import time
import json
import requests

  
# HOST = "splunk.fnfis.com"
HOST = "rest-splunk.fnfis.com"
PORT = 443
USERNAME = 'e5687265'
PASSWORD = 'Thorsaidhellov@1d'
# earliest_time = "-15m" 
# latest_time = "now"

service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD,
    
)
session_token = service.token

print(session_token)

print("Connected to Splunk")
user_pref_endpoint= f"servicesNS/"+USERNAME+"/user-prefs"
settings={"search-timezone": "Australia/Sydney"}
response = service.post(user_pref_endpoint, **settings)

if response.status_code == 200:
    print(f"Timezone updated successfully to GMT!")
else:
     print(f"Failed to update Timezone Status coed:{response.status_coed}")
     print("Response content",response.content)
# for app in service.apps:
#     print(app.name)

Start_time = "06/13/2024:18:10:00"
End_time = "06/13/2024:18:13:12"

search_query = """
search index = intuit_ist_switch host=vlinus*pwso20* sourcetype=prod_intuit_ist_switch_carbon_log  source="/data/wso2/wso2am-3.2.0/repository/logs/wso2carbon*.log" 
("{\\"responseMessage\\":\\"message timeout\\"}") OR(("statusCode\\":\\"2" OR "statusCode\\":\\"12\\"") AND 
"OUT_MESSAGE" AND "responseMessage" AND (NOT hostResponseCode OR \\"hostResponseCode\\"\\:\\"E*))
earliest="""+Start_time+ """ latest="""+End_time+ """
| rex "responseCode\\"\\:(?<rc>\d+)"
|rex "statusCode\\"\\:\\"(?<SC>\d+)" 
|dedup UUID 
| eval date=strftime(_time, "%Y-%m-%d") |search rc!=161 AND rc!=903 |stats count by rc
"""

# job = service.jobs.create(search_query, **search_kwargs)
job = service.jobs.create(search_query)
# job = service.jobs.create(search_query, earliest_time=earliest_time, latest_time=latest_time)
while not job.is_done():
    time.sleep(2)

results_list = []
for result in results.ResultsReader(job.results()):
    print(result)
    results_list.append(result)

# Write the list of results to a JSON file
with open('results.json', 'w') as file:
    json.dump(results_list, file, indent=4)

# for result in results.ResultsReader(job.results()):
#     print(result)
#     json_data = json.dumps(result, indent=4)
#     print(json_data)
#     with open("Result.json",'a' ) as file:
#         file.write(str(json_data)+'\n')
        
