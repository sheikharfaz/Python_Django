from django.contrib import admin
from .models import Core
from .models import Project, MasterSpares, LeavingFromPlaces, Facility

# Register your models here.
@admin.register(Core) #admin.site.register()
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(Project)
admin.site.register(MasterSpares)
admin.site.register(LeavingFromPlaces)
admin.site.register(Facility)