# -*- coding: utf-8 -*-
"""
A wrapper to send mail via Amazon EC2.
Pre-requisites: 1. EC2 instance with any python 3.6 distribution with bot3 and botocore libraries
                2. Verified sender and receiver email ids with AES
                3. Root access keys
                
Original source: https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-using-sdk-python.html
"""

def send(SENDER, RECIPIENT, SUBJECT, BODY, AWS_REGION):
    # Inputs: 1. SENDER: the sender's verified email id with AES
    #         2. RECIPIENT: the recipient's verified email id with AES
    #         3. SUBJECT: subject of the email
    #         4. BODY: email body
    #         5. AWS_REGION: region code where AES is registered
    # Output: An email is sent
    
    # import dependencies
    import boto3
    from botocore.exceptions import ClientError
    
    # main text of the email           
    begin_tags = """<html>
               <head></head>
               <body>
               <p>"""
                  
    end_tags = """</p>
               </body>
               </html>"""
    BODY_HTML = begin_tags + BODY + end_tags
    
    # for non-html clients
    BODY_TEXT = ("") 
    
    # The character encoding for the email.
    CHARSET = "UTF-8"
    
    # Read root keys, should be in the same folder as this script
    with open("rootkey.csv") as f: 
        i = 0
        for line in f: 
            if i ==0 :
                ACCESS_KEY = line.split('=')[1]
                ACCESS_KEY = ACCESS_KEY[:-1]
            else: 
                SECRET_KEY = line.split('=')[1]
            i+=1
    
    # initiate client
    client = boto3.client('ses',
                          aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY,
                          region_name=AWS_REGION)
    
    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])