import pymongo
import pandas as pd
import json

from Census.config import mongo_client

DATA_FILE_PATH="/config/workspace/adult.csv"
DATABASE_NAME="Adult_Census"
COLLECTION_NAME="Adult"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    #Convert dataframe to json so that we can dump these record in mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])