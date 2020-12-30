'''
Repartitioning the data


A dataframe text_df exists, having columns id, word, and chapter. The first 5 rows of text_df are printed to the console.

You can determine that there are 12 chapters by the following:

       text_df.select('chapter')\
              .distinct()\
              .sort('chapter')\
              .show(truncate=False)

The result of this command is printed to the console as Table 1.

The dataframe text_df is currently in a single partition. Suppose that you know that the upcoming processing steps are going to be grouping the data on chapters. Processing the data will be most efficient if each chapter stays within a single machine. To avoid unnecessary shuffling of the data from one machine to another, let's repartition the dataframe into one partition per chapter, using the repartition and getNumPartitions commands taught in the first video lesson to this chapter.

Don't hesitate to refer to the slides available at the right of the console if you forget how something was done in the video.

Instructions
100 XP

- Repartition the text_df into 12 partitions, with each chapter in its own partition.
- Display the number of partitions in the new dataframe.

'''
# Repartition text_df into 12 partitions on 'chapter' column
repart_df = text_df.repartition(12, "chapter")

# Prove that repart_df has 12 partitions
repart_df.rdd.getNumPartitions()
