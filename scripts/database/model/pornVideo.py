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
