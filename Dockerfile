FROM public.ecr.aws/docker/library/python:3.11.4-bullseye

RUN apt-get update && apt-get install -y \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --no-cache-dir --upgrade pip


# AWS CLIのインストール
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -f awscliv2.zip && \
    aws --version

# python環境の構築
WORKDIR /dbt-athena-community-aws-resources
COPY ./pyproject.toml pyproject.toml
COPY ./requirements.lock requirements.lock
COPY ./.python-version .python-version
COPY ./README.md README.md
RUN curl -sSf https://rye.astral.sh/get | RYE_NO_AUTO_INSTALL=1 RYE_INSTALL_OPTION="--yes" bash && \
    . "$HOME/.rye/env" && \
    rye --version && \
    rye sync --no-dev --no-lock
RUN echo 'source "$HOME/.rye/env"' >> /root/.bashrc

# dbt環境の構築
COPY ./tickit/ tickit/
COPY ./dbt_project.yml dbt_project.yml
COPY ./.dbt/profiles.yml /root/.dbt/profiles.yml
COPY ./generate_static_html.py generate_static_html.py
