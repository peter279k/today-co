#!/usr/bin/env python
# coding=utf-8
"""
This call sends an email to one recipient, using a validated sender address
Do not forget to update the sender address used in the sample
"""

from mailjet_rest import Client
import configparser
from util import configSectionMap
from Enum.subscribeType import SubscribeType
from database.mysqlConnect import *
from database.model.subscribers import *
from database.model.pornVideo import *

config = configparser.ConfigParser()
config.read("config.ini")
configMap = configSectionMap("MAILJET", config)

apiKey = configMap['mj_apikey_public']
apiSecret = configMap['mj_apikey_private']
fromMail = configMap['from_email_address']
mailTitle = configMap['mail_title']


# print the success or failure of your calls.
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


def sendMail(recipients, mailContent):
    global apiKey, apiSecret, fromMail

    mailjetTest = Client(auth=(apiKey, apiSecret))
    data = {
        'FromEmail': fromMail,
        'FromName': 'TodayCo',
        'Subject': mailTitle,
        # 'Text-part': contentText,
        'Html-part': mailContent,
        'Recipients': recipients
    }

    result = mailjetTest.send.create(data=data)
    checkStatusCode(result)


def getTopWeeklyMailContent():
    pornVideoList = getTopWeeklyPornVideos(10)
    content = 'This is weekly top 10 video list.<br>'
    for row in pornVideoList:
        content += row.video_title+'<br>'
    return content


def getTopDailyMailContent():
    pornVideoList = getTopWeeklyPornVideos(10)
    content = 'This is daily top 10 video list.<br>'
    for row in pornVideoList:
        content += row.video_title+'<br>'
    return content


# initialize MySQL database connection
connectMysql()

recipients = {SubscribeType.WEEKLY.value: [], SubscribeType.DAILY.value: []}

# get subscribers email list
emails = getVerifySubscribers()

for row in emails:
    recipients[row.type].append({"Email": row.email})

# send mail to weekly subscribers
if recipients[SubscribeType.WEEKLY.value]:
    sendMail(recipients[SubscribeType.WEEKLY.value], getTopWeeklyMailContent())

# send mail to daily subscribers
if recipients[SubscribeType.DAILY.value]:
    sendMail(recipients[SubscribeType.DAILY.value], getTopDailyMailContent())
