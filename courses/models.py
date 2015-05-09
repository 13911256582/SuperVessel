from django.db import models

# Create your models here.

from mongoengine import *
#from SuperClass.settings import DBNAME

connect('courseDB')

class Article(Document):
    uuid = UUIDField()
    title = StringField(max_length=120, required=True)
    title_en = StringField(max_length=120, required=True)
    abstract = StringField(max_length=120, required=True)
    abstract_en = StringField(max_length=120, required=True)

    createdTime = DateTimeField()
    coverImg = StringField()
    content = StringField()
    content_en = StringField()


class Comment(EmbeddedDocument):
    content = StringField()
    author = StringField(max_length=120, required=True)
    createdTime = DateTimeField() 

class Course(Document):
    title = StringField(max_length=120, required=True)
    description = StringField()
    author = StringField(max_length=120, required=True)
    createdTime = DateTimeField()
    comments = ListField(EmbeddedDocumentField(Comment))
    imageURL = URLField()
    videoURL = URLField()
    duration = IntField(default=0)
    viewCount = IntField(default=0)
    commentCount = IntField(default=0)



