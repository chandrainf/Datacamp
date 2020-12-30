'''
Create a role


A database role is an entity that contains information that define the role's privileges and interact with the client authentication system. Roles allow you to give different people (and often groups of people) that interact with your data different levels of access.

Imagine you founded a startup. You are about to hire a group of data scientists. You also hired someone named Marta who needs to be able to login to your database. You're also about to hire a database administrator. In this exercise, you will create these roles.

Instructions 1/3
35 XP

Create a role called data_scientist.

'''
-- Create a data scientist role
CREATE ROLE data_scientist

'''
Instructions 2/3
35 XP

Create a role called marta that has one attribute: the ability to login (LOGIN).

'''

-- Create a role for Marta
CREATE ROLE marta WITH LOGIN

'''
Instructions 3/3
30 XP

Create a role called admin with the ability to create databases (CREATEDB) and to create roles (CREATEROLE).

'''
-- Create an admin role
CREATE ROLE admin WITH CREATEDB CREATEROLE
