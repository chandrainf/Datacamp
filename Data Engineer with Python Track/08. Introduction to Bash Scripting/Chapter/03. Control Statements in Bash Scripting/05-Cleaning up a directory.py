'''
Cleaning up a directory


Continuing your work as a data scientist in a large organization, you were told today that a colleague has left for their dream job (lucky them!). Unfortunately, when their logins were terminated, all their files were dumped into a single folder.

The good news is that most of their useful code has been backed up. However, all their python files using the Random Forest algorithm are buried in the file dump.

The task has fallen to you to sift through the hundreds of files to determine if they are both Python files and contain a Random Forest model. This sounds like a perfect opportunity to use your Bash skills, rather than checking every single file manually.

Write a script that loops through each file in the robs_files/ directory to see if it is a Python file (ends in .py) AND contains RandomForestClassifier. If so, move it into the to_keep/ directory.

Instructions
100XP

- Use a FOR statement to loop through (using glob expansion) files that end in .py in robs_files/.
- Use an IF statement and grep (remember the 'quiet' flag?) to check if RandomForestClassifier is in the file. Don't use a shell-within-a-shell here.
- Move the Python files that contain RandomForestClassifier into the to_keep/ directory.

'''
# Create a FOR statement on files in directory
for file in robs_files/*.py
do
# Create IF statement using grep
if grep - q 'RandomForestClassifier' $file
then

# Move wanted files to to_keep/ folder
mv $file to_keep/
fi
done
