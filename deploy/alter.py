import requests

def create_alert_rule():
    # Set up authentication and headers
    auth = ("admin", "password")  # Replace with your Grafana username and password
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # Define the alert rule payload
    payload = {
        "name": "Model Accuracy Alert",
        "conditions": [
            {
                "evaluator": {
                    "type": "gt",
                    "params": [0.9]  # Set your desired threshold here
                },
                "reducer": {
                    "type": "avg",
                    "params": [],
                },
                "operator": {
                    "type": "and",
                },
                "query": {
                    "params": ["A", "5m", "now"],
                },
                "type": "query",
            },
        ],
        "notifications": [
            {
                "uid": "email-notification-uid",  # Replace with the UID of your notification channel
                "name": "Email",
                "type": "email",
            },
        ],
    }

    # Send a POST request to create the alert rule
    response = requests.post(
        "http://localhost:3000/api/alerts",
        auth=auth,
        headers=headers,
        json=payload,
    )

    if response.status_code == 200:
        print("Alert rule created successfully.")
    else:
        print("Error creating alert rule:", response.text)

# Call the function to create the alert rule
create_alert_rule()
