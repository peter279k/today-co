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
    if result.status_code == 200:
        print('OK')
    elif result.status_code == 201:
        print('Created')
    elif result.status_code == 204:
        print('No Content')
    elif result.status_code == 304:
        print('Not Modified')
    elif result.status_code == 400:
        print('Bad Request')
    elif result.status_code == 401:
        print('Unauthorized')
    elif result.status_code == 403:
        print('Forbidden')
    elif result.status_code == 404:
        print('Not Found')
    elif result.status_code == 405:
        print('Method Not Allowed')
    elif result.status_code == 429:
        print('Too Many Requests')
    elif result.status_code == 500:
        print('Internal Server Error')

def sentMail(recipients, contentText, contentHtml):
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    ConfigMap = ConfigSectionMap("MAILJET", Config)
    
    apiKey = ConfigMap['mj_apikey_public']
    apiSecret = ConfigMap['mj_apikey_private']
    fromMail = ConfigMap['from-email-address']
    
    mailTitle = 'Your email flight plan!2'
    fromName = 'TodayCo'

     
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
    
    apiKey = ConfigMap['mj_apikey_public']
    apiSecret = ConfigMap['mj_apikey_private']
    fromMail = ConfigMap['from-email-address']
    
    mailTitle = 'Your email flight plan!2'
    fromName = 'TodayCo'
    contentText = 'Dear passenger, welcome to Mailjet! May the delivery force be with you!'
    contentHtml = '<h3>Dear passenger, welcome to Mailjet!</h3><br />May the delivery force be with you!'
    recipients = list()
    
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