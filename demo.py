# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 17:26:00 2018

@author: u0113548
"""

import send_mail


SENDER = "dasnilakash@gmail.com"
RECIPIENT = "dasnilakash@gmail.com"
SUBJECT = "Computations done"
BODY = "Validation accuracy is ___"
AWS_REGION = "us-east-1" #US East (N. Virginia)

send_mail.send(SENDER,RECIPIENT,SUBJECT,BODY, AWS_REGION )