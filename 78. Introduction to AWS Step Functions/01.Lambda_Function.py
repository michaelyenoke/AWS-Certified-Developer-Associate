import json

def lambda_handler(event, context):

    # TODO implement

    return {

        'statusCode': 200,

        'body': json.dumps('You have successfully invoked the lambda function from Step Function.')

    }
