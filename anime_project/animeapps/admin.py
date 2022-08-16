from django.contrib import admin


from animeapps.models import AppUser,Anime, AnimeType


# Register your models here.
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('first_name','middle_name','last_name',\
                'email','contact','dob','password','address','created_at')


class AnimeTypeAdmin(admin.ModelAdmin):
    list_display = ('anime_name',)

class AnimeAdmin(admin.ModelAdmin):
    list_display = ('anime_name','Character','description')

admin.site.register(AppUser,AppUserAdmin)
admin.site.register(AnimeType,AnimeTypeAdmin)
admin.site.register(Anime,AnimeAdmin)
admin.site.site_title = "DASHBOARD"
admin.site.site_header = "Anime Store"
admin.site.index_title = "Anime Stote Admin"

    