import os
import boto3
from athena_utility import AthenaUtility


query = 'SELECT * FROM sample_data_for_company where year = 2021 limit 10;'
session = boto3.Session(
    aws_access_key_id=os.getenv('aws_access_key_id'),
    aws_secret_access_key=os.getenv('aws_secret_access_key'),
    region_name='us-east-1'
)

athena_utils = AthenaUtility(session=session, filename='athena_config.conf', decorator='ATHENA_UTILITY')
data = athena_utils.query_results(query=query)

print("Result Data: ")
print(data)

s3 = session.resource('s3')
athena_utils.delete_output(s3)  # This is for cleaning up the query result once data is fetched.
