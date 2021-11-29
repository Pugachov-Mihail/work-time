from django.contrib import admin

# Register your models here.
from main.models import ShopName, PersonalShope, PlansMonth

admin.site.register(ShopName)
admin.site.register(PersonalShope)
admin.site.register(PlansMonth)