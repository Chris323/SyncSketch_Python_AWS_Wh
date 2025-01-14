import json
import urllib3

def lambda_handler(event, context):
    # TODO implement
    whurl = ""
    message = {"text": f"The approval status of {event['item_name']} in {event['review']['name']} has changed to \"{event['new_status']}\""}
    send_webhook(whurl, message)

    #AKA reverse api
def send_webhook(webhook_url, payload):
    text = "Hello Hammer Creative, from AWS Lambda"
    #payload = {"text": text}
    
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

