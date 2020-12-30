'''
Granting and revoking access


Access control is a key aspect of database management. Not all database users have the same needs and goals, from analysts, clerks, data scientists, to data engineers. As a general rule of thumb, write access should never be the default and only be given when necessary.

In the case of our Pitchfork reviews, we don't want all database users to be able to write into the long_reviews view. Instead, the editor should be the only user able to edit this view.

Instructions
100 XP

- Revoke all database users' update and insert privileges on the long_reviews view.
- Grant the editor user update and insert privileges on the long_reviews view.

'''
-- Revoke everyone's update and insert privileges
REVOKE UPDATE, INSERT ON long_reviews FROM PUBLIC

-- Grant the editor update and insert privileges
GRANT UPDATE, INSERT ON long_reviews TO editor
