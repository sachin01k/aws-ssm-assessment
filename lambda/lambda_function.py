import boto3
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ssm = boto3.client("ssm")

def lambda_handler(event, context):
    try:
        parameter_name = os.environ.get("SSM_PARAMETER_NAME")

        if not parameter_name:
            raise ValueError("SSM_PARAMETER_NAME environment variable is not set")

        logger.info(f"Fetching SSM parameter: {parameter_name}")

        response = ssm.get_parameter(
            Name=parameter_name,
            WithDecryption=True
        )

        value = response["Parameter"]["Value"]

        return {
            "statusCode": 200,
            "value": value
        }

    except Exception as e:
        logger.error("Error while fetching SSM parameter", exc_info=True)

        return {
            "statusCode": 500,
            "error": str(e)
        }
