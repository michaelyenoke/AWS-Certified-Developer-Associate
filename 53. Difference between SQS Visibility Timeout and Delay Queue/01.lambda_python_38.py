import json
import boto3

def lambda_handler(event, context):
    try:
        sqsClient = boto3.client("sqs", region_name="us-east-1")
        try:
            response = sqsClient.receive_message(
                QueueUrl="<your Queue URL>",
                AttributeNames=['All'],
            )
            print(response)
            return response
        except Exception as e:
            print("Get queue message failed because ", e)
    except Exception as e:
        print("Client connection to SQS failed because ", e)
