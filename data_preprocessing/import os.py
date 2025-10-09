import os

csv_march_to_april = "/Users/xanijia/Desktop/fitbit_case_study/fitabase_data/fitabase_data_3.12.16-4.11.16"
csv_april_to_may = "/Users/xanijia/Desktop/fitbit_case_study/fitabase_data/fitabase _data_4.12.16-5.12.16"

def find_unique_csvs(csv_march_to_april, csv_april_to_may):
  
    # get all files in csv_march_to_april and filter for csvs
    csvs_in_csv_march_to_april = {f for f in os.listdir(csv_march_to_april) if f.endswith('.csv')}

    # get all files in csv_april_to_may and filter for csvs
    csvs_in_csv_april_to_may = {f for f in os.listdir(csv_april_to_may) if f.endswith('.csv')}

    # find CSVs in csv_april_to_may that are not in csv_march_to_april
  
    unique_csvs = list(csvs_in_csv_april_to_may - csvs_in_csv_march_to_april)

    print(unique_csvs)


  
# unique_files = find_unique_csvs(csv_april_to_may, csv_march_to_april)

# if unique_files: 
#     print(f"CSV files present in '{csv_april_to_may}' but not in '{csv_march_to_april}':")
#     for filename in unique_files: 
#         print(filename)
# else: 
#     print(f"No unique CSV files found in '{csv_april_to_may}' compared to '{csv_march_to_april}'.")

