'''
File import performance


You've been given a large set of data to import into a Spark DataFrame. You'd like to test the difference in import speed by splitting up the file.

You have two types of files available: departures_full.txt.gz and departures_xxx.txt.gz where xxx is 000 - 013. The same number of rows is split between each file.

Instructions
100 XP

- Import the departures_full.txt.gz file and the departures_xxx.txt.gz files into separate DataFrames.
- Run a count on each DataFrame and compare the run times.

'''
# Import the full and split files into DataFrames
full_df = spark.read.csv('departures_full.txt.gz')
split_df = spark.read.csv('departures_*.txt.gz')

# Print the count and run time for each DataFrame
start_time_a = time.time()
print("Total rows in full DataFrame:\t%d" % full_df.count())
print("Time to run: %f" % (time.time() - start_time_a))

start_time_b = time.time()
print("Total rows in split DataFrame:\t%d" % split_df.count())
print("Time to run: %f" % (time.time() - start_time_b))
