import pandas as pd
import numpy as np

# df = pd.read_csv('/Users/xanijia/Desktop/bellabeat_case_study/data/fitabase_data_3.12.16_to_4.11.16/weightLogInfo_merged.csv')

# unique_users = df['Id'].nunique()

# print(unique_users)


df = pd.read_csv('/Users/xanijia/Desktop/bellabeat_case_study/data/fitabase_data_3.12.16_to_4.11.16/dailyActivity_merged.csv')

unique_users = df['Id'].unique()

print(unique_users)

