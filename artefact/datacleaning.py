import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

df = pd.read_csv('spotify.csv',encoding = 'ANSI')




#print(df.info())
# for index, row in df.iterrows():
#     #print(row['artist(s)_name'], row['track_name'])
#     if (row['artist(s)_name'].find('¿')>-1):
#         print(row['artist(s)_name'],index)
#There was invalid characters in artist name and track name , so i didnt end up using these columns         

df= df.drop('acousticness_%',axis = 1 )
df = df.drop('instrumentalness_%',axis=1)

df = df.drop('key',axis=1)

df = df.drop('mode',axis=1)

df = df.drop('artist_count',axis=1)

df = df.drop('released_day',axis=1)

df = df.drop('speechiness_%',axis=1)
df = df.drop("in_shazam_charts" ,axis=1)

df = df.drop('valence_%', axis=  1)
df.rename(columns={'artist(s)_name': 'artist_name'}, inplace=True)

#i checked to see if there was any missing values , there was in shazam, i also  quickly realised this information  was not
#necessary so  i removed the file




 






cred = credentials.Certificate("lcacc2024-firebase-adminsdk-8bnwo-9b308a3274.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://lcacc2024-default-rtdb.europe-west1.firebasedatabase.app//'})
#print(f)
#df = df.set_index('track_name')

data_dict = df.to_dict()

#print(df.info)
ref = db.reference('/')
ref.set(data_dict)
#ref.set([])
print("sent to firebase")
