#OpenHappiness Models

from google.appengine.ext import db

#User table
class User(db.Model):
	user_id= db.StringProperty()
	handle = db.StringProperty()
	user = db.UserProperty()
	name = db.StringProperty()
	avatar=db.StringProperty()
	description = db.StringProperty(multiline=True)
	followercount=db.IntegerProperty()

#Tag table
#class Tag(db.Model):
#	tag = db.StringProperty()
	
#TaggedResult table
#class TaggedResult(db.Model):
#	tagid = db.IntegerProperty()
#	url = db.StringProperty()
#	tagdate = db.DateTimeProperty(auto_now_add=True)
#	userid = db.ReferenceProperty(User)
	

#Follow table
class Follow(db.Model):
	handle = db.StringProperty()
	userB = db.StringProperty()
	priority = db.IntegerProperty()


