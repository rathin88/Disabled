from django.contrib import admin
from search.models import User
from search.models import Tag
from search.models import Follow

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Follow)
