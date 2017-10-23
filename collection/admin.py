from django.contrib import admin
from collection.models import Thing

# Register your models here.
class ThingAdmin(admin.ModelAdmin):
    model = Thing
    list_display = ('name','description',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Thing, ThingAdmin)
