# AWS_EC2mail
I have written this wrapper to send email notifications via Amazon EC2 instance. This original source code can be found at https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-using-sdk-python.html. This wrapper provides an easy to use API to send an email notification while using an EC2 instance. A common usecase of this wrapper include sending a notification email after a training or optimizing a deep-learning model. 

To use this wrapper, the following steps are required:
1. Go to Amazon Simple Email Service (SES) on your AWS management console
2. Select a region, preferably US East (N. Virginia)
3. Click 'Email Addresses' on the left pane menu and verify a sender's and recipent's address
4. Go back to AWS management console and navigate to IAM->Security Status->Delete your root access keys->Manage security credentials->        Access keys
5. Click 'Create New Access Key' and download the 'rootkey.csv' file. Don't change the name of the file
6. Transfer 'AWS_EC2mail.py' and 'rootkey.csv' to the appropriate directory on the EC2 instance
7. Import  'AWS_EC2mail' and use AWS_EC2mail.send() to send an email. Refer to 'demo.py' for details
