'''
Reading Spark configurations


You've recently configured a cluster via a cloud provider. Your only access is via the command shell or your python code. You'd like to verify some Spark settings to validate the configuration of the cluster.

The spark object is available for use.

Instructions
100 XP

- Check the name of the Spark application instance ('spark.app.name').
- Determine the TCP port the driver runs on ('spark.driver.port').
- Determine how many partitions are configured for joins.
- Show the results.

'''
# Name of the Spark application instance
app_name = spark.conf.get('spark.app.name')

# Driver TCP port
driver_tcp_port = spark.conf.get('spark.driver.port')

# Number of join partitions
num_partitions = spark.conf.get('spark.sql.shuffle.partitions')

# Show the results
print("Name: %s" % app_name)
print("Driver TCP port: %s" % driver_tcp_port)
print("Number of partitions: %s" % num_partitions)
