'''
Data processing with csvkit


Once we have assembled a dataset, we still need to process and clean the data prior to more advanced analysis such as predictive modeling. In this capstone exercise, let's make use of various commands in csvkit for some common data processing and cleaning.

The Excel file Spotify_201809_201810.xlsx contains two sheets (tabs), named Spotify201809 and Spotify201810. First, we will split the Excel file down to its individual sheets, preview summary statistics, remove some columns, and then stack the two sheets back together again to form one single csv file, ready for further analysis.

Instructions 1/3
35 XP

-Convert the Spotify201809 sheet into its own csv file named Spotify201809.csv.

'''
# Convert the Spotify201809 sheet into its own csv file
in2csv Spotify_201809_201810.xlsx - -sheet "Spotify201809" > Spotify201809.csv

# Check to confirm name and location of data file
ls


'''
Instructions 2/3
35 XP

-Familiarize ourselves with the column names by printing a preview of the file using a function in csvkit.
-Find the column names for song track and popularity rank. Create a new CSV containing only these 2 columns.

'''
# Convert the Spotify201809 tab into its own csv file
in2csv Spotify_201809_201810.xlsx - -sheet "Spotify201809" > Spotify201809.csv

# Check to confirm name and location of data file
ls

# Preview file preview using a csvkit function
csvlook Spotify201809.csv

# Create a new csv with 2 columns: track_id and popularity
csvcut - c "track_id", "popularity" Spotify201809.csv > Spotify201809_subset.csv


'''
Instructions 3/3
30 XP

-Stack Spotify201809_subset.csv and Spotify201810_subset.csv together to form 1 csv file and create a new column with either Sep2018 or Oct2018, depending on original file source. Leave the name of the new column to its default group.

'''
# Convert the Spotify201809 tab into its own csv file
in2csv Spotify_201809_201810.xlsx - -sheet "Spotify201809" > Spotify201809.csv

# Check to confirm name and location of data file
ls

# Preview file preview using a csvkit function
csvlook Spotify201809.csv

# Create a new csv with 2 columns: track_id and popularity
csvcut - c "track_id", "popularity" Spotify201809.csv > Spotify201809_subset.csv

# While stacking the 2 files, create a data source column
csvstack - g "Sep2018", "Oct2018" Spotify201809_subset.csv Spotify201810_subset.csv > Spotify_all_rankings.csv
