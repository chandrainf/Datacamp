'''
File conversion and summary statistics with csvkit


It's common for Excel data files to have more than one worksheet (tab) of data. The Excel file SpotifyData.xlsx has two sheets named Worksheet1_Popularity and Worksheet2_MusicAttributes. Each sheet should be treated like its own data file, so we will use csvkit's commands here to convert each sheet to its own CSV file. Then, using the power of the commands we already know, print a high level summary for each column in the CSV files.

Instructions 1/4
25 XP

From SpotifyData.xlsx, convert the sheet "Worksheet1_Popularity" to CSV and call it Spotify_Popularity.csv.

'''
# Check to confirm name and location of the Excel data file
ls

# Convert sheet "Worksheet1_Popularity" to CSV
in2csv SpotifyData.xlsx - -sheet "Worksheet1_Popularity" > Spotify_Popularity.csv


'''
Instructions 2/4
25 XP

Print the high level summary statistics for each column in Spotify_Popularity.csv.

'''
# Check to confirm name and location of the new CSV file
ls

# Print high level summary statistics for each column
csvstat Spotify_Popularity.csv


'''
Instructions 3/4
25 XP

-From SpotifyData.xlsx, convert the tab "Worksheet2_MusicAttributes" to CSV and call it Spotify_MusicAttributes.csv.

'''
# Check to confirm name and location of the Excel data file
ls

# Convert sheet "Worksheet2_MusicAttributes" to CSV
in2csv SpotifyData.xlsx - -sheet "Worksheet2_MusicAttributes" > Spotify_MusicAttributes.csv


'''
Instructions 4/4
25 XP

-Print a preview of Spotify_MusicAttributes.csv using a function in csvkit with Markdown-compatible, fixed-width format.

'''
# Check to confirm name and location of the new CSV file
ls

# Print preview of Spotify_MusicAttributes
csvlook Spotify_MusicAttributes.csv
