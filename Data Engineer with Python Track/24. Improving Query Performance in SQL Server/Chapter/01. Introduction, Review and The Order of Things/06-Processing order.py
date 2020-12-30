'''
Processing order


The following query returns earthquakes with a magnitude higher than 8, and at a depth of more than 500km.

    SELECT Date, Country, Place, Depth, Magnitude
    FROM Earthquakes
    WHERE Magnitude > 8
        AND Depth > 500
    ORDER BY Depth DESC;
    
Copy and paste the query into the console and select Run Code to view the results.

In which order is the SQL syntax processed in this query?

Instructions
50 XP

Possible Answers

    -SELECT, FROM, WHERE, ORDER BY

    -FROM, WHERE, SELECT, AND

    -WHERE, FROM, SELECT, ORDER BY

    -FROM, WHERE, SELECT, ORDER BY

Answer : FROM, WHERE, SELECT, ORDER BY

'''
