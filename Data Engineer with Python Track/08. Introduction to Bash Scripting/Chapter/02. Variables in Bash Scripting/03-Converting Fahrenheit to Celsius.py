'''
Converting Fahrenheit to Celsius


You work in the analytics department for an Australian company that recently purchased an American company. 
The files and data from the US company are in the imperial system and need to be converted to metric. 
This sounds like a great opportunity to use your Bash skills to create a program which will assist.

Your task is to write a program that takes in a single number (a temperature in Fahrenheit) as an ARGV argument, converts it to Celsius and returns the new value. 
There may be decimal places so you will need to undertake calculations using the bc program.

At all times use 2 decimal places using the scale command for bc.

The formula for Fahrenheit to Celsius is:

    C = (F - 32) x (5/9)

Remember, since we are using arguments, you will need to run your script from the terminal pane rather than 'run this file' button.

Instructions
100XP

- Create a variable temp_f from the first ARGV argument.
- Call a shell-within-a-shell to subtract 32 from temp_f and assign to variable temp_f2.
- Using the same method, multiply temp_f2 by 5 and divide by 9, assigning to a new variable temp_c then print out temp_c.
- Save and run your script (in the terminal) using 108 Fahrenheit (the forecast temperature in Parramatta, Sydney this Saturday!).


'''
# Get first ARGV into variable
temp_f =$1

# Subtract 32
temp_f2 =$(echo "scale=2; $temp_f - 32" | bc)

# Multiply by 5/9 and print
temp_c =$(echo "scale=2; $temp_f2 * 5 / 9" | bc)

# Print the temp
echo $temp_c


'''
# Run following in command
bash script.sh 108
'''
