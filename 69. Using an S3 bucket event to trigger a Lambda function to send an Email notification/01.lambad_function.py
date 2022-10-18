import boto3
import json

def lambda_handler(event, context):
    
    for e in event["Records"]:
        bucketName = e["s3"]["bucket"]["name"]
        objectName = e["s3"]["object"]["key"]
        eventName = e["eventName"]
    
    bClient = boto3.client("ses")
    
    eSubject = 'AWS Lab' + str(eventName) + 'Event'
    
    eBody = """
        <br>
        Hi User,<br>
        
        something......<br>
        
        We are here to notify you that {} an event was triggered.<br>
        Bucket name : {} <br>
        Object name : {}
        <br>
    """.format(eventName, bucketName, objectName)
    
    send = {"Subject": {"Data": eSubject}, "Body": {"Html": {"Data": eBody}}}
    result = bClient.send_email(Source= "Your_Email_Address", Destination= {"ToAddresses": ["Your_Email_Address"]}, Message= send)
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
    
