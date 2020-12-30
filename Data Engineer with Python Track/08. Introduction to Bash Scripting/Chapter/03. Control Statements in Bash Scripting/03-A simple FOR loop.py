'''
A simple FOR loop


You are working as a data scientist in an organization. Due to a recent merge of departments, you have inherited a folder with many files inside. You know that the .R scripts may be useful for your work but you aren't sure what they contain.

Write a simple Bash script to loop through all the files in the directory inherited_folder/ that end in .R and print out their names so you can get a quick look at what sort of scripts you have. Hopefully the file names are useful!

Instructions
100XP

- Use a FOR statement to loop through files that end in .R in inherited_folder/ using a glob expansion.
- echo out each file name into the console.

'''

# Use a FOR loop on files in directory
for file in inherited_folder/*.R
do
# Echo out each file
echo $file
done
