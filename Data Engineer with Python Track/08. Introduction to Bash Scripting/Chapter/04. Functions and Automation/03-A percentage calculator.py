'''
A percentage calculator


In your work as a data scientist, you often find yourself needing to calculate percentages within Bash scripts. This would be a great opportunity to create a nice modular function to be called from different places in your code.

Your task is to create a Bash function that will calculate a percentage of two numbers that are given as arguments and return the value.

A test example you can think of to use in this script is a model that you just ran where there were 456 correct predictions out of 632 on the test set.

Remember that the shell can't natively handle decimal places, so it will be safer to employ the use of bc.

Instructions
100XP

- Create a function called return_percentage using the function-word method.
- Create a variable inside the function called percent that divides the first argument fed into the function by the second argument.
- Return the calculated value by echoing it back.
- Call the function with the mentioned test values of 456 (the first argument) and 632 (the second argument) and echo the result.

'''
# Create a function
function return_percentage() {

    # Calculate the percentage using bc
    percent =$(echo "scale=4; $1 / $2" | bc)

    # Return the calculated percentage
    echo $percent
}

# Call the function with 456 and 632 and echo the result
return_test =$(return_percentage 456 632)
echo "456 out of 632 as a percent is $return_test"
