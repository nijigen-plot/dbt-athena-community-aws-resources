#! /bin/bash

WORKDIR='/tmp/lambda/zip/'
TARGET_BUCKET='nijipro-dbt-resources'
mkdir -p ${WORKDIR}

cd aws/lambda || exit
for dir in */; do
    zip -r -j "${WORKDIR}$(basename "${dir}").zip" "${dir}lambda_function.py"
done

aws s3 sync --exact-timestamps --delete ${WORKDIR} s3://${TARGET_BUCKET}/lambda/
