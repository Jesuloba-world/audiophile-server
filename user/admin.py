from django.contrib import admin
from .models import CustomUser
from django.apps import apps

admin.site.register(CustomUser)


app = apps.get_app_config("graphql_auth")

for modelname, model in app.models.items():
    admin.site.register(model)
