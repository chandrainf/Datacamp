'''
Comparing broadcast vs normal joins


You've created two types of joins, normal and broadcasted. Now your manager would like to know what the performance improvement is by using Spark optimizations. If the results are promising, you'll be given more opportunity to tweak the Spark setup as needed.

Your DataFrames normal_df and broadcast_df are available for your use.

Instructions
100 XP

- Execute .count() on the normal DataFrame.
- Execute .count() on the broadcasted DataFrame.
- Print the count and duration of the DataFrames noting and differences.

'''
start_time = time.time()
# Count the number of rows in the normal DataFrame
normal_count = normal_df.count()
normal_duration = time.time() - start_time

start_time = time.time()
# Count the number of rows in the broadcast DataFrame
broadcast_count = broadcast_df.count()
broadcast_duration = time.time() - start_time

# Print the counts and the duration of the tests
print("Normal count:\t\t%d\tduration: %f" % (normal_count, normal_duration))
print("Broadcast count:\t%d\tduration: %f" %
      (broadcast_count, broadcast_duration))
