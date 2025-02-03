import json
import urllib3
import os

def lambda_handler(event, context):
    # FOUND IN .ENV
    whurl = match_webhook(event["name"])
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

def match_webhook(input):
    match input:
        case "project1":
            return "SlackWhurl1"
        case "project2":
            return "SlackWhurl2"
        case "project3":
            return "SlackWhurl3"
        case "project4":
            return "SlackWhurl4"
        case "project1":
            return "SlackWhurl5"
        case "project2":
            return "SlackWhurl6"
        case "project1":
            return "SlackWhurl7"
        case default:
            return "SlackWhurl"
