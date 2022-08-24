from django.contrib import admin
from django.urls import path, include
from . import views
from clients import views as V

urlpatterns = [
	path('', views.index, name = 'index'),
	path('signup', views.signup, name='signup'),
	path('signin', views.signin, name='signin'),
	path('signout', views.signout, name='signout'),
	path('home', V.home_view, name='home'),
	path('activate/<uidb64>/<token>', views.activate, name='activate'),


]