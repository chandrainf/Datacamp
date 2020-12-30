'''
Uploading model results to the cloud


You are working as a data scientist on building part of your machine learning cloud infrastructure. Your team has many machine learning experiments running all the time. When an experiment is finished, it will output the results file and a configuration file into a folder called output_dir/.

These results need to be uploaded to your cloud storage environment for analysis. Your task is to write a Bash script that contains a function which will loop through all the files in output_dir/ and upload the result files to your cloud storage.

For technical reasons, no files will be uploaded; we will simply echo out the file name. Though you could easily replace this section with code to upload to Amazon S3, Google Cloud or Microsoft Azure!

Instructions
100XP

- Set up a function using the 'function-word' method called upload_to_cloud.
- Use a FOR statement to loop through (using glob expansion) files whose names contain results in output_dir/ and echo that the filename is being uploaded to the cloud.
- Call the function just below the function definition using its name.

'''
# Create function
function upload_to_cloud() {
    # Loop through files with glob expansion
    for file in output_dir/*results *
    do
    # Echo that they are being uploaded
    echo "Uploading $file to cloud"
    done
}

# Call the function
upload_to_cloud
