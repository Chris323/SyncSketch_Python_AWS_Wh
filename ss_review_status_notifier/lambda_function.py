import json
import urllib3
import os
import logging

def lambda_handler(event, context):
    #whurl = os.getenv('SLACK_WEBHOOK') 
    #or
    #os.environ['SLACK_WEBHOOK']
    message = ""
    whurl = match_webhook(event["project"]["name"])
    logging_handler(event)
    if event["new_status"] == "":
        message = {"text": f"The approval status of \"{event['item_name'].upper()}\" in \"{event['review']['name'].upper()}\" has changed to \"NO STATUS\""}
    else:
        message = {"text": f"The approval status of \"{event['item_name'].upper()}\" in \"{event['review']['name'].upper()}\" has changed to \"{event['new_status'].capitalize()}\""}
    #message = {"text": f"{event}"} #uncomment to output entire event to slack
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

#TODO
def match_webhook(input):
    match input:
        case "project1":
            return "SLACK_WEBHOOK1"
        case "project2":
            return "SLACK_WEBHOOK2"
        case "project3":
            return "SLACK_WEBHOOK3"
        case "project4":
            return "SLACK_WEBHOOK4"
        case "project1":
            return "SLACK_WEBHOOK5"
        case "project2":
            return "SLACK_WEBHOOK6"
        case "project1":
            return "SLACK_WEBHOOK7"
        case default:
            return os.getenv('SLACK_WEBHOOK')

def logging_handler(event):
    logger = logging.getLogger()
    logger.setLevel("INFO")
    logger.info(event)     
           