import os

from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = "templates"

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

# cloudformation yaml template
cfn_template = env.get_template('dbt-infrastructure.yml.j2')

params = {
    "dbt_table_resource_s3_bucket": os.getenv('DBT_TABLE_RESOURCE_S3_BUCKET'),
    "query_output_s3_bucket": os.getenv('QUERY_OUTPUT_S3_BUCKET'),
    "data_pipeline_resource_s3_bucket": os.getenv('DATA_PIPELINE_RESOURCE_S3_BUCKET'),
    "slack_webhook_url_secrets_name": os.getenv('SLACK_WEBHOOK_URL_SECRETS_NAME'),
    "cloudformation_policy_name": os.getenv('CLOUDFORMATION_POLICY_NAME'),
    "dev_local_assume_role_bearer_user_name": os.getenv('DEV_LOCAL_ASSUME_ROLE_BEARER_USER_NAME')
}

with open(f'{os.getenv("REPOSITORY_DIR")}/aws/cloudformation/dbt-infrastructure.yml', 'w') as file:
    file.write(cfn_template.render(params))