# Data Engineering Test
InBank task

This is a commentary on my hometask from InBank.

This repository contains an SQL query for task 1(query_task1.sql) and 2 different python scripts for task 2(Inbank_task2_pandas.py & Inbank_task2_nopandas.py), along with files and other scripts that have been used in my work and testing.

For task 1 I have used a slightly edited query provided in the github to populate the tables. Because MySQL has some differences from the original Snowflake syntaxis it was written in.

The task 2 has been completed with 2 different python scripts - one with the use of pandas and one without pandas and only python standard libraries. This has been done since I’ve wanted to test the effectiveness of both approaches and measure the execution times to see which script would handle the task better.
The execution times were measured using the python timeit module.

Both scripts were tested first on the CSV files provided with task and then on CSV files with 1,000/10,000 rows and 5 columns of random values from 1 to 1000, that I’ve populated by a script in this repository called “populate_CSV_random.py”

As a result I’ve found out that in case of CSV files provided, without the pandas approach is much more effective, with the code execution time on several tries of ~0.00073 seconds, while with the pandas the time was ~0.0057 seconds, which is approximately 7 times slower.

The similar tendency was observed in the case of 2 CSV files with 1,000 rows and 5 columns: pandas ~0.0089 seconds, nopandas ~0.0052 seconds. However, as it could be seen the difference in execution times grew smaller as the file size increased.

With the 10,000 rows and 5 columns pandas performed slightly quicker with the time of ~0.0422 seconds, while nopandas has shown ~0.0457 seconds.

The execution times, however, may vary from one test to another, depending on a variety of factors, such as the hardware it was performed on.

So, in this particular task’s case it could be said that the solution without pandas is the better one, since it completed merging two task files much faster with the same result. But given the implication of it being used to aggregate much bigger financial data of a bank - pandas is better, since it performed better with larger file size.

Since the task 2 doesn’t specify, I have assumed several points and task ideas. 

First - the python script is to be executed each monday morning, so, based on the current date(using python datetime module) it determines the dates and names of files for the previous 2 days, sunday and saturday. However, the final version of scripts contains the lines that serve this functionality only as commentary lines, taking as an input the files with names of those provided by the task from github. It was done so that it would be easier for you, the one who reviews it, to simply execute it with those files without having to alter anything.

Second - the date when the output file was generated fills the entire column for the “file generation date”, since I’ve decided that while it may look like a clutter or useless, unnecessary amount of information, it may be used for the purpose of indexing, addressing and finding certain rows by the file generation date. If the null value was used for filling all rows of the last column, except first, it would look more appealing on a spreadsheet, but might lead to some errors regarding the future uses of it.

Third - the file structure is consistent in both input files.

I would love to discuss this assignment and my solutions with you and answer any questions regarding it. Hope to see you at the interview!

Thanks for your attention and have a nice day!
