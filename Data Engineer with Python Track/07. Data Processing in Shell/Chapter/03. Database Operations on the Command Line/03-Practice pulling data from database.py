'''
Practice pulling data from database


With the powers of csvkit, we don't need to download and set up fancy database management software like MS SQL Server, DB2, PgAdmin, or TablePlus to be able to access the data inside a SQL database. We can pull data directly from our command line using csvkit's sql2csv command.

In this practice, let's walk through pulling data step by step, by applying SQL manipulations to the table Spotify_Popularity which dwells inside a SQLite database called SpotifyDatabase and then saving the output of the SQL query to a local .csv file Spotify_Popularity_5Rows.csv.

Instructions 1/3
35 XP

Use sql2csv to access the SQLite database SpotifyDatabase and query and print all data in the table Spotify_Popularity.

'''
# Verify database name
ls

# Pull the entire Spotify_Popularity table and print in log
sql2csv - -db "sqlite:///SpotifyDatabase.db" \
        - -query "SELECT * FROM Spotify_Popularity"


'''
Instructions 2/3
35 XP

Use a SQL query to print the first 5 rows in the table Spotify_Popularity. Then, preview the results using csvlook.

'''
# Verify database name
ls

# Query first 5 rows of Spotify_Popularity and print in log
sql2csv - -db "sqlite:///SpotifyDatabase.db" \
        - -query "SELECT * FROM Spotify_Popularity LIMIT 5" \
    | csvlook


'''
Instructions 3/3
35 XP

Save queried results to a new file Spotify_Popularity_5Rows.csv. Verify and preview the file with ls and csvlook.

'''
# Verify database name
ls

# Save query to new file Spotify_Popularity_5Rows.csv
sql2csv - -db "sqlite:///SpotifyDatabase.db" \
        - -query "SELECT * FROM Spotify_Popularity LIMIT 5" \
    > Spotify_Popularity_5Rows.csv

# Verify newly created file
ls

# Print preview of newly created file
csvlook Spotify_Popularity_5Rows.csv
