'''
Applying SQL to a local CSV file


Sometimes the data manipulation we want to do is just easier to do with SQL. In this situation, we want to find the shortest duration song in Spotify_MusicAttributes.csv by applying the SQL below directly to the data file.

    SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1

Let's go through this step by step.

Instructions 1/3
35 XP

Complete the command to apply the SQL query to Spotify_MusicAttributes.csv.

'''
# Preview CSV file
ls

# Apply SQL query to Spotify_MusicAttributes.csv
csvsql - -query "SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1" Spotify_MusicAttributes.csv


'''
Instructions 2/3
35 XP

-Further improve the output by piping the output to csvlook.

'''
# Reformat the output using csvlook
csvsql - -query "SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1" \
    Spotify_MusicAttributes.csv | csvlook


'''
Instructions 3/3
30 XP

-Instead of printing to console, re-direct output and save as new file: LongestSong.csv.

'''
# Re-direct output to new file: LongestSong.csv
csvsql - -query "SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1" \
    Spotify_MusicAttributes.csv > LongestSong.csv

# Preview newly created file
csvlook LongestSong.csv
