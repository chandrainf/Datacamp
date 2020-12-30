'''
Ambiguous column names


When joining tables, we use aliases in the SELECT statement to indicate the source tables of the selected columns, with each column name prefixed with the table name alias.

The following query joins the Players and PlayerStats tables to return total points by PlayerName and Country for all players from Australia.

    SELECT PlayerName, p.Country,
            SUM(ps.TotalPoints) AS TotalPoints  
    FROM PlayerStats ps
    INNER JOIN Players p
    ON ps.PlayerName = p.PlayerName
    WHERE p.Country = 'Australia'
    GROUP BY p.PlayerName, p.Country

Copy and paste the query into the console and select Run Code to view the results. The query returns an error which includes the words ... Ambiguous column name...

Fix the query and run it. What was wrong with the original query?

Instructions
50 XP

Possible Answers

    - The INNER JOIN must also reference the Country column.

    - PlayerName is in both the Players and PlayerStats tables. It requires an alias prefix.

    - An alias cannot be the same name as the aggregated column, i.e. TotalPoints.

    - WHERE cannot process Australia because there are no Australians are in the NBA.

Answer : PlayerName is in both the Players and PlayerStats tables. It requires an alias prefix.

'''
