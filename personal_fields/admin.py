from django.contrib import admin

from  .models import Form, Text_field, Text_area, Select_item, Item_field, User
# Register your models here.

admin.site.register(Form)
admin.site.register(Select_item)
admin.site.register(Text_field)
admin.site.register(Text_area)
admin.site.register(Item_field)
