from DS import Loads

def demo_load_aiModel():
    import Datas
    aws_access_key_id, aws_secret_access_key, aws_s3_bucket_name = Datas.data_from_env()

    aimodel = 'kg, year, month, day' #변수
    filename = '고구마_특(1등).pickle' #파일 이름 

    Loads.load_AIModel(aimodel, filename, 
                       aws_access_key_id, aws_secret_access_key, aws_s3_bucket_name)

if __name__ == "__main__":
    demo_load_aiModel()