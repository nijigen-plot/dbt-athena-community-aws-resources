# dbt-athena-community-aws-resources

This Repository for running dbt-athena in AWS environment.

# Setup

## 1. Install and Sync rye

```
$ curl -sSf https://rye.astral.sh/get | RYE_NO_AUTO_INSTALL=1 RYE_INSTALL_OPTION="--yes" bash
$ . "$HOME/.rye/env"
$ rye --version
$ rye sync
```

## 2. Install and Apply direnv

```
$ curl -sfL https://direnv.net/install.sh | bash
$ eval "$(direnv hook bash)"
$ direnv allow
```

## 3. AWS Console

Please see this link(dummy)

## 4. Write constants in .envrc 

```
#!/bin/bash

repository_dir="$(pwd)"
export repository_dir

dbt_profiles_dir="$(pwd)/.dbt"
export dbt_profiles_dir

dbt_table_resource_s3_bucket=""
export dbt_table_resource_s3_bucket

query_output_s3_bucket=""
export query_output_s3_bucket

data_pipeline_resource_s3_bucket=""
export data_pipeline_resource_s3_bucket

aws_profile_name="dbt-local"
export aws_profile_name

slack_webhook_url_secrets_name=""
export slack_webhook_url_secrets_name

slack_webhook_url_channel_name=""
export slack_webhook_url_channel_name

cloudformation_policy_name=""
export cloudformation_policy_name

cloudformation_role_name=""
export cloudformation_role_name

local_dev_assume_role_bearer_user_name=""
export local_dev_assume_role_bearer_user_name

local_dev_role_name="localdevelopmentassumerole"
export local_dev_role_name

```

after that


```
$ direnv allow
$ rye run python ./script/jinja_render.py
$ git add
$ git commit
$ git push
```
