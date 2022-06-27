##https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html
## Also see for detailed s3 here => https://realpython.com/python-boto3-aws-s3/

##Sample program to upload a file in S3 bucket
import boto3

s3=boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
data = open('test.txt', 'rb')
#s3.Bucket('myftp12233445').put_object(Key='test.txt', Body=data)
s3.Bucket(bucket.name).put_object(Key='test.txt', Body=data)

