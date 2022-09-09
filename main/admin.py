from django.contrib import admin
from main.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display  = ('user', 'slug', 'date_added')
    search_fields = ['user',]

class ItemAdmin(admin.ModelAdmin):
    list_display  = ('user', 'item', 'date_added')
    search_fields = ['user',]

admin.site.register(Profile)
#admin.site.register(Item, ItemAdmin)
# admin.site.register(Post, PostAdmin)
#admin.site.register(Comment, PostComment)