import pandas as pd

df_target_label = pd.read_csv(u'data/graph_raw_label.csv')
df_target_relation = pd.read_csv(u'data/graph_raw_relation.csv')

address_list = list(df_target_label.address.values)
balance_list = []
print(address_list)