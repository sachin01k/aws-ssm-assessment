# \# AWS SSM Lambda Assessment

# 

# \## Overview

# This project demonstrates a Python AWS Lambda function that retrieves

# configuration values from AWS SSM Parameter Store using least-privilege IAM.

# 

# \## Architecture

# Lambda → IAM Role → SSM Parameter Store

# 

# \## Features

# \- Secure parameter retrieval (no hardcoding)

# \- Least privilege IAM policies

# \- Infrastructure as Code using CloudFormation

# \- CI/CD using AWS CodePipeline

# 

# \## Deployment

# 1\. Create SSM parameter: `/assessment/db\_password`

# 2\. Deploy CloudFormation stack:

# &nbsp;  - `cloudformation/lambda-stack.yaml`

# 3\. Validate Lambda execution

# 

# \## Cleanup

# Delete CloudFormation stacks to avoid charges.



