'''
Spark UI storage tab


A folder sherlock_parts exists on disk containing twelve text files.

    ls sherlock_parts
    sherlock_part0.txt   sherlock_part2.txt   sherlock_part7.txt
    sherlock_part1.txt   sherlock_part3.txt   sherlock_part8.txt
    sherlock_part10.txt  sherlock_part4.txt   sherlock_part9.txt
    sherlock_part11.txt  sherlock_part5.txt
    sherlock_part12.txt  sherlock_part6.txt

When loaded, this creates a dataframe having seven partitions.

    partitioned_df = sqlContext.read.text('sherlock_parts')
    partitioned_df.rdd.getNumPartitions()
    7

A table is created, and the table is cached:

    partitioned_df.createOrReplaceTempView('text')
    spark.catalog.cacheTable('text')

Question: What will appear in the Spark UI Storage tab once the cache operation is triggered by an action?

Answer the question
50XP

Possible Answers

    - RDDs (Spark UI Storage 1)

    - RDDs (Spark UI Storage 2)

    - RDDs (Spark UI Storage 3)

    - RDDs (Spark UI Storage 4)

Answer : RDDs (Spark UI Storage 4)

'''
