'''
Using variables in Bash


You have just joined a data analytics team at a new company after someone left very quickly to pursue a new job (lucky them!). 
Unfortunately they left so fast they did not have time to finish the Bash script they were working on as part of a new chatbot project.

There is an error with this script - it is printing out the words yourname rather than the person's name. 
You know this has something to do with variable assignment - can you help fix this script? Add the necessary components to ensure this script runs correctly.

Instructions
100XP

-Create a variable, yourname that contains the name of the user. Let's use the test name 'Sam' for this.
-Fix the echo statement so it prints the variable and not the word yourname.
-Run your script.

'''
# Create the required variable
yourname = "Sam"

# Print out the assigned name (Help fix this error!)
echo "Hi there $yourname, welcome to the website!"
