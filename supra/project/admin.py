from project.models import CompanyType, ProjectCategory, ProjectStatus, Company, Project
from django.contrib import admin

admin.site.register(CompanyType)
admin.site.register(ProjectCategory)
admin.site.register(ProjectStatus)
admin.site.register(Company)
admin.site.register(Project)