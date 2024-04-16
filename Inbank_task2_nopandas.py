import csv
from datetime import date, timedelta
import timeit
def tables_merge():
    #get the current date
    current_day = date.today()
    #the output file name based on the current date
    merged_file = "data_merged_" + str(current_day) + ".csv"
    input_files = [
        #in this case the names of files from task were used so that you won't have to change anything to review and test the code
        "data_2023-02-12.csv",
        "data_2023-02-11.csv",
        #these lines determine the names of files for previous two days from the current date
        #"data_" + str(current_day - timedelta(days=1)) + ".csv",
        #"data_" + str(current_day - timedelta(days=2)) + ".csv"
    ]
    with open(merged_file, mode='w', newline='') as fout:
        csv_writer = csv.writer(fout, delimiter=';')
        header_written = False
        # Process input filse
        for index, filename in enumerate(input_files):
            with open(filename, mode='r', newline='') as fin:
                csv_reader = csv.reader(fin, delimiter=';')  # Assuming input files also use semicolon
                for row_index, row in enumerate(csv_reader):
                    if row_index == 0:
                        if not header_written:
                            #Append the new column to the header and write it
                            row.append("file_generation_date")
                            csv_writer.writerow(row)
                            header_written = True
                        continue  #skip header from econd file
                    #append current date to each row
                    row.append(str(current_day))
                    csv_writer.writerow(row)
    print("Merged file saved as", merged_file)
print(timeit.timeit(tables_merge, number = 1)) #print out the execution time