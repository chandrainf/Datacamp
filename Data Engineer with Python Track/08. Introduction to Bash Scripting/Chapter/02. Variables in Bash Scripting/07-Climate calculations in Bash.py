'''
Climate calculations in Bash


You are continuing your work as a data scientist for the climate research organization. In a previous exercise, you extracted temperature data for 3 regions you are monitoring from some files from the /temps directory.

Remember, each file contains the daily temperature for each region. However, only two regions will be used in this exercise.

In this exercise, the lines from your previous exercise are already there which extract the data from each file. However, this time you will then store these variables in an array, calculate the average temperature of the regions and append this to the array.

For example, for temperatures of 60 and 70, the array should have 60, 70, and 65 as its elements.

Instructions
100XP

- Create an array with the two temp variables as elements.
- Call an external program to get the average temperature. You will need to sum array elements then divide by 2. Use the scale parameter to ensure this is to 2 decimal places.
- Append this new variable to your array and print out the entire array.
- Run your script.

'''
# Create variables from the temperature data files
temp_b = "$(cat temps/region_B)"
temp_c = "$(cat temps/region_C)"

# Create an array with these variables as elements
region_temps = ($temp_b $temp_c)

# Call an external program to get average temperature
average_temp =$(echo "scale=2; (${region_temps[0]} + ${region_temps[1]}) / 2" | bc)

# Append average temp to the array
region_temps += ($average_temp)

# Print out the whole array
echo ${region_temps[@]}
