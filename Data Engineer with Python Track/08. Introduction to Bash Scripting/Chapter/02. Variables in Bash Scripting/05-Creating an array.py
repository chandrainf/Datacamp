'''
Creating an array


In this exercise, you will practice building and accessing key properties of an array. Understanding what key properties are built in to Bash is important for fully utilizing arrays. For example, when iterating through arrays, knowing their length is very handy. Similarly, knowing how to easily return all array elements is also important for looping and also for checking your work and printing.

In this exercise, you will firstly build an array using two different methods and then access the length of the array. You will then return the entire array using a different special property.

Instructions 1/3
35 XP

- Create a normal array called capital_cities which contains the cities Sydney, New York and Paris. Do not use the declare method; fill the array as you create it. Be sure to put double quotation marks around each element!

'''
# Create a normal array with the mentioned elements
capital_cities = ("Sydney" "New York" "Paris")


'''
Instructions 2/3
35 XP

Create a normal array called capital_cities. However, use the declare method to create in this exercise.
Below, add each city, appending to the array. The cities were Sydney, New York, and Paris. Remember to use double quotation marks.

'''
# Create a normal array with the mentioned elements using the declare method
declare - a capital_cities

# Add (append) the elements
capital_cities += ("Sydney")
capital_cities += ("New York")
capital_cities += ("Paris")


'''
Instructions 3/3
30 XP

Now you have the array created, print out the entire array using a special array property.
Then print out the length of the array using another special property.

'''
# The array has been created for you
capital_cities = ("Sydney" "New York" "Paris")

# Print out the entire array
echo ${capital_cities[@]}

# Print out the array length
echo ${  # capital_cities[@]}
