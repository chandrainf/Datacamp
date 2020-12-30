'''
Cat detector


Sam has been getting more and more challenging projects as a result of her popularity and success.

The newest request is from the animal control team. They want to receive notifications when an image comes in from the Get It Done application contains a cat. They can find feral cats and go rescue them. They provided her with two images that she can test her system with. One contains a cat, one does not. Both images are referenced in variables image1 and image2 respectively.

Sam has also created the boto3 Rekognition client in the rekog variable.

Help Sam use Rekognition to enable the animal control team to rescue stray cats!

Instructions 1/3
35 XP

Use the Rekognition client to detect the labels for image1. Return a maximum of 1 label.

'''
# Use Rekognition client to detect labels
image1_response = rekog.detect_labels(
    # Specify the image as an S3Object; Return one label
    Image=image1, MaxLabels=1)

# Print the labels
print(image1_response['Labels'])

# Use Rekognition client to detect labels
image2_response = rekog.detect_labels(Image=image2, MaxLabels=1)

# Print the labels
print(image2_response['Labels'])

'''
Instructions 2/3
35 XP

- Detect the labels for image2 and print the response's labels..

'''
# Use Rekognition client to detect labels
image1_response = rekog.detect_labels(
    # Specify the image as an S3Object; Return one label
    Image=image1, MaxLabels=1)

# Print the labels
print(image1_response['Labels'])

# Use Rekognition client to detect labels
image2_response = rekog.detect_labels(Image=image2, MaxLabels=1)

# Print the labels
print(image2_response['Labels'])

'''
Instructions 3/3
30 XP

Question
Which image contained cats?

Possible Answers

    -image1.

    -image2.

Answer : image2 .

'''
