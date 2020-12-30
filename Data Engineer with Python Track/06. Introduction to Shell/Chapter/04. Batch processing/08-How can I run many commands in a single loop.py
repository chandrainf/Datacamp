'''
How can I run many commands in a single loop?


Printing filenames is useful for debugging, but the real purpose of loops is to do things with multiple files. This loop prints the second line of each data file:

    for file in seasonal/*.csv; do head -n 2 $file | tail -n 1; done

It has the same structure as the other loops you have already seen: all that's different is that its body is a pipeline of two commands instead of a single command.

Instructions
100 XP

Write a loop that prints the last entry from July 2017 (2017-07) in every seasonal file. It should produce a similar output to:

    grep 2017-07 seasonal/winter.csv | tail -n 1

but for each seasonal file separately. Please use file as the name of the loop variable, and remember to loop through the list of files seasonal/*.csv (instead of 'seasonal/winter.csv' as in the example).

Solution :

# Run the following command
for file in seasonal/*.csv; do grep 2017-07 $file | tail -n 1; done

'''
