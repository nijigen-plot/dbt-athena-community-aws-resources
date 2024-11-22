FROM public.ecr.aws/docker/library/python:3.10.14-bullseye

RUN apt-get update && apt-get install -y \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --no-cache-dir --upgrade pip


# AWS CLIのインストール
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install
RUN rm -f awscliv2.zip
RUN aws --version

# python環境の構築
WORKDIR /dbt-athena-community-aws-resources
COPY ./pyproject.toml pyproject.toml
RUN rye sync --no-dev --no-lock

# dbt環境の構築
COPY ./dbt_project.yml dbt_project.yml
COPY ./.dbt/profiles.yml /root/.dbt/profiles.yml
COPY ./generate_static_html.py generate_static_html.py
RUN sed -i '/aws_profile_name: dbt-local/d' /root/.dbt/profiles.yml
