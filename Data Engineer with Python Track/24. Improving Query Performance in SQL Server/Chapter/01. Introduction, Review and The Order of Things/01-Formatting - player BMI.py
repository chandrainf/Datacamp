'''
Formatting - player BMI


In this exercise, you are working with a team on a data analytics project, which has been asked to provide some statistics on NBA players to a health care company. You want to create a query that returns the Body Mass Index (BMI) for each player from North America.

        BMI = weight(kg) /height(cm)2

A colleague has passed you a query he was working on:

        select PlayerName, Country,
        round(Weight_kg/SQUARE(Height_cm/100),2) BMI 
        from Players Where Country = 'USA' 
        Or Country = 'Canada'
        order by BMI
        
To make some sense of the code, you want to structure and format it in a way that is consistent and easy to read.

Instructions
100 XP

- Change all SQL syntax (clauses, operators, and functions) to UPPERCASE.
- Make sure all SQL syntax begins on a new line.
- Add an indent to the calculated BMI column and OR statement.

'''
SELECT  PlayerName, Country, round(Weight_kg/SQUARE(Height_cm/100), 2) AS BMI
FROM Players
WHERE Country = 'USA' OR Country = 'Canada'
ORDER BY BMI
