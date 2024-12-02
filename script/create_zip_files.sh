#! /bin/bash

if [ -z "${DATA_PIPELINE_RESOURCE_S3_BUCKET}" ]; then
    echo "Error: DATA_PIPELINE_RESOURCE_S3_BUCKET variable is not set." >&2
    exit 1
fi
WORKDIR='/tmp/lambda/zip/'
mkdir -p ${WORKDIR}

cd aws/lambda || exit
for dir in */; do
    zip -r -j "${WORKDIR}$(basename "${dir}").zip" "${dir}lambda_function.py"
done

aws s3 sync --exact-timestamps --delete ${WORKDIR} s3://"${DATA_PIPELINE_RESOURCE_S3_BUCKET}"/lambda/
