#! /bin/bash

AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query "Account" --output text)
ROLE_ARN="arn:aws:iam::$AWS_ACCOUNT_ID:role/$LOCAL_DEV_ROLE_NAME"
SESSION_NAME="$AWS_PROFILE_NAME"
PROFILE_NAME="$AWS_PROFILE_NAME"

CREDENTIALS=$(aws sts assume-role --role-arn "$ROLE_ARN" --role-session-name "$SESSION_NAME" )

ACCESS_KEY=$(echo "$CREDENTIALS" | jq -r '.Credentials.AccessKeyId')
SECRET_KEY=$(echo "$CREDENTIALS" | jq -r '.Credentials.SecretAccessKey')
SESSION_TOKEN=$(echo "$CREDENTIALS" | jq -r '.Credentials.SessionToken')

# ~/.aws/credentialsファイルに認証情報を追加または更新
aws configure set aws_access_key_id "$ACCESS_KEY" --profile "$PROFILE_NAME"
aws configure set aws_secret_access_key "$SECRET_KEY" --profile "$PROFILE_NAME"
aws configure set aws_session_token "$SESSION_TOKEN" --profile "$PROFILE_NAME"
aws configure set region ap-northeast-1 --profile "$PROFILE_NAME"
