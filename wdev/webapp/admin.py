from django.contrib import admin
from .models import Cards, Homepage
admin.site.register(Homepage) #Make the our app modifiable in the admin and question is displayed in admin.
admin.site.register(Cards)
