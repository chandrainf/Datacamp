'''
Row filtering with HAVING


In some cases, using HAVING, instead of WHERE, as a filter condition will produce the same results. If filtering individual or ungrouped rows then it is more efficient to use WHERE.

In this exercise, you want to know the number of players from Latin American countries playing in the 2017-2018 NBA season.

Instructions 1/2
50 XP

Question

Copy the following query to the console and select Run Code to view the results. Why should HAVING not be used as a filter condition in this query?

    SELECT Country, COUNT(*) CountOfPlayers 
    FROM Players
    GROUP BY Country
    HAVING Country 
        IN ('Argentina','Brazil','Dominican Republic'
            ,'Puerto Rico');

Possible Answers

    - An aggregate function must enclose the Country column in the HAVING filter.

    - The filter is on individual rows. Using HAVING here, for filtering, could increase the time a query takes to run.

    - The query returns an error because HAVING is processed before GROUP BY.

    - If a query is using HAVING for filtering it must also use WHERE.

Answer : The filter is on individual rows. Using HAVING here, for filtering, could increase the time a query takes to run.

'''


'''
Instructions 2/2
50 XP

- Add the WHERE filter condition.
- Fill in the missing two Latin American countries in the IN statement.

'''

SELECT Country, COUNT(*) CountOfPlayers
FROM Players
-- Add the filter condition
WHERE Country
-- Fill in the missing countries
IN('Argentina', 'Brazil', 'Dominican Republic', 'Puerto Rico')
GROUP BY Country
