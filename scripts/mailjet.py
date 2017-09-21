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
def checkStatusCode(result):
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
        500: 'Internal Server Error',
    }

    if statusCode in statusCodeDict:
        print(statusCodeDict[statusCode])
    else:
        print('Unknown status code message')

def sendMail():
    config = configparser.ConfigParser()
    config.read("config.ini")
    configMap = ConfigSectionMap("MAILJET", config)

    apiKey = configMap['mj_apikey_public']
    apiSecret = configMap['mj_apikey_private']
    fromMail = configMap['from_email_address']

    mailTitle = 'Your email flight plan!2'
    fromName = 'TodayCo'
    contentText = 'Dear passenger, welcome to Mailjet! May the delivery force be with you!'
    contentHtml = '<h3>Dear passenger, welcome to Mailjet!</h3><br />May the delivery force be with you!'
    recipients = list()

    recipients.append({"Email": "youmu257@gmail.com"})
    recipients.append({"Email": "ragnro_456@yahoo.com.tw"})

    print(apiKey)
    print(apiSecret)
    print(fromMail)
    print(recipients)

    mailjetTest = Client(auth = (apiKey, apiSecret))
    data = {
      'FromEmail': fromMail,
      'FromName': fromName,
      'Subject': mailTitle,
      'Text-part': contentText,
      'Html-part': contentHtml,
      'Recipients': recipients
    }

recipients = list()
recipients.append({"Email": "youmu257@gmail.com"})
contentText = 'Dear passenger, welcome to Mailjet! May the delivery force be with you!'
contentHtml = '<h3>Dear passenger, welcome to Mailjet!</h3><br />May the delivery force be with you!'
#sentMail(recipients, contentText, contentHtml)
sentMailTest()
