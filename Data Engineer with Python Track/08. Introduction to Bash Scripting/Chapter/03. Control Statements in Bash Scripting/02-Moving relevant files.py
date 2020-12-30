'''
Moving relevant files


You have recently joined a new startup as one of the few technical employees. Your manager has asked if you can assist to clean up some of the folders on the server. The company has been through a variety of server monitoring software and so there are many files that should be deleted.

Luckily you know that all the files to keep contain both vpt and SRVM_ inside the file somewhere.

Your task is to write a Bash script that will take in file names as ARGV elements and move the file to good_logs/ if it matches both conditions above. Remember from the lecture, the q flag is for 'quiet' so it doesn't return the matched lines like grep normally does. It just returns true if any lines match.

You must remember to run your script using each file as an ARGV element. One each time; a total of four times to run your script.

Instructions
100XP

- Create a variable sfile out of the first ARGV element.
-Use an IF statement and grep to check if the first ARGV element contains SRVM_ AND vpt inside.
- Inside the IF statement, move matching files to the good_logs/ directory.
- Try your script on all of the files in the directory (that is, run it four times - once for each file). It should move only one of them.

'''
# Create variable from first ARGV element
sfile =$1

# Create an IF statement on first ARGV element's contents
if grep - q 'SRVM_' $sfile & & grep - q 'vpt' $sfile; then
	# Move file if matched
	mv $sfile good_logs/
fi


'''
# Run following in command

bash script.sh log1.txt
bash script.sh logdays.txt
bash script.sh logfiles8.txt
