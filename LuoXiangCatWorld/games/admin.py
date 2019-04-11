from django.contrib import admin

# Register your models here.
from .models import *

#admin.site.register(Cat)
#admin.site.register(Master)
#admin.site.register(Food)
admin.site.register(Market)
admin.site.register(Park)
admin.site.register(Site)
admin.site.register(Stay)
admin.site.register(Adopt)
admin.site.register(Wild)
admin.site.register(Enjoy)
admin.site.register(Store)
admin.site.register(Purchase)
admin.site.register(Sell)
admin.site.register(Feed)

class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'money')

admin.site.register(Master, MasterAdmin)

@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'sex', 'age', 'health')
    fields = ['name', 'breed', 'sex', 'age', 'birth', ('father', 'mother'), 'mate', 'health']
    list_filter = ('health', 'birth')

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'effect')

admin.site.register(Food, FoodAdmin)

