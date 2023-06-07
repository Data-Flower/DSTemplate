from DS.Get_by_dates import get_obj as get_dataframe_by_dates

def demo_case1():
    """
    특정 날짜만 가져오는 코드
    """
    # Datas에 작성된 data_from_env 함수로 필수 AWS 접속 데이터를 가져온다.
    import Datas
    aws_access_key_id, aws_secret_access_key, aws_s3_bucket_name = Datas.data_from_env()

    # case 1: 특정 날짜만 가져오기
    date1 = '20230403'
    date2 = None    

    df = get_dataframe_by_dates(aws_access_key_id, aws_secret_access_key, aws_s3_bucket_name, 
                           date1, date2)

    print(df)

def demo_case2():
    """
    시작 날짜부터 종료 날짜까지 가져오는 코드
    """
    # Datas에 작성된 data_from_env 함수로 필수 AWS 접속 데이터를 가져온다.
    import Datas
    aws_access_key_id, aws_secret_access_key, aws_s3_bucket_name = Datas.data_from_env()

    # case 2: 시작 날짜부터 종료 날짜까지 가져오기
    date1 = '20230403'
    date2 = '20230407'    

    df = get_dataframe_by_dates(aws_access_key_id, aws_secret_access_key, aws_s3_bucket_name, 
                           date1, date2)
    
    print(df)

if __name__ == "__main__":
    demo_case1()
    demo_case2()