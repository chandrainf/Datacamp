'''
Downloading single file using wget


Let's get some hands on practice for the option flags that make wget such a popular file downloading tool.

Instructions
100 XP

- Fill in the option flag for resuming a partial download.
- Fill in the option flag for letting the download occur in the background.
- Preview the download log file

'''
# Fill in the two option flags
wget - c - b https: // assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip

# Verify that the Spotify file has been downloaded
ls

# Preview the log file
cat wget-log
