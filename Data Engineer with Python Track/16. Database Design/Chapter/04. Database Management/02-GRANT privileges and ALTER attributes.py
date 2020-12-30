'''
GRANT privileges and ALTER attributes


Once roles are created, you grant them specific access control privileges on objects, like tables and views. Common privileges being SELECT, INSERT, UPDATE, etc.

Imagine you're a cofounder of that startup and you want all of your data scientists to be able to update and insert data in the long_reviews view. In this exercise, you will enable those soon-to-be-hired data scientists by granting their role (data_scientist) those privileges. Also, you'll give Marta's role a password.

Instructions
100 XP

- Grant the data_scientist role update and insert privileges on the long_reviews view.
- Alter Marta's role to give her the provided password.

'''
-- Grant data_scientist update and insert privileges
GRANT UPDATE, INSERT ON long_reviews TO data_scientist

-- Give Marta's role a password
ALTER ROLE marta WITH PASSWORD 's3cur3p@ssw0rd'
