from django.contrib import admin
from index.models import gameInfo
# Register your models here.

class gameInfoAdmin(admin.ModelAdmin):
    list_display = ('name','description','bestPrice','bestPriceCountry')

admin.site.register(gameInfo, gameInfoAdmin)
