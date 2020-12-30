'''
Cleaner scripting via shell variables


Because SQL queries, by nature, can be long and complex, we will frequently need to deal with line breaks while passing in SQL queries to csvkit commands.

One way to work around this is to store the SQL queries as a shell variable, then pass in the shell variable in place of the SQL query where needed.

Instructions
100 XP

- Fill in the csvsql command by calling upon the bash variable containing the SQL query instead of writing out the SQL query in full.

'''
# Preview CSV file
ls

# Store SQL query as shell variable
sqlquery = "SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1"

# Apply SQL query to Spotify_MusicAttributes.csv
csvsql - -query "$sqlquery" Spotify_MusicAttributes.csv
