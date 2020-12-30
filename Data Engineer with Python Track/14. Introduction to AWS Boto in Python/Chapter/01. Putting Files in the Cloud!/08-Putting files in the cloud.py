'''
Putting files in the cloud


Now that Sam knows how to create buckets, she is ready to automate a tedious part of her job. Right now, she has to download the latest files from the City of San Diego Open Data Portal, aggregate them, and share them with management.

Sharing an analysis with others is a common, yet tedious data science task. Automating these steps will allow Sam to focus on cooler projects, while keeping her management happy.

In the last lesson, Sam has already created the gid-staging bucket. She has already downloaded the files from the URLs, analyzed them, and wrote the results to final_report.csv.

She has also already initialized the boto3 S3 client and assigned it to the s3 variable.

Help Sam upload final_report.csv to the gid-staging bucket!

Instructions
100 XP

- Upload 'final_report.csv' to the 'gid-staging' bucket with the key '2019/final_report_01_01.csv'.
- Get the object metadata and store it in response.
- Print the object size in bytes.

'''
# Upload final_report.csv to gid-staging
s3.upload_file(Bucket='gid-staging',
               # Set filename and key
               Filename='final_report.csv',
               Key='2019/final_report_01_01.csv')

# Get object metadata and print it
response = s3.head_object(Bucket='gid-staging',
                          Key='2019/final_report_01_01.csv')

# Print the size of the uploaded object
print(response['ContentLength'])
