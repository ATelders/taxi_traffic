from src.d00_utils.compute_distance import convert_rad, compute_distance
from src.d01_data.load_data import df
import pandas as pd


# On ajoute une colonne dans laquelle on ajoute la distance en km
df["distance"] = df[['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']].apply(
    lambda x : compute_distance(
        x.pickup_longitude, x.pickup_latitude, x.dropoff_longitude, x.dropoff_latitude), axis=1
)


