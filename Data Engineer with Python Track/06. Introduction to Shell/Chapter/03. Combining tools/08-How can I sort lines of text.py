'''
How can I sort lines of text?


As its name suggests, sort puts data in order. By default it does this in ascending alphabetical order, but the flags -n and -r can be used to sort numerically and reverse the order of its output, while -b tells it to ignore leading blanks and -f tells it to fold case (i.e., be case-insensitive). Pipelines often use grep to get rid of unwanted records and then sort to put the remaining records in order.

Instructions
100 XP

Remember the combination of cut and grep to select all the tooth names from column 2 of seasonal/summer.csv?

    cut -d , -f 2 seasonal/summer.csv | grep -v Tooth

Starting from this recipe, sort the names of the teeth in seasonal/winter.csv (not summer.csv) in descending alphabetical order. To do this, extend the pipeline with a sort step.

Solution :

# Run the following command
cut -d , -f 2 seasonal/winter.csv | grep -v Tooth | sort -r

'''
