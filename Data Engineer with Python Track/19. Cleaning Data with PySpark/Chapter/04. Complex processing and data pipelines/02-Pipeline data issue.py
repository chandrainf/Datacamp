'''
Pipeline data issue


After creating your quick pipeline, you provide the json file to an analyst on your team. After loading the data and performing a couple exploratory tasks, the analyst tells you there's a problem in the dataset while trying to sort the duration data. She's not sure what the issue is beyond the sorting operation not working as expected.

Date          Flight Number   Airport     Duration    ID

09/30/2015    2287            ANC         409         107962
12/28/2015    1408            OKC         41          141917
08/11/2015    2287            ANC         410         87978

After analyzing the data, which command would fix the issue?

Answer the question
50XP

Possible Answers

    - departures_df = departures_df.orderBy(departures_df.Airport)

    - departures_df = departures_df.withColumn('Duration', departures_df['Duration'].cast(IntegerType()))

    - departures_df = departures_df.orderBy(departures_df['Duration'])

    - departures_df = departures_df.select(departures_df['Duration']).cast(LongType())

Answer : departures_df = departures_df.withColumn('Duration', departures_df['Duration'].cast(IntegerType()))

'''
