# TodayCo

## Introduction
- This service will send the newsletters every week after subscribing the newsletter.

- We also provide the top 10 videos for users to preview them.

## TO DO

- Complete the front-end website
- Complete the Python cron script(MySQL)
- Complete the newsletter template
- Complete the PHP backend functionality(e.g. store unsubscribed/subscribed email address)
- Verify the email address before storing them in the MySQL database

## Database Schema

Table1: subscribers

| filed nmae | field type(length) | comment                  | auto_increment? |
| -----------|--------------------|--------------------------|-----------------|
| id         | int(10)            | the user email address id| yes |
| email      | varchar(50)        | the user email address   | no  |
| verify     | boolean            | whether user verify the email address | no  |

Table2: porn_videos

| filed nmae | field type(length) | comment                  | auto_increment? |
| -----------|--------------------|--------------------------|-----------------|
| id         | int(10)            | the video id                     | yes |
| source     | varchar(10)        | the video source(xvideo/Avgle)   | no  |
| create_date| date(yyyy-mm-dd)   | the video create date            | no  |
