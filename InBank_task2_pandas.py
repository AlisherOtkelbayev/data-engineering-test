import pandas as pd
from datetime import datetime, timedelta
import timeit
def tables_merge():
    # in this case the names of files from task were used so that you won't have to change anything to review and test the code
    file1 = "data_2023-02-12.csv"
    file2 = "data_2023-02-11.csv"

    #these lines determine the names of files for previous two days from the current date
    #file1 = "data_" + str(current_day - timedelta(days=1)) + ".csv"
    #file2 = "data_" + str(current_day - timedelta(days=2)) + ".csv"

    #Read CSV files into pandas dataFrame
    df1 = pd.read_csv(file1, delimiter=';')
    df2 = pd.read_csv(file2, delimiter=';')
    #merge DataFrames
    merged_df = pd.concat([df1, df2], ignore_index=True)
    #add a new column for the file generation date
    merge_date = datetime.today().strftime('%Y-%m-%d')
    merged_df["file_generation_date"] = merge_date
    #Save the merged DataFrame to csv file
    merged_file = "data_merged_" + merge_date + ".csv"
    merged_df.to_csv(merged_file, index=False, sep=';')
    print("Merged file saved as", merged_file)
print(timeit.timeit(tables_merge, number = 1))