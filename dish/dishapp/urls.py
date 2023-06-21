from django.contrib import admin
from django.urls import path

from .views import (
	import_csv,home,search_hotels,
	)

urlpatterns = [

	path('import_csv/',import_csv,name='import_csv'),
	path('',home,name='home'),
	path('search_hotels/', search_hotels, name='search_hotels'),
]