import requests
from requests.auth import HTTPBasicAuth

# Define your Splunk server URL and authentication details
splunk_server = 'https://your_splunk_server:8089'
username = 'your_username'
password = 'your_password'
# Alternatively, if you have a token:
# token = 'Splunk your_splunk_token'

# Define the new time zone
new_time_zone = 'UTC'

# Create the payload for the API request
payload = {
    'uiTimezone': new_time_zone
}

# Define the endpoint for updating user settings
endpoint = f'{splunk_server}/servicesNS/-/-/authentication/users/{username}'

# Make the request to change the time zone
# Using HTTPBasicAuth for username and password
response = requests.post(endpoint, data=payload, auth=HTTPBasicAuth(username, password))
# Alternatively, if you use a token for authentication:
# headers = {'Authorization': f'Bearer {token}'}
# response = requests.post(endpoint, data=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print(f"Time zone changed successfully to {new_time_zone}.")
else:
    print(f"Failed to change time zone. Status code: {response.status_code}, Response: {response.text}")
