import pandas as pd
import numpy as np

print "loading csv"
uber_df = pd.read_csv('uber_trips_2015.csv', delimiter=',')
zones_df = pd.read_csv('zones.csv', delimiter=',')
print "done loading csv"

print "joining"
count_df = pd.merge(uber_df, zones_df, left_on='pickup_location_id', right_on='location_id') \
    .filter(items=['borough', 'zone']) \
    .groupby(['borough']) \
    .count()

print "Done joining: {}".format(count_df.head())
# total = count_df.agg({'zone': np.sum}).iloc[0][0]
# print "Total: {}".format(total)

# count_df['zone'] = count_df['zone'].apply(lambda x: x / 14264215.0)

#final_df = pd.merge(zones_df, count_df, how='left', on='borough') \
#   .filter(items=['borough', 'nta_code', 'zone'])
    # .select(lambda x: x == 'borough' or x == 'nta_code' or x == 'zone')

# final_df = zones_df.merge(count_df, on='borough') \
#     .filter(items=['borough', 'nta_code', 'zone'])

count_df.to_csv('uber_data.csv')