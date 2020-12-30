'''
Removing a DataFrame from cache


You've finished the analysis tasks with the departures_df DataFrame, but have some other processing to do. You'd like to remove the DataFrame from the cache to prevent any excess memory usage on your cluster.

The DataFrame departures_df is defined and has already been cached for you.

Instructions
100 XP

- Check the caching status on the departures_df DataFrame.
- Remove the departures_df DataFrame from the cache.
- Validate the caching status again.

'''
# Determine if departures_df is in the cache
print("Is departures_df cached?: %s" % departures_df.is_cached)
print("Removing departures_df from cache")

# Remove departures_df from the cache
departures_df.unpersist()

# Check the cache status again
print("Is departures_df cached?: %s" % departures_df.is_cached)
