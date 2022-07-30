import pandas as pd
import json
import os
import requests
import ssl
import urllib3
urllib3.disable_warnings()

ssl._create_default_https_context = ssl._create_unverified_context

def construct_index(row):
    """Helper function to return all the keywords from the title and genres columns"""
    if pd.isnull(row['genres']):
        genres = None
    else:
        genres = row['genres'].split('|')
         
    return f"{row['title']} {' '.join(genres) if genres else ''}"

# Load cleaned dataset
df = pd.read_csv('./data/movies_clean.csv')

# Construct the index, which includes title + genres
df['search_index'] = df.apply(construct_index, axis=1)

def df2json(df, index_name, id_col, file_loc='./data/', file_name='movies.json'):
    """Convert the dataframe to json file that is ready to be uploaded to the server"""
    if file_name in os.listdir(file_loc):
        os.remove(file_loc + file_name)
    
    with open(file_loc + file_name, 'a') as f:
        for i, row in df.iterrows():
            d1 = {'index': {'_index': index_name, '_id': f"{row[id_col]}"}}
            d2 = {}
            for col in df.columns:
                if col != id_col:
                    d2[col] = row[col]
            json.dump(d1, f)
            f.write('\n')
            json.dump(d2, f)
            f.write('\n')
            
df2json(df, 'movies', 'movieId')

def upload_json(file_loc, file_name, endpoint, username, password):
    """Bulk upload the JSON data file onto the domain"""
    url = endpoint + '/_bulk'
    with open(file_loc + file_name, 'r') as f:
        r = requests.post(url,
                          data=f,
                          auth=(username, password),
                          verify=False,
                          headers={'Content-type': 'application/json'})
    return r

print(upload_json('./data/', 'movies.json', 'https://localhost:9200', 'admin', 'admin'))