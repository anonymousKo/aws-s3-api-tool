#!/usr/bin/env python
#remove public read right for all keys within a directory

#usage: remove_public.py bucketName folderName

import sys
import boto3

BUCKET = sys.argv[1]
PATH = sys.argv[2]
s3client = boto3.client("s3",aws_access_key_id="aws_access_key_id",
    aws_secret_access_key="aws_secret_access_key",region_name="ap-east-1")
paginator = s3client.get_paginator('list_objects_v2')
page_iterator = paginator.paginate(Bucket=BUCKET, Prefix=PATH)
for page in page_iterator:
    keys = page['Contents']
    for k in keys:
        response = s3client.put_object_acl(
                        ACL='private',
                        Bucket=BUCKET,
                        Key=k['Key']
                    )
