'''
Installing Python dependencies


In the following exercises, we will work through the set up process for making sure our Python environment has the proper library dependencies installed prior to executing a Python model script. In this pipeline we will create the requirements.txt file which houses the dependencies we need to install, install the dependencies, and do a quick sanity check to make sure everything is properly set up.

Instructions 1/3
35 XP

- Instantiate the requirements.txt document and add the scikit-learn library to the requirements.txt file.

'''
# Add scikit-learn to the requirements.txt file
echo "scikit-learn" > requirements.txt

# Preview file content
cat requirements.txt


'''
Instructions 2/3
35 XP

Use pip to install the dependencies in the requirements.txt file.

'''
# Add scikit-learn to the requirements.txt file
echo "scikit-learn" > requirements.txt

# Preview file content
cat requirements.txt

# Install the required dependencies
pip install - r requirements.txt


'''
Instructions 3/3
30 XP

- Use pip to list what Python libraries are already installed in your environment.

'''
# Add scikit-learn to the requirements.txt file
echo "scikit-learn" > requirements.txt

# Preview file content
cat requirements.txt

# Install the required dependencies
pip install - r requirements.txt

# Verify that Scikit-Learn is now installed
pip list
