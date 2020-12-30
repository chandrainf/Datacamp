'''
Disallow NULL values with SET NOT NULL


The professors table is almost ready now. However, it still allows for NULLs to be entered. Although some information might be missing about some professors, there's certainly columns that always need to be specified.

Instructions 1/2
50 XP

- Add a not-null constraint for the firstname column.

'''

-- Disallow NULL values in firstname
ALTER TABLE professors 
ALTER COLUMN firstname SET NOT NULL;

'''
Instructions 2/2
25 XP

- Add a not-null constraint for the lastname column.
'''

-- Disallow NULL values in lastname
ALTER TABLE professors
ALTER COLUMN lastname SET NOT NULL;

