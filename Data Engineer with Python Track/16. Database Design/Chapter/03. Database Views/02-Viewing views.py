'''
Viewing views


Because views are very useful, it's common to end up with many of them in your database. It's important to keep track of them so that database users know what is available to them.

The goal of this exercise is to get familiar with viewing views within a database and interpreting their purpose. This is a skill needed when writing database documentation or organizing views.

Instructions 1/3
35 XP

- Query the information schema to get views.
- Exclude system views in the results.

'''
SELECT * FROM INFORMATION_SCHEMA.views
WHERE table_schema NOT IN('pg_catalog', 'information_schema')


'''
Instructions 2/3
35 XP

Question :

What does view1 do?

Possible Answers

    -Returns the content records with reviewids that have been viewed more than 4000 times.

    -Returns the content records that have reviews of more than 4000 characters.

    -Returns the first 4000 records in content.

Answer : Returns the content records that have reviews of more than 4000 characters.

'''


'''
Instructions 3/3
30 XP

Question
What does view2 do?

Possible Answers

    -Returns 10 random reviews published in 2017.

    -Returns the top 10 lowest scored reviews published in 2017.

    -Returns the top 10 highest scored reviews published in 2017.

Answer : Returns the top 10 highest scored reviews published in 2017.

'''
