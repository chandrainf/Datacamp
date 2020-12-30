'''
Sports analytics function


You have been contracted back to the soccer league to help them with some sports analytics. You notice that a number of the scripts undertake aggregations, just like you did in a previous exercise. Since there is a lot of duplication of code, this is an excellent opportunity to create a single useful function that can be called at many places in the script.

Your task is to create a Bash function that will take in a city name and find out how many wins they have had since recording began.

Inside the main function, this script will call out to a shell-within-a-shell which is captured in a (by default, global) variable. You can then access this variable outside the function. This was the first technique discussed in the video for getting data out of a function.

Most of the shell pipeline used has been done for you, though of course feel free to explore and understand what is happening here. Nothing there should be new to you!

Instructions
100 XP

- Create a function called get_number_wins using the function-word method.
- Create a variable inside the function called win_stats that takes the argument fed into the function to filter the last step of the shell-pipeline presented.
- Call the function using the city Etar.
- Below the function call, try to access the win_stats variable created inside the function in the echo command presented.

'''
# Create a function
function get_number_wins() {

    # Filter aggregate results by argument
    win_stats =$(cat soccer_scores.csv | cut - d "," - f2 | egrep - v 'Winner' | sort | uniq - c | egrep "$1")

}

# Call the function with specified argument
get_number_wins "Etar"

# Print out the global variable
echo "The aggregated stats are: $win_stats"
