'''
Moving model results with CASE


You are working as a data scientist in charge of analyzing some machine learning model results. The production environment moves files into a folder called model_out/ and names them model_RXX.csv where XX is a random number related to which experiment was run.

Each file has the following structure (example):

Model Name, Accuracy, CV, Model Duration (s)
Logistic,42,4,48
Your manager has told you that recent work in the organization has meant that tree-based models are to be kept in one folder and everything else deleted.

Your task is to use a CASE statement to move the tree-based models (Random Forest, GBM, and XGBoost) to the tree_models/ folder, and delete all other models (KNN and Logistic).

Instructions
100XP

- Use a FOR statement to loop through (using glob expansion) files in model_out/.
- Use a CASE statement to match on the contents of the file (we will use cat and shell-within-a-shell to get the contents to match against). It must check if the text contains a tree-based model name and move to tree_models/, otherwise delete the file.
- Create a default match that prints out Unknown model in FILE where FILE is the filename then run your script.

'''
# Use a FOR loop for each file in 'model_out'
for file in model_out/*
do
    # Create a CASE statement for each file's contents
    case $(cat $file) in
      # Match on tree and non-tree models
      *"Random Forest"*|*GBM*|*XGBoost*)
      mv $file tree_models / ; ;
      *KNN*|*Logistic*)
      rm $file; ;
      # Create a default
      *)
      echo "Unknown model in $file"; ;
    esac
done


'''
# Run following in command

bash script.sh model_R371.csv

'''
