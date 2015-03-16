from django.contrib import admin 
from dataomaha.models import *

class AppAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'section', 'featured', 'section_feature', )
    list_filter = [ 'section', 'featured', ]
	
admin.site.register(App, AppAdmin)
admin.site.register(Section)

