# AWS SSM Lambda Assessment
# Overview

This repository demonstrates a Python AWS Lambda function that securely retrieves configuration values from AWS Systems Manager (SSM) Parameter Store using least-privilege IAM permissions. The infrastructure is defined using AWS CloudFormation, with optional CI/CD automation via AWS CodePipeline.

Lambda Function
      |
      v
IAM Role (Least Privilege)
      |
      v
AWS SSM Parameter Store

1. Create SSM Parameter
  aws ssm put-parameter
    --name "/assessment/db_password"
    --value "your-secure-password"
    --type String

2.Deploy CloudFormation Stack
  aws cloudformation deploy
  --template-file cloudformation/lambda-stack.yaml
  --stack-name ssm-lambda-assessment
  --capabilities CAPABILITY_NAMED_IAM

3.Validation
  Invoke the Lambda function from the AWS Console or CLI
  Verify the parameter value is retrieved successfully
  Check logs in CloudWatch Logs

3.Delete
  aws cloudformation delete-stack \
  --stack-name ssm-lambda-assessment
  
  aws ssm delete-parameter \
  --name "/assessment/db_password"


