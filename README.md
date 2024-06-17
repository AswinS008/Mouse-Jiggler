import splunklib.client as client
import splunklib.results as results
import time
import json

def getQuery():
def assignVariable():
def Auth():
def postQuery():
def main():

Start_time = "06/13/2024:18:10:00"
End_time = "06/13/2024:18:13:12"

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

Start_time = "06/13/2024:18:10:00"
End_time = "06/13/2024:18:13:12"
tz="| eval _time = _time + (10*3600)" #Australia/Sydney

session_token = service.token

print(session_token)

print("Connected to Splunk")

# for app in service.apps:
#     print(app.name)

search_query = """
search index = paypal_ist_switch_prod host=vlppauepwso201 earliest=-5m latest=now 

| eval CurrentTimeZone=strftime(_time, "%y-%m-%d %H:%M:%S %Z") 
|stats count by CurrentTimeZone 

"""

job = service.jobs.create(search_query,exec_mode="normal")

while not job.is_done():
    time.sleep(2)

results_list = []
ctz=[]
for result in results.ResultsReader(job.results()):
    print(result)
    results_list.append(result)
	
# Write the list of results to a JSON file
with open('results.json', 'w') as file:
    json.dump(results_list, file, indent=4)







# |eval current_time=now(), current_time_gmt=striftime(now(,"%y-%m-%d %H:%M:%S %z"))
# | eval _time = striftime(strptime(_time, "%m/%d/%y:%H:%M:%S"),"%y-%m-%d %H:%M:%S")+'GMT'











