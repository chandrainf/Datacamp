'''
How can I combine many commands?


You can chain any number of commands together. For example, this command:

cut -d , -f 1 seasonal/spring.csv | grep -v Date | head -n 10
will:

    1. select the first column from the spring data;
    2. remove the header line containing the word "Date"; and
    3. select the first 10 lines of actual data.

Instructions
100 XP

In the previous exercise, you used the following command to select all the tooth names from column 2 of seasonal/summer.csv:

cut -d , -f 2 seasonal/summer.csv | grep -v Tooth

Extend this pipeline with a head command to only select the very first tooth name.

Solution :

# Run the following command
cut -d , -f 2 seasonal/summer.csv | grep -v Tooth | head -n 1

'''
