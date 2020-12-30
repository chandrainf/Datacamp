'''
Using arguments in Bash scripts


Often you will find that your Bash scripts are part of an overall analytics pipeline or process, so it's very useful to be able to take in arguments (ARGV) from the command line and use these inside your scripts.

Your job is to create a Bash script that will return the arguments inputted as well as utilize some of the special properties of ARGV elements in Bash scripts.

Since we are using arguments, you must run your script from the terminal pane, not using the 'run this file' button.

Instructions
100XP

- Echo the first and second ARGV arguments.
- Echo out the entire ARGV array in one command (not each element).
- Echo out the size of ARGV (how many arguments fed in).
- Save your script and run from the terminal pane using the arguments Bird Fish Rabbit. Don't use the ./script.sh method.

'''
# Echo the first and second ARGV arguments
echo $1
echo $2

# Echo out the entire ARGV array
echo $@

# Echo out the size of ARGV
echo $


'''
# Run following in command
bash script.sh Bird Fish Rabbit

'''
