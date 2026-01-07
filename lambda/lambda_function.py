import boto3
import os

def lambda_handler(event, context):
    ssm = boto3.client("ssm")

    parameter_name = os.environ.get("SSM_PARAMETER_NAME")

    response = ssm.get_parameter(
        Name=parameter_name,
        WithDecryption=False
    )

    return {
        "statusCode": 200,
        "value": response["Parameter"]["Value"]
    }
