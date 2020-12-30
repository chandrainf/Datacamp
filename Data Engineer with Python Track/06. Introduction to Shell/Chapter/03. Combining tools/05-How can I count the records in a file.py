'''
How can I count the records in a file?


The command wc (short for "word count") prints the number of characters, words, and lines in a file. You can make it print only one of these using -c, -w, or -l respectively.

Instructions
100 XP

Count how many records in seasonal/spring.csv have dates in July 2017 (2017-07).

- To do this, use grep with a partial date to select the lines and pipe this result into wc with an appropriate flag to count the lines.

Solution :

# Run the following command
grep 2017-07 seasonal/spring.csv | wc -l

'''
