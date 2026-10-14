from django.contrib import admin

# Register your models here.
from learning_logs.models import Entry, Topic

admin.site.register(Topic)
admin.site.register(Entry)
