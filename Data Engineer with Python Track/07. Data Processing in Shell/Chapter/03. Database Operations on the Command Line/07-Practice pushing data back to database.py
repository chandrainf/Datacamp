'''
Practice pushing data back to database


It is also possible to go the other way around and push local CSV files back to the database. As long as we specify the database as well as the CSV file to be loaded, csvsql does the rest of the work for us (e.g. inferring table schema), behind the scenes.

In the following exercise, complete the command to upload Spotify_MusicAttributes.csv as its own table in the SQLite database SpotifyDatabase. Then, as a sanity check, re-pull the data from the newly created table in the database.

Instructions
100 XP

- Upload Spotify_MusicAttributes.csv as its own table in the SQLite database SpotifyDatabase.
- Re-pull the data from the newly created table Spotify_MusicAttributes in the SQLite database SpotifyDatabase.

'''
# Preview file
ls

# Upload Spotify_MusicAttributes.csv to database
csvsql - -db "sqlite:///SpotifyDatabase.db" - -insert Spotify_MusicAttributes.csv

# Store SQL query as shell variable
sqlquery = "SELECT * FROM Spotify_MusicAttributes"

# Apply SQL query to re-pull new table in database
sql2csv - -db "sqlite:///SpotifyDatabase.db" - -query "$sqlquery"
