'''
Filtering data by row with csvkit


Now it's time get some hands-on practice for filtering data by exact row values using -m. Whether it's text or numeric, csvgrep can help us filter by these values.

Instructions 1/2
50 XP

- Filter Spotify_MusicAttributes.csv and return the row or rows where track_id equals118GQ70Sp6pMqn6w1oKuki.

'''
# Print a list of column headers in the data
csvcut - n Spotify_MusicAttributes.csv

# Filter for row(s) where track_id = 118GQ70Sp6pMqn6w1oKuki
csvgrep - c "track_id" - m 118GQ70Sp6pMqn6w1oKuki Spotify_MusicAttributes.csv


'''
Instructions 2/2
50 XP

-Filter Spotify_MusicAttributes.csv and return the row or rows where danceability equals 0.812.

'''
# Print a list of column headers in the data
csvcut - n Spotify_MusicAttributes.csv

# Filter for row(s) where danceability = 0.812
csvgrep - c "danceability" - m 0.812 Spotify_MusicAttributes.csv
