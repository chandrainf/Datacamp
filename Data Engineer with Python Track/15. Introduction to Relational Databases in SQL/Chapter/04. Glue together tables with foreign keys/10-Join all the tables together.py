'''
Join all the tables together


In this last exercise, you will find the university city of the professor with the most affiliations in the sector "Media & communication".

For this, you need to join all the tables, group by a column, and then use selection criteria to get only the rows in the correct sector.

Instructions 1/3
35 XP

Join all tables in the database (starting with affiliations, professors, organizations, and universities) and look at the result.

'''
-- Join all tables
SELECT *
FROM affiliations
JOIN professors
ON affiliations.professor_id = professors.id
JOIN organizations
ON affiliations.organization_id = organizations.id
JOIN universities
ON professors.university_id = universities.id

'''
Instructions 2/3
35 XP

-Now group the result by organization sector, professor, and university city.
-Count the resulting number of rows.


'''
-- Group the table by organization sector, professor and university city
SELECT COUNT(*), organizations.organization_sector,
professors.id, universities.university_city
FROM affiliations
JOIN professors
ON affiliations.professor_id = professors.id
JOIN organizations
ON affiliations.organization_id = organizations.id
JOIN universities
ON professors.university_id = universities.id
GROUP BY organizations.organization_sector,
professors.id, universities.university_city

'''
Instructions 3/3
30 XP

Only retain rows with "Media & communication" as organization sector, and sort the table by count, in descending order.

'''
-- Filter the table and sort it
SELECT COUNT(*), organizations.organization_sector,
professors.id, universities.university_city
FROM affiliations
JOIN professors
ON affiliations.professor_id = professors.id
JOIN organizations
ON affiliations.organization_id = organizations.id
JOIN universities
ON professors.university_id = universities.id
WHERE organizations.organization_sector = 'Media & communication'
GROUP BY organizations.organization_sector,
professors.id, universities.university_city
ORDER BY count DESC
