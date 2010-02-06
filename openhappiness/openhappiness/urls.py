# urls.py

from django.conf.urls.defaults import *

urlpatterns = patterns("",
    (r"^$", "openhappiness.main.views.index"),
    (r"^logout/","openhappiness.main.views.logout"),
    (r"^user/","openhappiness.main.views.userprofile"),
    (r"^profile/followlist","openhappiness.main.views.followlist"),
    (r"^profile/followers","openhappiness.main.views.followers"),
    (r"^profile/editprofile","openhappiness.main.views.editprofile"),
    (r"^profile/","openhappiness.main.views.selfprofile"),
    (r"^signup/submitsignup","openhappiness.main.views.submitsignup"),
    (r"^signup/","openhappiness.main.views.signup"),
    (r"^follow/","openhappiness.main.views.follow"),

)

