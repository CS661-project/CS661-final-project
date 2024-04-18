import pandas as pd
from functools import reduce


df_w_gdp = pd.read_csv('./Data_files/gdp_current_updated.csv')
df_w_pri = pd.read_csv('./Data_files/agriculture_percent_gdp_updated.csv')
df_w_sec = pd.read_csv('./Data_files/manufacturing_percent_gdp_updated.csv')
df_w_ter = pd.read_csv('./Data_files/services_percent_gdp_updated.csv')


# df_final = pd.merge(df_w_gdp, df_w_pri, on=['Country Name','Country Code'])
data_frames=[df_w_gdp,df_w_pri,df_w_sec,df_w_ter]
# df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['Country Name','Country Code'],how='outer'), data_frames)
# df_merged.to_csv('test.csv')


# result_1 = pd.concat(data_frames, join='outer', axis=1)
# result_1.to_csv('test.csv')