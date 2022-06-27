#https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-managing-instances.html

import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)
