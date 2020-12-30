'''
Get the current day


Whilst working on a variety of Bash scripts in your data analytics infrastructure, you find that you often need to get the current day of the week. You can see this is unnecessary duplication of code and can be refactored (reduce the size by writing more efficient code) using your new skills in Bash functions.

Write a simple Bash function that, when called, will simply print out the current day of the week. This will involve parsing the output of the date program from a shell-within-a-shell.

A reminder that the output of date will look something like this (depending on the timezone you are calling it from!)

    Fri 27 Dec 2019 14:24:33 AEDT

You want to extract the Fri part only.

Instructions
100XP

- Set up a function called what_day_is_it without using the word function (as you did using the function-word method).
- Parse the output of date into a variable called current_day. The extraction component has been done for you.
- Echo the result.
- Call the function just below the function definition.

'''
# Create function
what_day_is_it() {

    # Parse the results of date
    current_date =$(date | cut - d " " - f1)

    # Echo the result
    echo $current_date
}

# Call the function
what_day_is_it
