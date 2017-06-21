from django.contrib import admin
from hello.models import ShoppingItem, Department, Section, Job


admin.site.register(ShoppingItem)
admin.site.register(Department)
admin.site.register(Section)
admin.site.register(Job)


class ShoppingItemAdmin(admin.ModelAdmin):
    pass


class Department(admin.ModelAdmin):
    pass



