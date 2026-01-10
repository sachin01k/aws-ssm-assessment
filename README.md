# AWS Lambda SSM Reader with CI/CD (CloudFormation + CodePipeline)

## Overview
This repository demonstrates a Python AWS Lambda function that securely retrieves configuration values from AWS Systems Manager (SSM) Parameter Store using least-privilege IAM permissions. The infrastructure is defined using AWS CloudFormation, with optional CI/CD automation via AWS CodePipeline.

The Lambda function reads a value from **AWS SSM Parameter Store** and returns it.

---

## Architecture

- AWS Lambda (Python 3.x)
- AWS SSM Parameter Store
- AWS IAM (Least privilege)
- AWS CodePipeline
- AWS CodeBuild
- AWS CloudFormation

---

## 🔄 CI/CD Flow

1. Source code is uploaded to S3 as `source.zip`
2. CodePipeline is triggered
3. CodeBuild packages Lambda code into `lambda.zip`
4. CloudFormation deploy stage creates/updates Lambda stack
5. Lambda reads value from SSM Parameter Store

---

## Security & Best Practices

- IAM roles follow **principle of least privilege**
- No hardcoded credentials
- SSM parameter name passed via environment variable
- Infrastructure managed entirely using CloudFormation
- Easy cleanup by deleting CloudFormation stacks

---

## Example Lambda Response

```json
{
  "statusCode": 200,
  "value": "root"
}
```

## Description
This PR implements an AWS Lambda function that reads values from SSM Parameter Store.
The deployment is automated using AWS CodePipeline and CloudFormation following IaC best practices.

## Key Features
- Lambda written in Python 3.x
- IAM roles with least privilege
- CloudFormation for infrastructure
- CodePipeline with CloudFormation deploy stage

## Cleanup
All resources can be removed by deleting the CloudFormation stacks.



