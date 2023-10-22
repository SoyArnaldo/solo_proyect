from django.contrib import admin
from apps.main.models import Conocimiento

class ConocimientoAdmin(admin.ModelAdmin):
	fieldsests = [
		("Header", {"fields": [ "author", "link_video"]}),
		("Content", {"fields": ["conocimiento"]}),
		("Date", {"fields": ["modified"]})
	]
# Register your models here.
admin.site.register(Conocimiento, ConocimientoAdmin)