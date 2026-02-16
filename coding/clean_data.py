import pandas as pd 
data = pd.read_csv('cleaning_data.csv', usecols=['track_name', 'track_popularity', 'artist_name', 'artist_followers', 'album_name', 'album_type','album_total_tracks'])

column_values = data[['track_name', 'track_popularity', 'artist_name', 'artist_followers', 'album_name', 'album_type', 'album_total_tracks']].values.tolist()
print(column_values)

data = data[data['track_popularity'] >= 50]


data = data[data['artist_followers'] >= 500000]

data = data[data['album_type'] == 'album']






data.to_csv('filtered_data.csv', index=False)
print("Cleaned data saved as 'filtered_data.csv' ")

print(data.describe())
data.info()


