import boto3

s3 = boto3.client('s3')

response = s3.copy_object(
            Bucket='my_bucket',
                CopySource='my_bucket/my_object',
                    Key='my_object',
                        StorageClass='STANDARD_IA'
                        )

print(response)

