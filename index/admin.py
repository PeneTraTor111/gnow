from django.contrib import admin
from index.models import gameInfo,gRadio
# Register your models here.

class gameInfoAdmin(admin.ModelAdmin):
    list_display = ('name','description','bestPrice','bestPriceCountry')

admin.site.register(gameInfo, gameInfoAdmin)

class gRadioAdmin(admin.ModelAdmin):
    list_display = ('head','time','href','imgSrc','imgTitle','describe')

admin.site.register(gRadio, gRadioAdmin)