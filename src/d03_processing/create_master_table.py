import pandas as pd
from src.d00_utils.compute_distance import intervalle_trajet

# On importe nos données traitées
df = pd.read_csv('/home/apprenant/PycharmProjects/taxi_traffic/data/intermediate_train.csv')

# On va calculer le nombre de kms parcourus par jour de la semaine
kmparc = df.groupby(by=["day_no"])['distance'].sum().values

# On va calculer le nombre de trajet en fonction du jour de la semaine
nb_traj_sem = list(df.groupby(by=["day_no"])['day_no'].count().values)

# Nombre de trajets effectués en fonction de l’horaire de la journée par tranche de 4h
# On commence par associer à chaque ligne
df['hour_interval'] = df.apply(lambda row: intervalle_trajet(row['pickup_datetime'].hour), axis=1)
nb_traj_hour = df.groupby(by=["hour_interval"])['hour_interval'].count().values