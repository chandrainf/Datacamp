'''
Printing column headers with csvkit


There are many ways to preview the data within csvkit alone(e.g. csvlook, csvstat, etc). However, if all we want is to find the position and name of the columns in our data, it is easier to simply print a string of column headers. Let's print the column headers for the data file Spotify_MusicAttributes.csv.

Instructions
100 XP

- Print in console a list of column headers in the data file Spotify_MusicAttributes.csv using a csvkit command.

'''

# Check to confirm name and location of data file
ls

# Print a list of column headers in data file
csvcut - n Spotify_MusicAttributes.csv
