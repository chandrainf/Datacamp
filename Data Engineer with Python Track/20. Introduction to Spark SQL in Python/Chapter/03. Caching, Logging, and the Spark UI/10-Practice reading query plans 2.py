'''
Practice reading query plans 2


Three dataframes are available: part2_df, part3_df, and part4_df. The questions posed in this exercise can be answered by inspecting the explain() output of each dataframe.

Note that Spark tags each column name with a descriptor, delimited by a # symbol. For example, word#0, id#1L, part#2, and title#3. For the purpose of this exercise, these descriptors can be ignored.

Instructions 1/4
25 XP

Question

What file was part2_df loaded from? The full path is not wanted here, we want only the filename and its extension.
Possible Answers

    - /tmp/tmp212v0fcm/sherlock_parts.parquet

    - 'sherlock.parquet'

    - InMemoryFileIndex

    - 'sherlock_parts.parquet'

Answer : 'sherlock_parts.parquet'



Instructions 2/4
25 XP

Question

part3_df has a bug. part3_df was supposedly loaded with column part = 3. Select the integer value that is actually loaded.
Possible Answers

    - 4

    - part#10

    - part#4

    - (part,4)

Answer : 4


Instructions 3/4
25 XP

Question

What file was part4_df loaded from? The full path is not wanted here, we want only the filename and its extension.
Possible Answers

    - 'sherlock_parts.parquet'

    - file:/tmp/tmpkq34jee3/sherlock.parquet

    - 'sherlock.parquet'

    - sherlock_parts

Answer : 'sherlock.parquet'


Instructions 4/4
25 XP

Question

The ReadSchema property tells us the schema of the dataframe that was loaded. Give the value of the ReadSchema property of part4_df.
Possible Answers

    - 'word#84,id#85L'

    - /tmp/tmp07lrcp7y/sherlock.parquet

    - 'struct<word:bigint,id:string>'

    - 'struct<word:string,id:bigint>'

Answer : 'struct<word:string,id:bigint>'

'''
