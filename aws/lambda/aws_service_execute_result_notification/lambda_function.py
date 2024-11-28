import json # loggerにする

import boto3
import urllib3
from botocore.exceptions import ClientError

http = urllib3.PoolManager()


def get_secret():

    secret_name = "slack-wehbook-url"
    region_name = "ap-northeast-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response["SecretString"]

    return secret


def states_notification(event_msg: dict, url: str, channel_name: str):
    status = event_msg["detail"]["status"]
    if status == "FAILED":
        message_blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f':information_source: *<https://{event_msg["region"]}.console.aws.amazon.com/states/home?region={event_msg["region"]}#/v2/executions/details/{event_msg["detail"]["executionArn"]}| {event_msg["detail-type"]} | {event_msg["region"]} | Account: {event_msg["account"]}>*',
                },
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'*State Machine Arn*\n\
```\n\
{event_msg["detail"]["stateMachineArn"]}\n\
```\n',
                },
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'*Input*\n\
```\n\
{event_msg["detail"]["input"]}\n\
```\n',
                },
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'*Output*\n\
```\n\
{event_msg["detail"]["cause"]}\n\
```\n',
                },
            },
        ]
    else:
        message_blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f':information_source: *<https://{event_msg["region"]}.console.aws.amazon.com/states/home?region={event_msg["region"]}#/v2/executions/details/{event_msg["detail"]["executionArn"]}| {event_msg["detail-type"]} | {event_msg["region"]} | Account: {event_msg["account"]}>*',
                },
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'*State Machine Arn*\n\
```\n\
{event_msg["detail"]["stateMachineArn"]}\n\
```\n',
                },
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'*Input*\n\
```\n\
{event_msg["detail"]["input"]}\n\
```\n',
                },
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'*Output*\n\
```\n\
{event_msg["detail"]["status"]}\n\
```\n',
                },
            },
        ]

    msg = {
        "channel": channel_name,
        "username": "AWS-StepFunctions-Result",
        "blocks": message_blocks,
    }

    encoded_msg = json.dumps(msg).encode("utf-8")
    resp = http.request("POST", url, body=encoded_msg)
    print(
        {
            "message": event_msg,
            "status_code": resp.status,
            "response": resp.data,
        }
    )


def glue_job_notification(event_msg: dict, url: str, channel_name: str):
    status = event_msg["detail"]["state"]
    if status == "FAILED":
        message_blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",  # https://ap-northeast-1.console.aws.amazon.com/gluestudio/home?region=ap-northeast-1#/editor/job/store_report_spotify/runs
                    "text": f'[FAILED] :information_source: *<https://{event_msg["region"]}.console.aws.amazon.com/gluestudio/home?region={event_msg["region"]}#/editor/job/{event_msg["detail"]["jobName"]}/runs| {event_msg["detail-type"]} | {event_msg["region"]} | Account: {event_msg["account"]}>*',
                },
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'*Glue Job Name*\n\
```\n\
{event_msg["detail"]["jobName"]}\n\
```\n',
                },
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'*Message*\n\
```\n\
{event_msg["detail"]["message"]}\n\
```\n',
                },
            },
        ]
    else:
        message_blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'[SUCCEEDED] :information_source: *<https://{event_msg["region"]}.console.aws.amazon.com/gluestudio/home?region={event_msg["region"]}#/editor/job/{event_msg["detail"]["jobName"]}/runs| {event_msg["detail-type"]} | {event_msg["region"]} | Account: {event_msg["account"]}>*',
                },
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'*Glue Job Name*\n\
```\n\
{event_msg["detail"]["jobName"]}\n\
```\n',
                },
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'*Message*\n\
```\n\
{event_msg["detail"]["message"]}\n\
```\n',
                },
            },
        ]

    msg = {
        "channel": channel_name,
        "username": "AWS-Glue-Job-Result",
        "blocks": message_blocks,
    }

    encoded_msg = json.dumps(msg).encode("utf-8")
    resp = http.request("POST", url, body=encoded_msg)
    print(
        {
            "message": event_msg,
            "status_code": resp.status,
            "response": resp.data,
        }
    )


def athena_notification(event_msg: dict, url: str, channel_name: str):
    if event_msg["source"] == "aws.athena":
        message_blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'Query {event_msg["detail"]["currentState"]}',
                },
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'\n*Athena Query Detail*\n```\nquery id : {event_msg["detail"]["queryExecutionId"]}\n{event_msg["detail"]["athenaError"]["errorMessage"]}```\n',
                },
            },
        ]
    else:
        raise ValueError("条件に合致するMessageが送信されませんでした。")

    msg = {
        "channel": channel_name,
        "username": "AWS-Athena-Query-Result",
        "blocks": message_blocks,
    }
    encoded_msg = json.dumps(msg).encode("utf-8")
    resp = http.request("POST", url, body=encoded_msg)
    print(
        {
            "message": event_msg,
            "status_code": resp.status,
            "response": resp.data,
        }
    )


def lambda_handler(event, context):
    url = json.loads(get_secret())["general"]
    channel_name = "#general"
    event_message = json.loads(event["Records"][0]["Sns"]["Message"])  # Athenaの場合あとで.strip('"')する

    # テスト動作させるときと実際のイベントでは中身jsonだったりstrだったりかわるので対処
    if type(event_message) == str:
        event_message = json.loads(event_message)
    # 各種サービスごとに分岐させる
    source = event_message["source"]
    if source == "aws.states":
        states_notification(event_message, url, channel_name)
    elif source == "aws.athena":
        athena_notification(event_message, url, channel_name)
    elif source == "aws.glue":
        glue_job_notification(event_message, url, channel_name)
    else:
        print("sourceに対するイベントを受け取る実装ができていません。")
        print(f"source name = {source}")
        print(f"event = {event_message}")
