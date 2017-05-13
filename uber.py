import pandas as pd
import numpy as np

print "loading csv"
uber_df = pd.read_csv('uber_trips_2015.csv', delimiter=',')
# demographics_df = pd.read_csv('demographics.csv', delimiter=',')
# geographic_df = pd.read_csv('geographic.csv', delimiter=',')
zones_df = pd.read_csv('zones.csv', delimiter=',')
# green_df = pd.read_csv('green_trips.csv', delimiter=',')
# yellow_df = pd.read_csv('yellow_trips.csv', delimiter=',')
print "done loading csv"

count_df = pd.merge(uber_df, zones_df, left_on='pickup_location_id', right_on='location_id') \
    .groupby(['borough', 'nta_code']) \
    .count()
    # .select(lambda x: x == 'borough' or x == 'nta_code' or x == 'zone')

count_df.to_csv('uber_data.csv')