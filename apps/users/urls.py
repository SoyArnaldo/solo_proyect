from django.urls import path, include
from apps.users.views import  signin, signup, signout, profile, signup_redirect, profile_delete

app_name = 'users'
urlpatterns = [
	path(route='', view=signup, name='signup'), 
	path(route='signin/', view=signin, name='signin'), 
	path(route='signout/', view=signout, name='signout'),
	path(route='profile/<username>', view=profile, name='profile'),
	path(route='profile/<profile>/delete', view=profile_delete, name='profile_delete'),
	path(route='social/signup/', view=signup_redirect, name='signup_redirect'),
    path('', include('apps.main.urls')),
]