from django.contrib import admin
from agency.models import Category, Estate, Headermenu, Page

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name','parent_category')

class EstateAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name','category')
        
class HeadermenuAdmin(admin.ModelAdmin):
    list_display = ('name','url')
    
class PageAdmin(admin.ModelAdmin):
    list_display = ('title','slug')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Estate, EstateAdmin)
admin.site.register(Headermenu, HeadermenuAdmin )
admin.site.register(Page, PageAdmin)
