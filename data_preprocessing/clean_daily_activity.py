import pandas as pd 

# read dailyActivity csv from march to april file
df = pd.read_csv('/data/fitabase_data_3.12.16_to_4.11.16/dailyActivity_merged.csv', encoding="latin1")

# rename columns to match sql database table
df.columns = ['id', 'activity_date', 'total_steps', 'total_distance', 'tracker_distance', 'logged_activities', 'very_active_distance', 'moderately_active_distance', 'light_active_distance', 'sedentary_active_distance', 'very_active_minutes', 'fairly_active_minutes', 'lightly_active_minutes', 'sedentary_minutes', 'calories']

# read dailyActivity csv from april to march file
df_2 = pd.read_csv('/data/fitabase_data_4.12.16_to_5.12.16/dailyActivity_merged.csv')

# rename columns to match sql database table
df_2.columns = ['id', 'activity_date', 'total_steps', 'total_distance', 'tracker_distance', 'logged_activities', 'very_active_distance', 'moderately_active_distance', 'light_active_distance', 'sedentary_active_distance', 'very_active_minutes', 'fairly_active_minutes', 'lightly_active_minutes', 'sedentary_minutes', 'calories']

# save to new clean csv







