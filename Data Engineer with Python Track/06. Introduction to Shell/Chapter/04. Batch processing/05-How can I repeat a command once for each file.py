'''
How can I repeat a command once for each file?


You can always type in the names of the files you want to process when writing the loop, but it's usually better to use wildcards. Try running this loop in the console:

for filename in seasonal/*.csv; do echo $filename; done

It prints:

    seasonal/autumn.csv
    seasonal/spring.csv
    seasonal/summer.csv
    seasonal/winter.csv

because the shell expands seasonal/*.csv to be a list of four filenames before it runs the loop.

Instructions
100 XP

Modify the wildcard expression to people/* so that the loop prints the names of the files in the people directory regardless of what suffix they do or don't have. Please use filename as the name of your loop variable.

Solution :

# Run the following command
for filename in people/*; do echo $filename; done

'''
