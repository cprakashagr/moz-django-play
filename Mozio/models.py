from mongoengine import Document
from mongoengine import fields


class Provider(Document):
    name = fields.StringField(verbose_name="name", max_length=25)
    email = fields.StringField(verbose_name="email", max_length=25)
    phoneNumber = fields.StringField(verbose_name="phoneNumber", max_length=15)
    language = fields.StringField(verbose_name="language", max_length=2)
    currency = fields.StringField(verbose_name="currency", max_length=3)


class Polygons(Document):
    name = fields.StringField(verbose_name="name")
    price = fields.IntField(verbose_name="price")
    geometry = fields.PolygonField()
    providerId = fields.ReferenceField(Provider, reverse_delete_rule=2, required=True)

    meta = {
        'indexes': [[("geometry", "2dsphere"), ("datetime", 1)]]
    }
