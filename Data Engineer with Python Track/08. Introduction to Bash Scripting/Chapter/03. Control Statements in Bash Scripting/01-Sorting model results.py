'''
Sorting model results


You are working as a data scientist in a large corporation. The production environment for your machine learning models writes out text files into the model_results/ folder whenever an experiment is completed. The files have the following structure (example):

    Model Name: KNN
    Accuracy: 89
    F1: 0.87
    Date: 2019-12-01
    ModelID: 34598utjfddfgdg

You can see the model name, accuracy and F1 scores, the date the experiment completed and a unique ID to link the model experiment back into your experiment system.

The company has a threshold of 90% for accuracy for a model to continue experimentation. Your task is to write a Bash script that takes in an ARGV argument (a filename), extracts the accuracy score and conditionally sorts the model result file into one of two folders: good_models/ for those with accuracy greater than or equal to 90 and bad_models/ for those less than 90. You must run your script from the terminal with the requested arguments before submitting your answer.

NOTE!! If you don't run the script with an argument, it will hang - so make sure to run the script with the requested argument! If you make an error requiring a hint - you may need to refresh the session before submitting as well!

Instructions
100XP

- Create a variable, accuracy by extracting the "Accuracy" line (and "Accuracy" value) in the first ARGV element (a file).
- Create an IF statement to move the file into good_models/ folder if it is greater than or equal to 90 using a flag, not a mathematical sign.
- Create an IF statement to move the file into bad_models/ folder if it is less than 90 using a flag, not a mathematical sign.
- Run your script from the terminal pane twice (using bash script.sh). Once with model_results/model_1.txt, then once with model_results/model_2.txt as the only argument.

'''
# Extract Accuracy from first ARGV element
accuracy =$(grep Accuracy $1 | sed 's/.* //')

# Conditionally move into good_models folder
if [$accuracy - ge 90]
then
mv $1 good_models/
fi

# Conditionally move into bad_models folder
if [$accuracy - lt 90]
then
mv $1 bad_models/
fi


'''
# Run following in command
bash script.sh model_results/model_1.txt
bash script.sh model_results/model_2.txt

'''
