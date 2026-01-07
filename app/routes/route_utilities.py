from flask import abort, make_response
from ..db import db
import requests
import os

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        response = {"message": f"{cls.__name__} {model_id} invalid"}
        abort(make_response(response , 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)
    
    if not model:
        response = {"message": f"{cls.__name__} {model_id} not found"}
        abort(make_response(response, 404))
    
    return model

def send_slack_notification(message):
    """Send a notification message to Slack."""
    slack_token = os.environ.get("SLACK_API_TOKEN")
    channel = os.environ.get("SLACK_CHANNEL_ID", "#curious-george")
    
    if not slack_token:
        print("ERROR: SLACK_API_TOKEN is not set")
        return
    
    headers = {
        "Authorization": f"Bearer {slack_token}"
    }
    
    data = {
        "channel": channel,
        "text": message
    }
    
    try:
        response = requests.post("https://slack.com/api/chat.postMessage", headers=headers, json=data)
        response_data = response.json()
        
        if not response_data.get("ok"):
            print(f"ERROR: Slack API failed - {response_data.get('error', 'Unknown error')}")
            print(f"Response: {response_data}")
        else:
            print(f"SUCCESS: Slack message sent to {channel}")
    except Exception as e:
        print(f"ERROR: Failed to send Slack message - {str(e)}")