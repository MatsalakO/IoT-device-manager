from peewee import Model, CharField, ForeignKeyField, PostgresqlDatabase


db = PostgresqlDatabase(
    "test_database",
    user="postgres",
    password="1234",
    host="localhost",
    port=5432,
)


class BaseModel(Model):
    class Meta:
        database = db


class ApiUser(BaseModel):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()


class Location(BaseModel):
    name = CharField()


class Device(BaseModel):
    name = CharField()
    type = CharField()
    login = CharField()
    password = CharField()
    location = ForeignKeyField(Location, backref="devices")
    api_user = ForeignKeyField(ApiUser, backref="devices")


db.connect()
db.create_tables([ApiUser, Location, Device])
db.close()
