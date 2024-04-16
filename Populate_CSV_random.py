import csv
import random
#number of rows and columns
num_rows = 10000
num_columns = 5
#output files
filename1 = "test_data.csv"
filename2 = "test_data2.csv"
#generate the random values to fill into the table
def generate_random_row(num_columns):
    return [random.randint(1, 1000) for _ in range(num_columns)]

#Create and write data to the CSV file
with open(filename1, mode='w', newline='') as file:
    writer = csv.writer(file, delimiter = ";")
    #Write a header
    writer.writerow(['Column1', 'Column2', 'Column3', 'Column4', 'Column5'])
    # Write the data rows
    for c in range(num_rows):
        row = generate_random_row(num_columns)
        writer.writerow(row)

#the same as previous one
with open(filename2, mode='w', newline='') as file:
    writer = csv.writer(file, delimiter = ";")
    writer.writerow(['Column1', 'Column2', 'Column3', 'Column4', 'Column5'])
    for c in range(num_rows):
        row = generate_random_row(num_columns)
        writer.writerow(row)

print(f"CSV file '{filename1}' with {num_rows} rows and {num_columns} columns has been created.")
#could have been done with just one function