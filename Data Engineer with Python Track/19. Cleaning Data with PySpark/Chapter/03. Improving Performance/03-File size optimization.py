'''
File size optimization


Consider if you're given 2 large data files on a cluster with 10 nodes. Each file contains 10M rows of roughly the same size. While working with your data, the responsiveness is acceptable but the initial read from the files takes a considerable period of time. Note that you are the only one who will use the data and it changes for each run.

Which of the following is the best option to improve performance?

Answer the question
50XP

Possible Answers

    - Split the 2 files into 8 files of 2.5M rows each.

    - Convert the files to parquet.

    - Split the 2 files into 50 files of 400K rows each.

    - Split the files into 30 files containing a random number of rows.

Answer : Split the 2 files into 50 files of 400K rows each.

'''
