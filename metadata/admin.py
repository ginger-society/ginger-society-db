from gingerdj.contrib import admin

from .models import *

def create_model_admin(model):
    class ModelAdmin(admin.ModelAdmin):
        list_display = [field.name for field in model._meta.fields]
        search_fields = [field.name for field in model._meta.fields if isinstance(
            field, models.CharField)]
        list_filter = [field.name for field in model._meta.fields]

    return ModelAdmin









admin.site.register(dbschema, create_model_admin(dbschema) )


admin.site.register(dbschema_branch, create_model_admin(dbschema_branch) )


admin.site.register(templates, create_model_admin(templates) )


admin.site.register(service, create_model_admin(service) )


admin.site.register(service_envs, create_model_admin(service_envs) )


admin.site.register(package, create_model_admin(package) )


admin.site.register(package_env, create_model_admin(package_env) )


admin.site.register(organization, create_model_admin(organization) )


admin.site.register(snapshots, create_model_admin(snapshots) )

