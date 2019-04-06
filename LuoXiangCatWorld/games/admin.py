from django.contrib import admin

# Register your models here.
from .models import Cat, Master, Food, Market, Park, Site, Stay, Adopt, Wild, Enjoy, Store, Purchase, Sell

admin.site.register(Cat)
admin.site.register(Master)
admin.site.register(Food)
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

#class UserAdmin(admin.ModelAdmin):
#    list_display = ('user_id', 'name')

#admin.site.register(Master, UserAdmin)

#@admin.register(Cat)
#class CatAdmin(admin.ModelAdmin):
#    list_display = ('id', 'name', 'sex', 'birth', 'health')
#    fields = ['id', 'name', 'sex', ('birth', 'health')]
#    list_filter = ('health', 'birth')
