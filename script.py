
import requests




# Base URL for the API
BASE_URL = "https://hackhour.hackclub.com"
api_key = "55ef9bc4-cb2d-484e-9062-ca055761e82b"
slack_id = "U07B1MK6MAQ"
def start_session(slack_id, work, api_key):
    url = f"{BASE_URL}/api/start/{slack_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "work": work
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()








def start():
    api_key = "55ef9bc4-cb2d-484e-9062-ca055761e82b"
    slack_id = "user_slack_id"
    use = "BS2"  
    start_session(slack_id, use, api_key)
    return "startet"


start()