'''
Running PySpark files


In this exercise, you're going to run a PySpark file using spark-submit. This tool can help you submit your application to a spark cluster.

For the sake of this exercise, you're going to work with a local Spark instance running on 4 threads. The file you need to submit is in /home/repl/spark-script.py. Feel free to read the file:

  cat /home/repl/spark-script.py

You can use spark-submit as follows:

  spark-submit \
    --master local[4] \
    /home/repl/spark-script.py

What does this output? Note that it may take a few seconds to get your results.

Instructions
50XP

Possible Answers

    - An error.
    - A DataFrame with average Olympian heights by year.
    - A DataFrame with Olympian ages.

Answer : A DataFrame with average Olympian heights by year.

'''
