from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'cal'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
	url(r'^checkin/$',views.checkin, name='check_in'),
	path('checkout/<int:pk>/', views.checkout, name='check_out'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
	# url(r'^Leaveview/$', views.LeaveView.as_view(), name='LeaveView'),
    url(r'^leave/new/$', views.event, name='event_new'),
	url(r'^event/edit/(?P<Leave_id>\d+)/$', views.event, name='event_edit'),
	path('view_attendance/<int:pk>/', views.view_attendance, name='view_attendance'),
	path('view_leave/<int:pk>/',views.view_leave,name='view_leave'),
]
#path('edit/<int:pk>/', views.Editfiles,name='Editfiles'),