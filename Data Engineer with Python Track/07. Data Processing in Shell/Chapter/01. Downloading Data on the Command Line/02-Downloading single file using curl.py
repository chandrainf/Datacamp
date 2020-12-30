'''
Downloading single file using curl


Let's get some hands on practice for the more commonly used options and flags with curl. The URL for the hosted file is a shortened URL using tinyurl. Because of that, we need to fill out a flag option that allows for redirected URLs.

Instructions 1/2
50 XP

Fill in the option flag that allow downloading from a redirected URL.

'''
# Use curl to download the file from the redirected URL
curl - L https: // assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip


'''
Instructions 2/2
50 XP

In the same step as the download, add in the necessary syntax to rename the downloaded file as Spotify201812.zip.

'''
# Download and rename the file in the same step
curl - o Spotify201812.zip - L https: // assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip
