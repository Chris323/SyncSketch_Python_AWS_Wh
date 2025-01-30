import json
import urllib3
import os

def lambda_handler(event, context):
    # FOUND IN .ENV
    whurl = "SLACK_WEBHOOK"
    message = {"text": f"The approval status of \"{event['item_name'].upper()}\" in \"{event['review']['name'].upper()}\" has changed to \"{event['new_status'].capitalize()}\""}
    send_webhook(whurl, message)

    #AKA reverse api
def send_webhook(webhook_url, payload):
    #text = "Hello Hammer Creative, from AWS Lambda"
    
    # Create an HTTP pool manager
    http = urllib3.PoolManager()
    try:
        # Send the POST request with JSON payload
        response = http.request(
            "POST",
            webhook_url,
            body=json.dumps(payload)
        )
        
        # Check for successful response
        if response.status != 200:
            print(f"Error: {response.status}")
        
        else:
            print("Webhook sent successfully")

    except Exception as e:
        # Log the error if the request fails
        return {"statusCode": 500, "body": f"Error: {str(e)}"}

