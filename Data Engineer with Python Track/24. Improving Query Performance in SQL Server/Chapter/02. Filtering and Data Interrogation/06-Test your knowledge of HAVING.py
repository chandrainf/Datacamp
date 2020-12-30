'''
Test your knowledge of HAVING


The following query from the NBA Season 2017-2018 database returns the total points contribution, of a teams Centers, where total points are greater than 2500.

    SELECT Team, 
        SUM(TotalPoints) AS TotalCPoints
    FROM PlayerStats
    WHERE Position = 'C'
    GROUP BY Team
    HAVING SUM(TotalPoints) > 2500;

Copy and paste the above query into the query console and select Run Code to check the results.

When using HAVING in a query which one of the following statements is FALSE?

Instructions
50 XP

Possible Answers

    - When filtering a numeric column, HAVING must be used with an aggregate function, for example: SUM(), COUNT(), AVG()...

    - WHERE and HAVING can be used in the same query.

    - Use HAVING with, and after, GROUP BY.

    - HAVING and WHERE produce the same output, so it doesn't matter which one you use.

Answer : HAVING and WHERE produce the same output, so it doesn't matter which one you use.

'''
