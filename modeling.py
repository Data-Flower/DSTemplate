import pandas as pd
import numpy as np
from lightgbm import LGBMRegressor
import pickle

def save_model(model, model_file):
    try:
        with open(model_file, 'wb') as file:
            pickle.dump(model, file)
        print(f"The model has been saved to {model_file} successfully.")
    except Exception as e:
        print(f"An error occurred while saving the model to {model_file}. Error: {str(e)}")
        
def load_model(model_file):
    try:
        with open(model_file, 'rb') as file:
            model = pickle.load(file)
        print(f"The model has been loaded from {model_file} successfully.")
        return model
    except Exception as e:
        print(f"An error occurred while loading the model from {model_file}. Error: {str(e)}")
        return None
    
def make_model(pummok = '고구마', grade = '특(1등)', path = 'data/df.csv'):
    
    df = pd.read_csv(path, index_col = 0)
    df = df.query('PUMMOK == @pummok')
    df = df.query('DDD == @grade')
    
    df['Y']=  df['ADJ_DT'].astype('str').str[:4].astype('int')
    df['M']=  df['ADJ_DT'].astype('str').str[4:6].astype('int')
    df['D']=  df['ADJ_DT'].astype('str').str[-2:].astype('int')
    df['UUN']=  df['UUN'].str[:-2].astype('float')
    df = df.drop(columns = ['ADJ_DT', 'DDD', 'PUMMOK'])
    
    y = df['PPRICE']
    X = df.drop(columns = 'PPRICE')
    
    model = LGBMRegressor()
    model.fit(X, y)
    save_model(model, f'{pummok}_{grade}.pickle')

def predict_model(year, month, day, kg, model_name ='고구마_특(1등).pickle'):
    model = load_model(model_name)
    print( f'해당 품목의 {year}년 {month}월 {day}일 가격은 {np.round(model.predict([[kg, year, month, day]])[0], 1)}원으로 예측됩니다.')

if __name__ == "__main__":
    # make_model()
    predict_model(2023, 6, 10, 10)