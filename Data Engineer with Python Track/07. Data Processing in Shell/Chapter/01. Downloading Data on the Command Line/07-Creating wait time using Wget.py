'''
Creating wait time using Wget


For download smaller files, enforcing a mandatory wait time between file downloads makes sure we don't overload the server with too many requests. Here, we will using the built in option flag with wget to create a mandatory wait time (in seconds) between downloading each file stored in the URL list file.

Instructions
100 XP

Create a mandatory 1 second pause between downloading all files in url_list.txt.

'''
# View url_list.txt to verify content
cat url_list.txt

# Create a mandatory 1 second pause between downloading all files in url_list.txt
wget - -wait = 1 - i url_list.txt

# Take a look at all files downloaded
ls
