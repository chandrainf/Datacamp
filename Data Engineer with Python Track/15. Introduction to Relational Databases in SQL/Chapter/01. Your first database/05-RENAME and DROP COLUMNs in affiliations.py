'''
RENAME and DROP COLUMNs in affiliations


As mentioned in the video, the still empty affiliations table has some flaws. In this exercise, you'll correct them as outlined in the video.

You'll use the following queries:

    To rename columns:
    ALTER TABLE table_name
    RENAME COLUMN old_name TO new_name;
    To delete columns:
    ALTER TABLE table_name
    DROP COLUMN column_name;

Instructions 1/2
50 XP

- Rename the organisation column to organization in affiliations.

'''
-- Rename the organisation column
ALTER TABLE affiliations
RENAME COLUMN organisation TO organization

'''
Instructions 2/2
50 XP

- Delete the university_shortname column in affiliations.

'''
-- Delete the university_shortname column
ALTER TABLE affiliations
DROP COLUMN university_shortname
