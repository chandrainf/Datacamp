'''
Removing commented lines


Your boss would like you to perform some complex parsing on a new dataset. The data represents annotation data for the ImageNet dataset, but focusing specifically on dog breeds and identifying them in images. Before any actual analysis can occur, you'll need to clear out several components of invalid / incorrect data. The general schema of the document is unknown so you'd like to import the rows into a single column, allowing for quick analysis.

To start, you need to remove all commented rows in the dataset.

The spark context, and the base CSV file (annotations.csv.gz) are available for you to work with. The col function is also available for use.

Instructions
100 XP

- Import the annotations.csv.gz file to a DataFrame and perform a row count. Specify a separator character of |.
- Query the data for the number of rows beginning with #.
- Import the file again to a new DataFrame, but specify the comment character in the options to remove any commented rows.
- Count the new DataFrame and verify the difference is as expected.

'''
# Import the file to a DataFrame and perform a row count
annotations_df = spark.read.csv('annotations.csv.gz', sep='|')
full_count = annotations_df.count()

# Count the number of rows beginning with '#'
comment_count = annotations_df.filter(col('_c0').startswith('#')).count()

# Import the file to a new DataFrame, without commented rows
no_comments_df = spark.read.csv('annotations.csv.gz', sep='|', comment='#')

# Count the new DataFrame and verify the difference is as expected
no_comments_count = no_comments_df.count()
print("Full count: %d\nComment count: %d\nRemaining count: %d" %
      (full_count, comment_count, no_comments_count))
