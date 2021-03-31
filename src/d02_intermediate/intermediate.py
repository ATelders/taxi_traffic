import sys
sys.path.insert(0, '/home/apprenant/PycharmProjects/taxi_traffic/')
from src.d00_utils.compute_distance import compute_distance, time_slot
from src.d01_data.load_data import df
import pandas as pd

# -------------------------- Cleaning --------------------------

# Put column in date format
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime'])

# Create distance column in kms
df["distance"] = df[['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']].apply(
    lambda x: compute_distance(
        x.pickup_longitude, x.pickup_latitude, x.dropoff_longitude, x.dropoff_latitude), axis=1
)

# Select relevant values
df = df[df['distance'] < 30]
df = df[df['trip_duration'] < 6000]


# -------------------------- Insights --------------------------

# Create average speed column
df['speed'] = df.apply(lambda row: 3600*row['distance']/row['trip_duration'], axis=1)

# Create day name and day number columns
df['day_name'] = df['pickup_datetime'].dt.day_name()
df['day_no'] = df['pickup_datetime'].dt.dayofweek

# Average of trips by weekday
trip_count_by_weekday = list(df.groupby(by=["day_no"])['day_no'].count().values/26)

# Number of trips by 4 hour time slots
df['hour_interval'] = df.apply(lambda row: time_slot(row['pickup_datetime'].hour), axis=1)
trip_count_by_timeslot = df.groupby(by=["hour_interval"])['hour_interval'].count()

# Number of kms by weekday
km_count_by_weekday = df.groupby(by=["day_no"])['distance'].sum().values

# Export data
# We chose csv over sql because we only use one table
df.to_csv('/home/apprenant/PycharmProjects/taxi_traffic/data/intermediate_train.csv')
