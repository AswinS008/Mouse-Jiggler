
import splunklib.client as client
import splunklib.results as results
import time
import json
import requests

Start_time = "06/13/2024:18:10:00"
End_time = "06/13/2024:18:13:12"

HOST = "fnfis.com"
PORT = 4843
USERNAME = 'e565'
PASSWORD = 'Thoov@1d'

service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD,
    
)
session_token = service.token

print(session_token)

print("Connected to Splunk")



search_query = """
search index = intuit_ist_switch host=vlinus*pwso20* sourcetype=prod_intuit_ist_switch_carbon_log  
"""

job = service.jobs.create(search_query)

while not job.is_done():
    time.sleep(2)

results_list = []
for result in results.ResultsReader(job.results()):
    print(result)
    results_list.append(result)
