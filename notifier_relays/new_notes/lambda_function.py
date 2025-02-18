import json
import urllib3
import os
import logging

def lambda_handler(event, context):
    logging_handler(event)
    whurl = os.environ['SLACK_WEBHOOK_TESTING'] #for testing channel output
    #whurl = match_webhook(event["project"]["name"])
    #message = {"text": f"{event}"} #uncomment to output entire event to slack, may bog down speeds
    #message = {"text": f"New Notes: {event['item_info'][0]['comments'][0]['text']}"}
    message = {"text": "---------------------------------------------------\n"+
                "** NEW NOTES NOTIFICATION ** \n"+
                f"Project Name: \"{event['project']['name']}\" \n"+
                f"Item Name: \"{event['item_info'][0]['name'].upper()}\" \n"+
                f"Review Name: \"{event['review']['name'].upper()}\" \n"+
                f"New Notes By: \"{event['item_info'][0]['comments'][0]['creator']['full_name']}\""}
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

#Channel webhook selection
def match_webhook(input):
    if "mtg -" in input.lower():
        return os.getenv('SLACK_WEBHOOK_MTG')
    elif "lor-" in input.lower():
        return os.getenv('SLACK_WEBHOOK_LOR')
    elif "som-" in input.lower():
        return os.getenv('SLACK_WEBHOOK_SOM')
    elif "umbra" in input.lower():
        return os.getenv('SLACK_WEBHOOK_UMBRA')
    elif "forza" in input.lower() or "steel" in input.lower() or "motorsport" in input.lower():
        return os.getenv('SLACK_WEBHOOK_FORZA')
    elif "camn-" in input.lower():
        return os.getenv('SLACK_WEBHOOK_CAMN')
    elif "jaws" in input.lower():
        return os.getenv('SLACK_WEBHOOK_JAWS')
    elif "prm-" in input.lower():
        return os.getenv('SLACK_WEBHOOK_PRM')
    elif "kf3-" in input.lower():
        return os.getenv('SLACK_WEBHOOK_KF3')
    elif "fn" in input.lower() or "fort" in input.lower():
        return os.getenv('SLACK_WEBHOOK_FN')
    #elif "gfsh" in input.lower():
        #return os.getenv('SLACK_WEBHOOK_GFSH')
    else:
        return os.getenv("SLACK_WEBHOOK")

def logging_handler(event):
    logger = logging.getLogger()
    logger.setLevel("INFO")
    logger.info(event)     
           