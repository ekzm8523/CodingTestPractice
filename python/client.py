import boto3
import requests
from slack_sdk import WebClient
import time


def health_check():
    secret_name = "CS-Broker"
    region_name = "ap-northeast-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    secret = eval(get_secret_value_response['SecretString'])
    ai_server_path = secret['AI_SERVER_PATH']
    slack = WebClient(secret['AI_SERVER_SLACK_BOT_TOKEN'])
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        response = requests.get(f"{ai_server_path}:3000/healthz", timeout=1)
        if response.status_code != 200:
            slack.chat_postMessage(
                channel=secret['AI_SERVER_CHANNEL'],
                text=f"{current_time} : AI server health check fail !!!!!!!!!! \nerror message : {response.text} \n"
                     f"status code : {response.status_code}",
            )
    except requests.exceptions.ConnectTimeout:
        slack.chat_postMessage(
            channel=secret['AI_SERVER_CHANNEL'],
            text=f"{current_time} : AI server health check fail !!!!!!!!!!\n please check AI Server",
        )
    slack.chat_postMessage(
        channel="C03PB6FA92N",
        text=f"ok",
    )


if __name__ == '__main__':
    health_check()