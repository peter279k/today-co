from database.mysqlConnect import BaseModel
from peewee import AutoField, CharField, IntegerField


class Subscribers(BaseModel):
    id = AutoField()
    email = CharField()
    verify = IntegerField()
    type = CharField()

    class Meta:
        table_name = 'subscribers'


def getVerifySubscribers():
    return (Subscribers.select(Subscribers.email, Subscribers.type)
            .where(Subscribers.verify == 1)
            .namedtuples())
