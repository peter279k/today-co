#!/usr/bin/env python
# coding=utf-8
"""
This call sends an email to one recipient, using a validated sender address
Do not forget to update the sender address used in the sample
"""

from mailjet_rest import Client
import configparser
from util import ConfigSectionMap

## print the success or failure of your calls.
def CheckStatusCode(result):
    statusCode = result.status_code
    statusCodeDict = {
        200: 'ok',
        201: 'Created',
        204: 'No Content',
        304: 'Not Modified',
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed',
        429: 'Too Many Requests',
        500: 'Internal Server Error'
    }
    
    if statusCode in statusCodeDict:
        print(statusCodeDict[statusCode])
    else:
        print('Unknown status code message')

def sentMail(recipients, contentText, contentHtml):
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    ConfigMap = ConfigSectionMap("MAILJET", Config)
    
    apiKey    = ConfigMap['mj_apikey_public']
    apiSecret = ConfigMap['mj_apikey_private']
    fromMail  = ConfigMap['from-email-address']
    
    mailTitle = 'Your email flight plan!2'
    fromName  = 'TodayCo'

     
    mailjet_test = Client(auth=(apiKey, apiSecret))
    data = {
      'FromEmail': fromMail,
      'FromName': fromName,
      'Subject': mailTitle,
      'Text-part': contentText,
      'Html-part': contentHtml,
      'Recipients': recipients
    }
     
    result = mailjet_test.send.create(data=data)
    CheckStatusCode(result)

def sentMailTest():
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    ConfigMap = ConfigSectionMap("MAILJET", Config)
    
    apiKey    = ConfigMap['mj_apikey_public']
    apiSecret = ConfigMap['mj_apikey_private']
    fromMail  = ConfigMap['from-email-address']
    
    mailTitle   = 'Your email flight plan!2'
    fromName    = 'TodayCo'
    contentText = 'Dear passenger, welcome to Mailjet! May the delivery force be with you!'
    contentHtml = '<h3>Dear passenger, welcome to Mailjet!</h3><br />May the delivery force be with you!'
    recipients  = list()
    
    recipients.append({"Email": "youmu257@gmail.com"})
    
                    
    print(apiKey)
    print(apiSecret)
    print(fromMail)
    print(recipients)
     
    mailjet_test = Client(auth=(apiKey, apiSecret))
    data = {
      'FromEmail': fromMail,
      'FromName': fromName,
      'Subject': mailTitle,
      'Text-part': contentText,
      'Html-part': contentHtml,
      'Recipients': recipients
    }
     
    result = mailjet_test.send.create(data=data)
    CheckStatusCode(result)


recipients = list()
recipients.append({"Email": "youmu257@gmail.com"})
contentText = 'Dear passenger, welcome to Mailjet! May the delivery force be with you!'
contentHtml = '<h3>Dear passenger, welcome to Mailjet!</h3><br />May the delivery force be with you!'
#sentMail(recipients, contentText, contentHtml)
sentMailTest()