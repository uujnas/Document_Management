
from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    
	path('',views.log_in, name='login'),
	path('logout/',views.log_out, name='logout'),
	path('password/', views.change_password, name='change_password'),
]
