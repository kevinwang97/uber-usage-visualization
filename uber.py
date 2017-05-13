import pandas as pd

print "loading csv"
uber_df = pd.read_csv('uber_trips_2015.csv', delimiter=',')
zones_df = pd.read_csv('zones.csv', delimiter=',')
print "done loading csv"

count_df = pd.merge(uber_df, zones_df, left_on='pickup_location_id', right_on='location_id') \
    .filter(items=['borough', 'nta_code', 'zone']) \
    .groupby(['borough', 'nta_code']) \
    .count()
    # .select(lambda x: x == 'borough' or x == 'nta_code' or x == 'zone')

count_df.to_csv('uber_data.csv')