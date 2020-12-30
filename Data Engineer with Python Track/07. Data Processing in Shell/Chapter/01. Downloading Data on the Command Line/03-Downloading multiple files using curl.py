'''
Downloading multiple files using curl


We have 100 data files stored in long sequentially named URLs. Scroll right to see the complete URLs.

    https://s3.amazonaws.com/assets.datacamp.com/production/repositories/4180/datasets/files/datafile001.txt
    https://s3.amazonaws.com/assets.datacamp.com/production/repositories/4180/datasets/files/datafile002.txt
    ......
    https://s3.amazonaws.com/assets.datacamp.com/production/repositories/4180/datasets/files/datafile100.txt

To minimize having to type the long URLs over and over again, we'd like to download all of these files using a single curl command.

Instructions
100 XP

- Download all 100 data files using a single curl command.
- Print all downloaded files to directory.

'''
# Download all 100 data files
curl - O https: // s3.amazonaws.com/assets.datacamp.com/production/repositories/4180/datasets/files/datafile[001-100].txt

# Print all downloaded files to directory
ls datafile*.txt
