from django.db import models
from google.appengine.ext import db

#User table
class User(db.Model):
	user = db.UserProperty(primary_key=True)
	name = db.StringProperty()
	description = db.StringProperty(multiline=True)

#Tag table
class Tag(db.Model):
	tagid = db.IntegerProperty(primary_key=True)
	url = db.StringProperty()
	tagdate = db.DateTimeProperty(auto_now_add=True)
	userid = db.ReferenceProperty(User)

#Follow table
class Follow(db.Model):
	userSelf = db.ReferenceProperty(User)
	userTo = db.ReferenceProperty(User)
	priority = db.IntegerProperty()
	
