# 📘 Bellabeat Case Study – Marketing Analysis Change Log

## Initial Setup

### 2025-10-08
- 📦 **Downloaded** the Fitabase dataset from Kaggle:  
  [https://www.kaggle.com/datasets/arashnic/fitbit?resource=download](https://www.kaggle.com/datasets/arashnic/fitbit?resource=download)
- 🗂️ **Created** a project folder on desktop named `bellabeat_case_study`.
- 🗃️ **Unzipped** the downloaded Fitabase zip file.
- 📁 **Moved** the following folders into a new `data` directory inside the project repo:
  - `Fitabase Data 3.12.16-4.11.16`
  - `Fitabase Data 4.12.16-5.12.16`
- ✏️ **Renamed** data folders for consistency:
  - `Fitabase Data 3.12.16-4.11.16` → `fitabase_data_3.12.16_to_4.11.16`
  - `Fitabase Data 4.12.16-5.12.16` → `fitabase_data_4.12.16_to_5.12.16`
- 🧩 **Created** additional project subfolders:
  - `sql_scripts/`
  - `data_preprocessing/`
  - `db/`
  - `designing/`
- 🌿 **Initialized Git repository** using SourceTree and connected it to GitHub (`bellabeat_case_study` repo).
- 🎨 **Created a changelog** using markdown and committed changes to remote repo. 

---

✅ *Next planned steps:*  
- Design database diagram to organize the csv data into columns with data types and store it in the designing folder
- Create a SQLite database, use CREATE TABLE scripts to create tables using the db diagram and standardized, sql friendly column names 
- Clean csv's with pandas - rename column names to match sql tables, merge matching csv files and names, split datetime columns into two separate columbns if needed, etc.
- Import/Load cleaned csvs into respective tables  
- Begin SQL-based data exploration and preprocessing.


