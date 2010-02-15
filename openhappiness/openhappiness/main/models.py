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

#TagSequence table
class TagSequence(db.Model):
	tag_id=db.IntegerProperty()
	tag_sequence_no=db.IntegerProperty()
	tag=db.StringProperty()
	handle=db.StringProperty()

#UserSearch tag storage table
class UserSearch(db.Model):
	tag_id=db.IntegerProperty()
	url=db.StringProperty()
	handle=db.StringProperty()	

#Follow table
class Follow(db.Model):
	handle = db.StringProperty()
	userB = db.StringProperty()
	priority = db.IntegerProperty()


