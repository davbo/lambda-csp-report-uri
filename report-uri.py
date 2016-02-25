from __future__ import print_function
from datetime import datetime

import boto3
import json

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    """Events are CSP reports, to be stored in S3"""
    result = {"report-created": False}
    if 'csp-report' in event:
        s3.Object('csp-reports', datetime.now().strftime('%Y/%m/%d/%H-%M-%S-%f.json')).put(Body=json.dumps(event))
        result["report-created"] = True
    return result
