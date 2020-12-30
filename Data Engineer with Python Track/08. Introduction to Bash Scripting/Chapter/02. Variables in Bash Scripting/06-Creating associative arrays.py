'''
Creating associative arrays


Associative arrays are powerful constructs to use in your Bash scripting. They are very similar to 'normal' arrays, however they have a few important differences in their creation, manipulation and key properties.

Associative arrays allow you to index using words rather than numbers, which can be important for ease of inputting and accessing properties. For example, rather than accessing 'index 4' of an array about a city's information, you can access the city_population property, which is a lot clearer!

In this exercise we will practice creating and adding to an associative array. We will then access some special properties that are unique to associative arrays. Let's get started!

NOTE if you trigger a hint, you may need to refresh the browser to remove old variables etc that affect the test suite

Instructions 1/3
35XP

Create an empty associative array on one line called model_metrics. Do not add any elements to it here.
Add the following key-value pairs; (model_accuracy, 98), (model_name, "knn"), (model_f1, 0.82).

'''

# Create empty associative array
declare - A model_metrics

# Add the key-value pairs
model_metrics[model_accuracy] = 98
model_metrics[model_name] = "knn"
model_metrics[model_f1] = 0.82


'''
Instructions 2/3
35XP

Create the same associative array (model_metrics) all in one line. (model_accuracy, 98), (model_name, "knn"), (model_f1, 0.82). Remember you must add square brackets* around the keys!
Print out the array to see what you created.

'''
# Declare associative array with key-value pairs on one line
declare - A model_metrics = ([model_accuracy]=98 [model_name]="knn" [model_f1]=0.82)

# Print out the entire array
echo ${model_metrics[@]}


'''
Instructions 3/3
30XP

Now that you've created an associative array, print out just the keys of this associative array.

'''
# An associative array has been created for you
declare - A model_metrics = ([model_accuracy]=98 [model_name]="knn" [model_f1]=0.82)

# Print out just the keys
echo ${!model_metrics[@]}
