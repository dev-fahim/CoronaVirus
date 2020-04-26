from django.contrib import admin
from org_app import models

# Register your models here.


admin.site.register(models.Category)
admin.site.register(models.Organisation)
admin.site.register(models.OrgDetail)
admin.site.register(models.OrgProject)
