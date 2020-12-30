'''
Querying the dimensional model


Here it is! The schema reorganized using the dimensional model: 

Let's try to run a query based on this schema. How about we try to find the number of minutes we ran in July, 2019? We'll break this up in two steps. First, we'll get the total number of minutes recorded in the database. Second, we'll narrow down that query to week_id's from July, 2019.

Instructions 1/2
50 XP

Calculate the sum of the duration_mins column.

'''
SELECT
-- Select the sum of the duration of all runs
SUM(duration_mins)
FROM
runs_fact

'''
Instructions 2/2
50 XP

- Join week_dim and runs_fact.
- Get all the week_id's from July, 2019.

'''

SELECT
-- Get the total duration of all runs
SUM(duration_mins)
FROM
runs_fact
-- Get all the week_id's that are from July, 2019
INNER JOIN week_dim on week_dim.week_id = runs_fact.week_id
WHERE month = 'July' and year = '2019'
