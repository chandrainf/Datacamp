'''
Interactive Use of PySpark


Spark comes with an interactive python shell in which PySpark is already installed in it. PySpark shell is useful for basic testing and debugging and it is quite powerful. The easiest way to demonstrate the power of PySpark’s shell is to start using it. In this example, you'll load a simple list containing numbers ranging from 1 to 100 in the PySpark shell.

The most important thing to understand here is that we are not creating any SparkContext object because PySpark automatically creates the SparkContext object named sc, by default in the PySpark shell.

Instructions
100 XP

- Create a python list named numb containing the numbers 1 to 100.
- Load the list into Spark using Spark Context's parallelize method and assign it to a variable spark_data.

'''
# Create a python list of numbers from 1 to 100
numb = range(1, 100)

# Load the list into PySpark
spark_data = sc.parallelize(numb)
