from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','listing','email','contact_date')
    list_display_links=('id','name')
    search_fields=('name','emaiil','listing')
    list_per_page=25


admin.site.register(Contact,ContactAdmin)
