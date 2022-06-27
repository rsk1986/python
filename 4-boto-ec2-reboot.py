# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-managing-instances.html

import sys
import boto3
from botocore.exceptions import ClientError

INSTANCE_ID = sys.argv[1]
ec2 = boto3.client('ec2')

try:
    ec2.reboot_instances(InstanceIds=[INSTANCE_ID], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        print("You don't have permission to reboot instances.")
        raise

try:
    response = ec2.reboot_instances(InstanceIds=[INSTANCE_ID], DryRun=False)
    print('Success', response)
except ClientError as e:
    print('Error', e)

