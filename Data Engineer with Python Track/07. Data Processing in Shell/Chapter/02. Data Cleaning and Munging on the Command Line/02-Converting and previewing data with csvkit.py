'''
Converting and previewing data with csvkit


csvkit is written to process only CSV files. Therefore, the first thing we do is to convert our raw data file into CSV format.

After conversion, it's good practice to take a quick peak into the content of the file for a quick sanity check.

Instructions 1/3
35 XP

-Use Linux's built in unzip tool to unpack the zipped file SpotifyData.zip.

'''
# Use ls to find the name of the zipped file
ls

# Use Linux's built in unzip tool to unpack the zipped file
unzip SpotifyData.zip

# Check to confirm name and location of unzipped file
ls


'''
Instructions 2/3
35 XP

-Convert the unzipped Excel file SpotifyData.xslx to csv and name this new file SpotifyData.csv. There is only one sheet (tab) in this file, so there's no need to worry about sheet specifications.

'''
# Convert SpotifyData.xlsx to csv
in2csv SpotifyData.xlsx > SpotifyData.csv


'''
Instructions 3/3
30 XP

-Print a preview of the newly converted csv file in console using a command that is part of the csvkit suite.

'''
# Print a preview in console using a csvkit suite command
csvlook SpotifyData.csv
