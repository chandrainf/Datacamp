'''
Summing an array


A common programming task is obtaining the sum of an array of numbers. Let's create a function to assist with this common task.

Create a Bash function that will take in an array of numbers and return its sum. We will use bc rather than expr to ensure we can handle decimals.

Your company's security rules state that all variables in functions must be restricted local scope so you will need to keep this in mind.

An array of numbers you can use for a test of your function would be the daily sales in your organization this week (in thousands):

14 12 23.5 16 19.34 which should sum to 84.84

Instructions
100XP

- Create a function called sum_array and add a base variable (equal to 0) called sum with local scope. You will loop through the array and increment this variable.
- Create a FOR loop through the ARGV array inside sum_array (hint: This is not $1! but another special array property) and increment sum with each element of the array.
- Rather than assign to a global variable, echo back the result of your FOR loop summation.
- Call your function using the test array provided and echo the result. You can capture the results of the function call using the shell-within-a-shell notation.

'''
# Create a function with a local base variable
function sum_array() {
    local sum = 0
    # Loop through, adding to base variable
    for number in "$@"
    do
    sum =$(echo "$sum + $number" | bc)
    done
    # Echo back the result
    echo $sum
}
# Call function with array
test_array = (14 12 23.5 16 19.34)
total =$(sum_array "${test_array[@]}")
echo "The sum of the test array is $total"
