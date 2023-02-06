import pymongo #
import pandas as pd
import json



client = pymongo.MongoClient("mongodb+srv://hugar_rajesh:Rajesh_0808@rajesh.ud2bw.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH='insurance.csv'
DATA_BASE_NAME='INSURANCE'
COLLECTION_NAME = 'INSURANCE_PREMIUM_PREDICTION'


if __name__=='__main__':
    df=pd.read_csv(DATA_FILE_PATH)
    print(f'Rows and columns :{df.shape}')
    
    df.reset_index(drop=True,inplace=True)
    
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    
    client[DATA_BASE_NAME][COLLECTION_NAME].insert_many(json_record)
    
    
    
    
    