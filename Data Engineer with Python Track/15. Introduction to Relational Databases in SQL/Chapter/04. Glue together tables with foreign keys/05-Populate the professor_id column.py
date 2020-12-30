'''
Populate the "professor_id" column


Now it's time to also populate professors_id. You'll take the ID directly from professors.

Here's a way to update columns of a table based on values in another table:

    UPDATE table_a
    SET column_to_update = table_b.column_to_update_from
    FROM table_b
    WHERE condition1 AND condition2 AND ...;
    
This query does the following:

For each row in table_a, find the corresponding row in table_b where condition1, condition2, etc., are met.
Set the value of column_to_update to the value of column_to_update_from (from that corresponding row).
The conditions usually compare other columns of both tables, e.g. table_a.some_column = table_b.some_column. Of course, this query only makes sense if there is only one matching row in table_b.

Instructions 1/3
35 XP

First, have a look at the current state of affiliations by fetching 10 rows and all columns.

'''
-- Have a look at the 10 first rows of affiliations
SELECT *
FROM affiliations
LIMIT 10

'''
Instructions 2/3
35 XP

Update the professor_id column with the corresponding value of the id column in professors.
"Corresponding" means rows in professors where the firstname and lastname are identical to the ones in affiliations.

'''

-- Update professor_id to professors.id where firstname, lastname correspond to rows in professors
UPDATE affiliations
SET professor_id = professors.id
FROM professors
WHERE affiliations.firstname = professors.firstname AND affiliations.lastname = professors.lastname

'''
Instructions 3/3
30 XP

Check out the first 10 rows and all columns of affiliations again. Have the professor_ids been correctly matched?

'''
-- Update professor_id to professors.id where firstname, lastname correspond to rows in professors
UPDATE affiliations
SET professor_id = professors.id
FROM professors
WHERE affiliations.firstname = professors.firstname AND affiliations.lastname = professors.lastname

-- Have a look at the 10 first rows of affiliations again
SELECT *
FROM affiliations
LIMIT 10
