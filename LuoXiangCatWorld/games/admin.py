from django.contrib import admin

# Register your models here.
from .models import *

#admin.site.register(Cat)
#admin.site.register(Master)
#admin.site.register(Food)
admin.site.register(Market)
admin.site.register(Park)
admin.site.register(Adopt)
admin.site.register(Wild)
admin.site.register(Store)
admin.site.register(Sell)
admin.site.register(Feed)

class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'money')

admin.site.register(Master, MasterAdmin)

@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'master', 'sex', 'age', 'hunger')
    #fields = ['name', 'breed', 'sex', 'age', 'birth', 'hunger']
    list_filter = ('hunger', 'birth')

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'effect')

admin.site.register(Food, FoodAdmin)

