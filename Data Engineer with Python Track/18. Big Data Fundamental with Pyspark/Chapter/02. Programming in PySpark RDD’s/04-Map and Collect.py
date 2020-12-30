'''
Map and Collect


The main method by which you can manipulate data in PySpark is using map(). The map() transformation takes in a function and applies it to each element in the RDD. It can be used to do any number of things, from fetching the website associated with each URL in our collection to just squaring the numbers. In this simple exercise, you'll use map() transformation to cube each number of the numbRDD RDD that you created earlier. Next, you'll return all the elements to a variable and finally print the output.

Remember, you already have a SparkContext sc, and numbRDD available in your workspace.

Instructions
100 XP

- Create map() transformation that cubes all of the numbers in numbRDD.
- Collect the results in a numbers_all variable.
- Print the output from numbers_all variable.

'''
# Create map() transformation to cube numbers
cubedRDD = numbRDD.map(lambda x: x ** 3)

# Collect the results
numbers_all = cubedRDD.collect()

# Print the numbers from numbers_all
for numb in numbers_all:
    print(numb)
