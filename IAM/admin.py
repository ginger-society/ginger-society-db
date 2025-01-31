from gingerdj.contrib import admin

from .models import *

def create_model_admin(model):
    class ModelAdmin(admin.ModelAdmin):
        list_display = [field.name for field in model._meta.fields]
        search_fields = [field.name for field in model._meta.fields if isinstance(
            field, models.CharField)]
        list_filter = [field.name for field in model._meta.fields]

    return ModelAdmin




admin.site.register(user, create_model_admin(user) )


admin.site.register(app, create_model_admin(app) )


admin.site.register(group, create_model_admin(group) )


admin.site.register(api_token, create_model_admin(api_token) )


admin.site.register(tableexample, create_model_admin(tableexample) )

