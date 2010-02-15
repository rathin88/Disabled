#OpenHappiness Views add django forms

from google.appengine.api import users
from google.appengine.ext.db import *

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.simple import redirect_to

from openhappiness.main.models import User
from openhappiness.main.models import Follow

def index(request):
	user=users.get_current_user()
	if not user:
		return HttpResponseRedirect(users.create_login_url(request.path))
	else:
		return render_to_response('main/index.html',{})
		
def logout(request):
	user=users.get_current_user()
	if user:
		return HttpResponseRedirect(users.create_logout_url(request.path))
	else:
		return render_to_response('main/logout.html',{})

def signup(request):
	user=users.get_current_user()
	if not user:
		return HttpResponseRedirect(users.create_login_url(request.path))
	else:
		user_id=user.user_id()
		return render_to_response('main/signup/signup.html',{"user_id":user_id})

# user_id, name, description, avatar
def submitsignup(request):
	user=users.get_current_user()
	params=request.GET
	user_id=params['user_id']
	name=params['name']
	description=params['description']
	avatar=params['avatar']
	handle=user.nickname()
	query = GqlQuery("SELECT * FROM User WHERE handle = :hndl", hndl=str(handle))
	result=query.get()
	if result is None:
		newUser= User()
		newUser.user_id=user_id
		newUser.name=name
		newUser.description=description
		newUser.handle=handle
		newUser.avatar=avatar
		newUser.followercount=0
		newUser.put()
		return render_to_response('main/signup/submitaccount.html',{"user_id":user_id, "name": name, "description": description ,"nickname": handle} )
	else:
		return render_to_response('main/signup/signuperror.html', {"user_id":result.user_id, "name": result.name, "nickname": result.handle} )

# handle
def userprofile(request):
	user=users.get_current_user()
	params=request.GET
	handle=params['handle']
	qurey = GqlQuery("SELECT * FROM User WHERE handle=:hndl", hndl=handle)
	profile_details=qurey.get()
	if profile_details is not None:
		return render_to_response('main/profile/userprofile.html', {"name": profile_details.name, "nickname":profile_details.handle, "user_id":profile_details.user_id, "description":profile_details.description, "avatar":profile_details.avatar})
	else:
		return render_to_response('main/profile/userprofileerror.html', {"handle":handle})

		
# action
def selfprofile(request):
	user=users.get_current_user()
	params=request.GET
	action=params['action']
	handle=user.nickname()
	qurey = GqlQuery("SELECT * FROM User WHERE handle=:hndl", hndl=handle)
	profile_details = qurey.get()
	if action=="show":
		return render_to_response('main/profile/profile.html',  {"name": profile_details.name, "nickname":profile_details.handle, "user_id":profile_details.user_id, "description":profile_details.description, "avatar":profile_details.avatar})
	if action=="edit":
		return render_to_response('main/profile/editprofile.html', {"name": profile_details.name, "nickname":profile_details.handle, "user_id":profile_details.user_id, "description":profile_details.description, "avatar":profile_details.avatar})

# user_id, name, description, avatar
def editprofile(request):
	user=users.get_current_user()
	params=request.GET
	newUser=User()
	newUser.user_id=params['user_id']
	newUser.name=params['name']
	newUser.description=params['description']
	newUser.avatar=params['avatar']
	newUser.handle=user.nickname()
	newUser.put()
	return render_to_response('main/profile/profile.html', {"name": newUser.name, "nickname":newUser.handle, "user_id":newUser.user_id, "description":newUser.description, "avatar":newUser.avatar})

# handleB, priority
def follow(request):
	user=users.get_current_user()
	params=request.GET
	newFollow=Follow()
	newFollow.handle=user.nickname()
	newFollow.userB=params['handleB']
	newFollow.priority=int(params['priority'])
	newFollow.put()
	query = GqlQuery("SELECT * FROM Follow WHERE handle=:hndl", hndl=user.nickname())
	followlist = query.fetch(0)
	return render_to_response('main/profile/followlist.html',  {"followlist": followlist})

def listfollow(request):
	user=users.get_current_user()
	query = GqlQuery("SELECT * FROM Follow WHERE handle=:hndl", hndl=user.nickname())
	followlist = query.fetch(0)
	return render_to_response('main/profile/followlist.html',  {"followlist": followlist})

def followers(request):
	user=users.get_current_user()
	query = GqlQuery("SELECT * FROM Follow WHERE userB=:usrB", usrB=user.nickname())
	followerlist = query.fetch(0)
	return render_to_response('main/profile/followers.html', {"followerlist" : followerlist})

