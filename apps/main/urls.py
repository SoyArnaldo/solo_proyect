# Django
from django.urls import path, include

# Views (son funciones)
from apps.main.views import home, conocimiento, conocimiento_create, conocimiento_update, conocimiento_delete, conocimiento_read

# Es para evitar conflictos con otras aplicaciones, en caso de que tengamos
# una vista con el mismo nombre.
app_name = 'main'
urlpatterns = [
	path(route='dashboard/', view=home, name='home'),
	path(route='dashboard/conocimiento/', view=conocimiento, name='conocimiento'),
	path(route='dashboard/conocimiento/read', view=conocimiento_read, name='conocimiento_read'),
	path(route='dashboard/conocimiento/<video_id>/create', view=conocimiento_create, name='conocimiento_create'),
	path(route='dashboard/conocimiento/<str:conocimiento>/update', view=conocimiento_update, name='conocimiento_update'),
	path(route='dashboard/conocimiento/<str:conocimiento>/delete', view=conocimiento_delete, name='conocimiento_delete'),
]

