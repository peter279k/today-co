# TodayCo

# We're back
As you will see, this prepository has been inactive for about three years.

The `Sielx` framework has been deprecated from Symfony team.

And glad that [@youmu257](https://github.com/youmu257) comes back to do this at his available time to do contributions for this repository.

## Introduction
- This service will send the newsletters every week after subscribing the newsletter.

- We also provide the top 10 videos for users to preview them.

## Requirements
If you want to build this web service for yourself, the requirements are as follows:

- A VPS hosting(The current OS is Ubuntu)
- PHP 7
- Python 3
- Composer(The dependency package manager of PHP)
- MySQL

## TO DO

- Complete the front-end website
- Complete the Python cron script(MySQL)
- Complete the newsletter template
- Complete the PHP backend functionality(e.g. store unsubscribed/subscribed email address)
- Verify the email address before storing them in the MySQL database
- Build the Database Migration(Phinx)
- Make the code clean and readability(coding style)

## Database Schema

Table1: subscribers

| filed nmae | field type(length) | comment                  | auto_increment?  |
| -----------|--------------------|--------------------------|----------------- |
| id         | int(10)primary key | the user email address id                   | yes |
| email      | varchar(50)        | the user email address                      | no  |
| verify     | boolean            | users whether has verified the email address| no  |
| type       | varchar(6)         | subscribe video is weekly or daily          | no  |

Table2: porn_videos

| filed nmae  | field type(length) | comment                         | auto_increment? |
| ------------|--------------------|---------------------------------|-----------------|
| id          | int(10)primary key | the primary key id              | yes             |
| source      | varchar(10)        | video source(xvideo/avgle...)   | no              |
| view_numbers| medium int         | the video view numbers          | no              |
| video_id    | int(50)            | the video url                   | no              |
| view_ratings| varchar(10)        | the video ratings               | no              |
| video_title | varchar(50)        | the video images title          | no              |
| create_date | date(yyyy-mm-dd)   | the date of creating video      | no              |

Table3: sites_format

| filed nmae | field type(length) | comment                         | auto_increment? |
| -----------|--------------------|---------------------------------|-----------------|
| id         | int(10)primary key | the primary key id              | yes             |
| source     | varchar(10)        | video source(xvideo/avgle...)   | no              |
| video_url  | varchar(100)| www.xvideos.com/video{video_id}/{video_title}| no        |
| video_images| varchar(100)| img-egc.xvideos.com/videos/thumbs/{1}/{2}/{3}/{uid}/{uid_img}| no |

## The sites format rule

In this section, we present the websites video and image url format.

| source | image/video| format url                                                     |
| -------|------------|----------------------------------------------------------------|
| avgle  | image      | static.avgle.com/media/videos/tmb2/{video_id}/{image_file_name}|
| avgle  | video      | avgle.com/video/{video_id}/{video_title}                       |
| xvideo | image      | img-egc.xvideos.com/videos/thumbs/{1}/{2}/{3}/{uid}/{uid_img}  |
| xvideo | video      | www.xvideos.com/video{video_id}/{video_title}                  |

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

- Create the database named ```kaogun```.

- Replace the user name and password ```phinx.yml``` in production section.

Here is the sample settings are as follows:

```bash
production:
    adapter: mysql
    host: localhost
    name: production_db
    user: your_user_name
    pass: your_password
    port: 3306
    charset: utf8
```

- In the VPS server, run the ```vendor/bin/phinx migrate -e development -t 20170822112955``` to initial the Databse table.
