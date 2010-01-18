
# views.py

from google.appengine.api import users
from django.shortcuts import render_to_response, get_object_or_404
#from openhappiness.main.models import User
from django.http import HttpResponseRedirect

from django.views.generic.simple import redirect_to

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
	
		
		



