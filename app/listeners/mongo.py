from mongoengine import DateTimeField, Document, ListField
from django.conf import settings
from mongoengine import *

connect(host="mongodb://root:mongoadmin@recognition_mongodb:27017/mongodb?authSource=admin")
# connect(host=settings.MONGODB_URL)

class MQTT(Document):
    encoding = ListField()
    created = DateTimeField()