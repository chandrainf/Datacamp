'''
Filtering data by column with csvkit


Let's get some hands-on practice for filtering data column using the csvkit command csvcut. Remember that we can filter columns by referring to the position of the column (e.g. 1st column, 2nd column) or by referring to the exact name of the column as it appears in the data file.

Instructions 1/4
25 XP

- Print the first column in Spotify_MusicAttributes.csv by referring to the column by its position in the file.

'''
# Print a list of column headers in the data
csvcut - n Spotify_MusicAttributes.csv

# Print the first column, by position
csvcut - c 1 Spotify_MusicAttributes.csv


'''
Instructions 2/4
25 XP

-Print the first, third, and fifth column in Spotify_MusicAttributes.csv by referring to them by position.

'''
# Print a list of column headers in the data
csvcut - n Spotify_MusicAttributes.csv

# Print the first, third, and fifth column, by position
csvcut - c 1, 3, 5 Spotify_MusicAttributes.csv


'''
Instructions 3/4
25 XP

-Print the first column in Spotify_MusicAttributes.csv by referring to the column by its name.

'''
# Print a list of column headers in the data
csvcut - n Spotify_MusicAttributes.csv

# Print the first column, by name
csvcut - c "track_id" Spotify_MusicAttributes.csv


'''
Instructions 4/4
25 XP

-Print the first, third, and fifth column in Spotify_MusicAttributes.csv by referring to them by name.

'''
# Print a list of column headers in the data
csvcut - n Spotify_MusicAttributes.csv

# Print the track id, song duration, and loudness, by name
csvcut - c "track_id", "duration_ms", "loudness" Spotify_MusicAttributes.csv
