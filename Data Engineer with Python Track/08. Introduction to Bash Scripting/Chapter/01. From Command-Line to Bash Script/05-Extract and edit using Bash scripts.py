'''
Extract and edit using Bash scripts


Continuing your work for the Bulgarian soccer league - you need to do some editing on the data you have. 
Several teams have changed their names so you need to do some replacements. 
The data is the same as the previous exercise.

You will need to create a Bash script that makes use of sed to change the required team names.

Instructions
100XP

- Create a pipe using sed twice to change the team Cherno to Cherno City first, and then Arda to Arda United.
- Pipe the output to a file called soccer_scores_edited.csv.
- Save your script and run from the console. Try opening soccer_scores_edited.csv using shell commands to confirm it worked (the first line should be changed)!

'''
#!/bin/bash

# Create a sed pipe to a new file
cat soccer_scores.csv | sed 's/Cherno/Cherno City/g' | sed 's/Arda/Arda United/g' > soccer_scores_edited.csv

# Now save and run!
