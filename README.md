from flask import Flask, request, jsonify
import splunklib.client as client
import splunklib.results as results
import time
import json

app = Flask(__name__)

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

def exe(s_query, service):
    job = service.jobs.create(s_query, exec_mode="normal")

    while not job.is_done():
        time.sleep(2)

    results_list = []

    for result in results.ResultsReader(job.results()):
        results_list.append(result)
    return results_list

def get_Query(service):
    Start_time = "06/13/2024:18:10:00"
    End_time = "06/13/2024:18:13:12"
    search_query = """
    search index = intuit_ist_switch host=vlinus*pwso20* sourcetype=prod_intuit_ist_switch_carbon_log source="/data/wso2/wso2am-3.2.0/repository/logs/wso2carbon*.log"
    earliest=""" + Start_time + """ latest=""" + End_time + """
    "OUT_MESSAGE" AND "responseMessage" AND "hostResponseCode" |rex "hostResponseCode\\"\:\\"(?<sucess_hostResponseCode>\d+)"
    | eval date=strftime(_time, "%Y-%m-%d") | dedup UUID |stats count(sucess_hostResponseCode) as success_count by date

    """
    result = exe(search_query, service)
    print("Query output:\n", result)
    return json.dumps(result, indent=4)

service = login()

@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()
    result_id = data.get('result_id')
    
    # Assuming we want to use get_Query function for this example
    query_result = get_Query(service)
    
    return jsonify({'result': query_result})

if __name__ == '__main__':
    app.run(debug=True)
-----------------------------------------------------------------

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3 Tabs with Buttons and Result Fields</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .tab {
            display: none;
        }
        .tab-header {
            display: flex;
            cursor: pointer;
            padding: 10px;
            background-color: #f1f1f1;
        }
        .tab-header.active {
            background-color: #ccc;
        }
        .tab-content {
            padding: 20px;
            display: none;
        }
        .tab-content.active {
            display: block;
        }
        .button-container {
            margin: 10px 0;
        }
        .result {
            margin-top: 10px;
        }
    </style>
</head>
<body>

<div class="tab-header" data-tab="tab1">Tab 1</div>
<div class="tab-header" data-tab="tab2">Tab 2</div>
<div class="tab-header" data-tab="tab3">Tab 3</div>

<div id="tab1" class="tab-content">
    <div class="button-container">
        <button onclick="triggerExe('result1-1')">Button 1</button>
        <button onclick="triggerExe('result1-2')">Button 2</button>
        <button onclick="triggerExe('result1-3')">Button 3</button>
    </div>
    <div class="result" id="result1-1">Result 1-1</div>
    <div class="result" id="result1-2">Result 1-2</div>
    <div class="result" id="result1-3">Result 1-3</div>
</div>

<div id="tab2" class="tab-content">
    <div class="button-container">
        <button onclick="triggerExe('result2-1')">Button 1</button>
        <button onclick="triggerExe('result2-2')">Button 2</button>
        <button onclick="triggerExe('result2-3')">Button 3</button>
    </div>
    <div class="result" id="result2-1">Result 2-1</div>
    <div class="result" id="result2-2">Result 2-2</div>
    <div class="result" id="result2-3">Result 2-3</div>
</div>

<div id="tab3" class="tab-content">
    <div class="button-container">
        <button onclick="triggerExe('result3-1')">Button 1</button>
        <button onclick="triggerExe('result3-2')">Button 2</button>
        <button onclick="triggerExe('result3-3')">Button 3</button>
    </div>
    <div class="result" id="result3-1">Result 3-1</div>
    <div class="result" id="result3-2">Result 3-2</div>
    <div class="result" id="result3-3">Result 3-3</div>
</div>

<script>
    const headers = document.querySelectorAll('.tab-header');
    const contents = document.querySelectorAll('.tab-content');

    headers.forEach(header => {
        header.addEventListener('click', () => {
            headers.forEach(h => h.classList.remove('active'));
            contents.forEach(c => c.classList.remove('active'));
            
            header.classList.add('active');
            document.getElementById(header.getAttribute('data-tab')).classList.add('active');
        });
    });

    function triggerExe(resultId) {
        fetch('/execute', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ result_id: resultId })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById(resultId).innerText = data.result;
        })
        .catch(error => console.error('Error:', error));
    }

    // Set initial active tab
    headers[0].classList.add('active');
    contents[0].classList.add('active');
</script>

</body>
</html>
