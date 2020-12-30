'''
REFERENCE a table with a FOREIGN KEY


In your database, you want the professors table to reference the universities table. You can do that by specifying a column in professors table that references a column in the universities table.

As just shown in the video, the syntax for that looks like this:

ALTER TABLE a 
ADD CONSTRAINT a_fkey FOREIGN KEY (b_id) REFERENCES b (id);
Table a should now refer to table b, via b_id, which points to id. a_fkey is, as usual, a constraint name you can choose on your own.

Pay attention to the naming convention employed here: Usually, a foreign key referencing another primary key with name id is named x_id, where x is the name of the referencing table in the singular form.

Instructions 1/2
50 XP

Rename the university_shortname column to university_id in professors.

'''
-- Rename the university_shortname column
ALTER TABLE professors
RENAME COLUMN university_shortname TO university_id


'''
Instructions 2/2
50 XP

- Add a foreign key on university_id column in professors that references the id column in universities.
- Name this foreign key professors_fkey.
'''

-- Rename the university_shortname column
ALTER TABLE professors
RENAME COLUMN university_shortname TO university_id

-- Add a foreign key on professors referencing universities
ALTER TABLE professors
ADD CONSTRAINT professors_fkey FOREIGN KEY(university_id) REFERENCES universities(id)
