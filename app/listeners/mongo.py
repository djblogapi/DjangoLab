from mongoengine import *

connect(host="mongodb://root:mongoadmin@recognition_mongodb:27017/mongodb?authSource=admin")


class MQTT(Document):
    encoding = ListField()
    created = DateTimeField()
