
# Register your models here.
from django.contrib import admin
from rango.models import Category, Page

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)


#admin.site.register(Category)
#admin.site.register(Page)
