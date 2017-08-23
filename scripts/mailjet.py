#!/usr/bin/env python
# coding=utf-8
"""
This call sends an email to one recipient, using a validated sender address
Do not forget to update the sender address used in the sample
"""

from mailjet_rest import Client
import configparser

def ConfigSectionMap(section, Config):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

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

def sent_mail():
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    ConfigMap = ConfigSectionMap("MAILJET", Config)
    
    api_key = ConfigMap['mj_apikey_public']
    api_secret = ConfigMap['mj_apikey_private']
    from_mail = ConfigMap['from-email-address']
    
    mail_title = 'Your email flight plan!2'
    from_name = 'TodayCo'
    content_text = 'Dear passenger, welcome to Mailjet! May the delivery force be with you!'
    content_html = '<h3>Dear passenger, welcome to Mailjet!</h3><br />May the delivery force be with you!'
    recipients = list()
    
    recipients.append({"Email": "youmu257@gmail.com"})
    recipients.append({"Email": "ragnro_456@yahoo.com.tw"})
    
                    
    print(api_key)
    print(api_secret)
    print(from_mail)
    print(recipients)
     
    mailjet_test = Client(auth=(api_key, api_secret))
    data = {
      'FromEmail': from_mail,
      'FromName': from_name,
      'Subject': mail_title,
      'Text-part': content_text,
      'Html-part': content_html,
      'Recipients': recipients
    }
     
    result = mailjet_test.send.create(data=data)
    CheckStatusCode(result)


