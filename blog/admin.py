# This is where you register admin models so they show up on django's admin page

from django.contrib import admin
from .models import Post

admin.site.register(Post)

