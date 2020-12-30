'''
Data downloading with Wget and curl


To kick off a data analysis project, it's good practice to first consolidate all of our data into one place. Often times, this means downloading and pulling data from various locations such as HTTP servers and databases.

While curl is handy for downloading a single file, it's somewhat unwieldy for handling multiple file downloads. In this capstone exercise, we will use both curl and Wget to download a series of monthly Spotify files, do some minor processing, and consolidate all downloaded files in our local directory.

Instructions
100 XP

- Download the zipped 201812SpotifyData data saved in the shortened (redirected) URL using curl. In the same step, rename file as Spotify201812.zip.
- Unzip Spotify201812.zip, delete the original zipped file, and rename the unzipped file to Spotify201812.csv to stay consistent.
- Use url_list.txt and Wget to download all 3 files: Spotify201809.csv, Spotify201810.csv, and Spotify201811.csv in one step, with an upper cap download speed of 2500KB/s.

'''
# Use curl, download and rename a single file from URL
curl - o Spotify201812.zip - L https: // assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip

# Unzip, delete, then re-name to Spotify201812.csv
unzip Spotify201812.zip & & rm Spotify201812.zip
mv 201812SpotifyData.csv Spotify201812.csv

# View url_list.txt to verify content
cat url_list.txt

# Use Wget, limit the download rate to 2500KB/s, download all files in url_list.txt
wget - -limit-rate = 2500k - i url_list.txt

# Take a look at all files downloaded
ls
