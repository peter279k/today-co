# TodayCo

## Introduction
- This service will send the newsletters every week after subscribing the newsletter.

- We also provide the top 10 videos for users to preview them.

## Requirements
If you want to build this web service for yourself, the requirements are as follows:

- A VPS hosting
- PHP 7
- Python 3
- Composer(the package manager of PHP)
- MySQL

## TO DO

- Complete the front-end website
- Complete the Python cron script(MySQL)
- Complete the newsletter template
- Complete the PHP backend functionality(e.g. store unsubscribed/subscribed email address)
- Verify the email address before storing them in the MySQL database
- Build the Database Migration(Phinx)

## Database Schema

Table1: subscribers

| filed nmae | field type(length) | comment                  | auto_increment?  |
| -----------|--------------------|--------------------------|----------------- |
| id         | int(10)            | the user email address id                   | yes |
| email      | varchar(50)        | the user email address                      | no  |
| verify     | boolean            | users whether has verified the email address| no  |

Table2: porn_videos

| filed nmae  | field type(length) | comment                         | auto_increment? |
| ------------|--------------------|---------------------------------|-----------------|
| id          | int(10)            | the video id                    | yes             |
| source      | varchar(10)        | the video source(xvideo/Avgle)  | no              |
| view_numbers| int(10)            | the video view numbers          | no              |
| view_ratings| varchar(5)         | the video ratings               | no              |
| create_date | date(yyyy-mm-dd)   | the date of creating video      | no              |

## Installation

We have the two parts to build our awesome service.

The one is websites and another one is crontab daemon scripts.

This section only includes the building websites.

If you want to more details about the crontab daemon scripts, please check out this [guide](https://github.com/peter279k/today-co/blob/master/scripts/README.md).

### Buidling website

We use the composer to install the required PHP packages.The steps are as follows:

- download the Composer

```php
curl -sS https://getcomposer.org/installer | php
```

- install the required PHP packages via Composer

```php
php composer.phar install
```

- Replace the db username and password in ```migrations.php```

- Using the migrations to initial the Databse

- Enjoy it!

## Database Migration

We strongly recommend you using the [Phinx](https://phinx.org) to build the database.

The building guide is as follows:

- 
