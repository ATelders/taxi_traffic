from src.d00_utils.compute_distance import compute_distance
from src.d01_data.load_data import df
import pandas as pd

# On ajoute une colonne dans laquelle on ajoute la distance en km
df["distance"] = df[['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']].apply(
    lambda x: compute_distance(
        x.pickup_longitude, x.pickup_latitude, x.dropoff_longitude, x.dropoff_latitude), axis=1
)

# On met les colonnes de date au bon format
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime'])

# On créé la colonne vitesse moyenne
df['speed'] = df.apply(lambda row: 3600*row['distance']/row['trip_duration'], axis=1)

# On créé la colonne jour de la course et une colonne avec le nombre associé au jour
df['day_name'] = df['pickup_datetime'].dt.day_name()
df['day_no'] = df['pickup_datetime'].dt.dayofweek

# On exporte nos données traitées
df.to_csv('/home/apprenant/PycharmProjects/taxi_traffic/data/intermediate_train.csv')
