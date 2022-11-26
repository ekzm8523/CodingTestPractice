import json

import requests
from slack_sdk import WebClient
import time
import os


def health_check():
    ai_server_path = os.getenv('AI_SERVER_PATH')
    slack = WebClient(os.getenv('AI_SERVER_SLACK_BOT_TOKEN'))
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        response = requests.get(f"{ai_server_path}:3000/healthz", timeout=1)
        if response.status_code != 200:
            slack.chat_postMessage(
                channel=os.getenv('AI_SERVER_CHANNEL'),
                text=f"{current_time} : AI server health check fail !!!!!!!!!! \nerror message : {response.text} \n"
                     f"status code : {response.status_code}",
            )
            slack.chat_postMessage(
                channel=os.getenv('NOTIFICATION_CHANNEL'),
                text=f"{current_time} : AI server 죽었어요!!!!!\n please check AI Server",
            )
    except requests.exceptions.ConnectTimeout:
        slack.chat_postMessage(
            channel=os.getenv('AI_SERVER_CHANNEL'),
            text=f"{current_time} : AI server health check fail !!!!!!!!!!\n please check AI Server",
        )
        slack.chat_postMessage(
            channel=os.getenv('NOTIFICATION_CHANNEL'),
            text=f"{current_time} : AI server 죽었어요!!!!!\n please check AI Server",
        )


def lambda_handler(event, context):
    health_check()

    return {"status": 200}

