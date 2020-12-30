'''
Add a user role to a group role


There are two types of roles: user roles and group roles. By assigning a user role to a group role, a database administrator can add complicated levels of access to their databases with one simple command.

For your startup, your search for data scientist hires is taking longer than expected. Fortunately, it turns out that Marta, your recent hire, has previous data science experience and she's willing to chip in the interim. In this exercise, you'll add Marta's user role to the data scientist group role. You'll then remove her after you complete your hiring process.

Instructions
100 XP

- Add Marta's user role to the data scientist group role.
- Celebrate! You hired multiple data scientists.
- Remove Marta's user role from the data scientist group role.

'''

-- Add Marta to the data scientist group
GRANT data_scientist TO marta

-- Celebrate! You hired data scientists.

-- Remove Marta from the data scientist group
REVOKE data_scientist FROM marta
