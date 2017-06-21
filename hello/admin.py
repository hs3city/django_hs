from django.contrib import admin
from hello.models import User, Department, Section, Job


admin.site.register(User)
admin.site.register(Department)
admin.site.register(Section)
admin.site.register(Job)


class UserAdmin(admin.ModelAdmin):
    pass


class Department(admin.ModelAdmin):
    pass



