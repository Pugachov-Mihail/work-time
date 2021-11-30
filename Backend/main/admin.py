from django.contrib import admin

# Register your models here.
from main.models import ShopName, PersonalShope, PlansMonth, PlansDay

admin.site.register(ShopName)
admin.site.register(PersonalShope)
admin.site.register(PlansMonth)
admin.site.register(PlansDay)