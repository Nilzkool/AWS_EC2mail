# A script to demonstrate the use of AWS_EC2mail

import AWS_EC2mail

# Email details
SENDER = "xyz@gmail.com" #sender's SES verified email ID
RECIPIENT = "abc@gmail.com"  #recipient's SES verified email ID
SUBJECT = "Computations done" # subject of email
BODY = "Validation accuracy is _" # main body of email
AWS_REGION = "us-east-1" #US East (N. Virginia), go to https://docs.aws.amazon.com/general/latest/gr/rande.html
                         # for a list of region code

# send mail from SENDER to RECIPIENT
AWS_EC2mail.send(SENDER,RECIPIENT,SUBJECT,BODY, AWS_REGION )
