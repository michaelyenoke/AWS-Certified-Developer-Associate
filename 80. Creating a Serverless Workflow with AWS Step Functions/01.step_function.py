{
  "Comment": "Read or write data from DynamoDB and send Success or Failed message",
  "StartAt": "TableOperationType",
  "States": {
    "TableOperationType": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.TableOperation",
          "StringEquals": "Read",
          "Next": "ReadDataFromTable"
        },
        {
          "Variable": "$.TableOperation",
          "StringEquals": "Write",
          "Next": "WriteDataToTable"
        }
      ],
      "Default": "NoMatch"
    },
    "ReadDataFromTable": {
      "Type": "Task",
      "Resource": "arn",
      "Parameters": {
        "TableName": "mydynamodbtable",
        "Key": {
          "ID": {
            "S.$": "$.ID"
          }
        }
      },
      "Catch": [
        {
          "ErrorEquals": [
            "States.TaskFailed"
          ],
          "Next": "FailureNotification"
        }
      ],
      "ResultPath": "$.DynamoDB",
      "Next": "CheckStatus"
    },
    "WriteDataToTable": {
      "Type": "Task",
      "Resource": "arn",
      "Parameters": {
        "TableName": "mydynamodbtable",
        "Item": {
          "ID": {
            "S.$": "$.ID"
          },
          "Name": {
            "S.$": "$.Name"
          }
        }
      },
      "Catch": [
        {
          "ErrorEquals": [
            "States.TaskFailed"
          ],
          "Next": "FailureNotification"
        }
      ],
      "ResultPath": "$.DynamoDB",
      "Next": "CheckStatus"
    },
    "NoMatch": {
      "Type": "Fail",
      "Error": "Unknown Table Operation",
      "Cause": "No Matches!"
    },
    "CheckStatus": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.DynamoDB.SdkHttpMetadata.HttpStatusCode",
          "NumericEquals": 200,
          "Next": "SuccessNotification"
        },
        {
          "Not": {
            "Variable": "$.DynamoDB.HttpStatusCode",
            "NumericEquals": 200
          },
          "Next": "FailureNotification"
        }
      ]
    },
    "SuccessNotification": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sns:publish",
      "Parameters": {
        "Message": "DynamoDB Operation Success !",
        "TopicArn": "arn"
      },
      "End": true
    },
    "FailureNotification": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sns:publish",
      "Parameters": {
        "Message": "DynamoDB Operation Failed !",
        "TopicArn": "arn"
      },
      "End": true
    }
  }
}
