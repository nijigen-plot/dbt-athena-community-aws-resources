import os

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))

# cloudformation yaml template
cfn_template = env.get_template("./aws/cloudformation/dbt-infrastructure.j2.yml")
buildspec_template = env.get_template("./buildspec.j2.yml")
stepfunctions_template = env.get_template("./aws/stepfunctions/dbt_batch.j2.yml")

params = {
    "dbt_table_resource_s3_bucket": os.getenv("DBT_TABLE_RESOURCE_S3_BUCKET"),
    "query_output_s3_bucket": os.getenv("QUERY_OUTPUT_S3_BUCKET"),
    "data_pipeline_resource_s3_bucket": os.getenv("DATA_PIPELINE_RESOURCE_S3_BUCKET"),
    "slack_webhook_url_secrets_name": os.getenv("SLACK_WEBHOOK_URL_SECRETS_NAME"),
    "slack_webhook_url_channel_name": os.getenv("SLACK_WEBHOOK_URL_CHANNEL_NAME"),
    "cloudformation_policy_name": os.getenv("CLOUDFORMATION_POLICY_NAME"),
    "cloudformation_role_name": os.getenv("CLOUDFORMATION_ROLE_NAME"),
    "local_dev_assume_role_bearer_user_name": os.getenv(
        "LOCAL_DEV_ASSUME_ROLE_BEARER_USER_NAME"
    ),
    "local_dev_role_name": os.getenv("LOCAL_DEV_ROLE_NAME"),
}

with open(
    f'{os.getenv("REPOSITORY_DIR", os.path.expanduser("."))}/aws/cloudformation/dbt-infrastructure.yml',
    "w",
) as file:
    file.write(cfn_template.render(params) + "\n")
with open(
    f'{os.getenv("REPOSITORY_DIR", os.path.expanduser("."))}/buildspec.yml', "w"
) as file:
    file.write(buildspec_template.render(params) + "\n")
with open(
    f'{os.getenv("REPOSITORY_DIR", os.path.expanduser("."))}/aws/stepfunctions/dbt_batch.yml', "w") as file:
    file.write(stepfunctions_template.render(params) + "\n")
