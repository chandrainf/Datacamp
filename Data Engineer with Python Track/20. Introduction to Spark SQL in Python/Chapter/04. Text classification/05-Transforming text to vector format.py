'''
Transforming text to vector format


You learned how to split sentences and transform an array of words into a numerical vector using a CountVectorizer.

A dataframe df is provided having the following columns: sentence, in, and out. Each column is an array of strings. sentence is a list of words representing a sentence from a text book. The out column gives the last word of sentence. The in column is obtained by removing the last word from sentence.

The CountVectorizer model expects a dataframe having a column words and creates a column vec.

You will first perform a transform that adds an invec column, which looks like the following:

    +----------------------+-------+------------------------------------+
    |in                    |out    |invec                               |
    +----------------------+-------+------------------------------------+
    |[then, how, many, are]|[there]|(126,[3,18,28,30],[1.0,1.0,1.0,1.0])|
    |[how]                 |[many] |(126,[28],[1.0])                    |
    |[i, donot]            |[know] |(126,[15,78],[1.0,1.0])             |
    +----------------------+-------+------------------------------------+

    only showing top 3 rows

Then you will perform a second transform, which looks like the following:

    +------------------------------------+----------------+
    |invec                               |outvec          |
    +------------------------------------+----------------+
    |(126,[3,18,28,30],[1.0,1.0,1.0,1.0])|(126,[11],[1.0])|
    |(126,[28],[1.0])                    |(126,[18],[1.0])|
    |(126,[15,78],[1.0,1.0])             |(126,[21],[1.0])|
    +------------------------------------+----------------+

    only showing top 3 rows

Instructions
100 XP

- Create a dataframe called result by using model to transform() df. result has the columns sentence, in, out, and invec. invec is the vector transformation of the in column.
- Add a column to result called outvec. result now has the columns sentence, in, out, invec, and outvec.

'''
# Transform df using model
result = model.transform(df.withColumnRenamed('in', 'words'))\
    .withColumnRenamed('words', 'in')\
    .withColumnRenamed('vec', 'invec')
result.drop('sentence').show(3, False)

# Add a column based on the out column called outvec
result = model.transform(result.withColumnRenamed('out', 'words'))\
    .withColumnRenamed('words', 'out')\
    .withColumnRenamed('vec', 'outvec')
result.select('invec', 'outvec').show(3, False)
