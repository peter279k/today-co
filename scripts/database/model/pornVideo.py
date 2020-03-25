import datetime
from database.mysqlConnect import BaseModel
from peewee import AutoField, CharField, IntegerField, DateTimeField


class PornVideo(BaseModel):
    id = AutoField()
    source = CharField()
    view_numbers = IntegerField()
    video_id = CharField()
    view_ratings = CharField()
    video_title = CharField()
    create_date = DateTimeField()

    class Meta:
        table_name = 'porn_videos'


def getTopWeeklyPornVideos(top):
    today = datetime.date.today()
    lastSevenDay = today - datetime.timedelta(days=7)

    return (PornVideo.select()
            .where(PornVideo.create_date >= lastSevenDay)
            .order_by(PornVideo.view_ratings.desc())
            .limit(top)
            .namedtuples())


def getTopDailyPornVideos(top):
    return (PornVideo.select()
            .where(PornVideo.create_date >= datetime.date.today())
            .order_by(PornVideo.view_ratings.desc())
            .limit(top)
            .namedtuples())
