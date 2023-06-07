from DS import Loads

def demo_load_aiModel():
    import Datas
    aws_access_key_id, aws_secret_access_key, aws_s3_bucket_name = Datas.data_from_env()

    aimodel = '대충 AI모델 데이터 내용'
    filename = 'AI_model.txt'

    Loads.load_AIModel(aimodel, filename, 
                       aws_access_key_id, aws_secret_access_key, aws_s3_bucket_name)

if __name__ == "__main__":
    demo_load_aiModel()