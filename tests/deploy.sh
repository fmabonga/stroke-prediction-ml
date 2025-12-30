#!/bin/bash
aws ecr create-repository \
  --repository-name "stroke-prediction-lambda" \
  --region "us-east-1"

ECR_URL=$(aws ecr describe-repositories \
  --region us-east-1 \
  --repository-names stroke-prediction-lambda \
  --query 'repositories[0].repositoryUri' \
  --output text)


aws ecr get-login-password \
  --region "us-east-1" \
| docker login \
  --username AWS \
  --password-stdin ${ECR_URL}

REMOTE_IMAGE_TAG="${ECR_URL}:v1"

docker build -t stroke-prediction-lambda --platform linux/amd64 .
docker tag stroke-prediction-lambda ${REMOTE_IMAGE_TAG}
docker push ${REMOTE_IMAGE_TAG}

ROLE_ARN=$(aws iam get-role \
  --role-name ml-lambda-role \
  --query 'Role.Arn' \
  --output text)


aws lambda create-function \
  --function-name stroke-prediction-docker \
  --package-type Image \
  --code ImageUri=${REMOTE_IMAGE_TAG} \
  --role ${ROLE_ARN} \
  --timeout 30 \
  --region us-east-1 \
  --architectures x86_64
