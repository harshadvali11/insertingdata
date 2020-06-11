from django.contrib import admin

# Register your models here.

# importing models from application
from app.models import *

# syntax for registering a model is admin.site.register(Modelname)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Access_Records)

'''
#if u rimporting module directly like
from app import models

admin.site.register(models.Topic)
'''