from database.mysqlConnect import BaseModel
from peewee import AutoField, CharField


class SitesFormat(BaseModel):
    id = AutoField()
    source = CharField()
    video_url = CharField()
    video_images = CharField()

    class Meta:
        table_name = 'sites_format'


def getSitesFormatBySource(source):
    return (SitesFormat.select(SitesFormat.video_url, SitesFormat.video_images)
            .where(SitesFormat.source == source)
            .namedtuples())
