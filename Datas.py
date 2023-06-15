
def data_from_env():
    import os
    from dotenv import load_dotenv
    load_dotenv()

    aws_access_key_id = os.environ.get('aws_access_key_id')
    aws_secret_access_key = os.environ.get('aws_secret_access_key')
    aws_s3_bucket_name = os.environ.get('aws_s3_bucket_name')

    # print(aws_access_key_id)
    # print(aws_secret_access_key)
    # print(aws_s3_bucket_name)
    return aws_access_key_id, aws_secret_access_key, aws_s3_bucket_name

if __name__ == "__main__":
    print(data_from_env())