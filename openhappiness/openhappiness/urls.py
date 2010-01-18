# urls.py

from django.conf.urls.defaults import *

urlpatterns = patterns("",
    (r"^$", "openhappiness.main.views.index"),
    (r"^logout/","openhappiness.main.views.logout")
)

