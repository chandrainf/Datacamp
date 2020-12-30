'''
Extracting data from files


You are a data scientist for a climate research organization.
To update some models, you need to extract temperature data for 3 regions you are monitoring.
Unfortunately the temperature reading devices are quite old and can only be configured to dump data each day into a folder called /temps on your server.
Each file contains the daily temperature for each region.

Your task is to extract the data from each file (by concatenating) into the relevant variable and print it out.
The temperature in the file region_A needs to be assigned to the variable temp_a and so on.

You will later do some more advanced calculations on these variables.

Instructions
100XP

- Create three variables from the data in the three files within temps by concatenating the content into a variable using a shell-within-a-shell.
- Print out the variables to ensure it worked.
- Save your script and run from the command line.


'''

# Create three variables from the temp data files' contents
temp_a =$(cat temps/region_A)
temp_b =$(cat temps/region_B)
temp_c =$(cat temps/region_C)

# Print out the three variables
echo "The three temperatures were $temp_a, $temp_b, and $temp_c"
