
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .import views
#from django.views.generic import TemplateView
from .views import BasicUploadView, ProgressBarUploadView,DragAndDropUploadView

app_name='upload'
urlpatterns = [
	
	path('', views.file_upload,name='file_upload'),
	path('folder/', views.create_folder,name='folder'),
	path('add_file/', views.add_file, name='add_file'),
	path('<id>/remove_folder/',views.remove_folder,name='remove_folder'),
	path('<id>/rename_folder/',views.rename_folder,name='rename_folder'),
	path('<id>/folder_detail',views.folder_detail,name="folder_detail"),
	path('files/', views.upload_files,name='files'),
	path('search/', views.search_file,name='search_files'),
	path('searchfile/', views.Search_File_New,name='search_file_new'),
	path('filterfiles/', views.filterfiles,name='filterfiles'),
	#path('files/<int:pk>/', views.FileUpdateView.as_view(),name='edit_file'),
	path('edit/<int:pk>/', views.Editfiles,name='Editfiles'),
	#path('edit_save/<int:pk>/', views.Editfiles_save,name='Editfiles_save'),
	path('view/<int:pk>/', views.Viewfiles,name='Viewfiles'),
	path('Download/<int:pk>/', views.Downloadfiles,name='Downloadfiles'),
	path('signup/',views.signup,name='signup'),
	path('manage_user/',views.manage_user,name='manage_user'),
	path('users/',views.user_list_new,name='user_list_new'),
	path('modify/<int:pk>/',views.modify_user,name='modify_user'),
	path('Contacts/',views.UserContacts,name='Contacts'),
	path('addContacts/',views.ADDContacts,name='addContacts'),
	path('search_contact/',views.Search_Contact,name='Search_Cont'),
	path('clear/', views.clear_database, name='clear_database'),
    #path('', BasicFileUploadView.as_view(), name='basic-upload'),
	path('basic/', BasicUploadView.as_view(), name='basic_upload'),
	#path('multiple/', MultipleUploadView.as_view(), name='multiple_upload'),
	path('progressbar/', ProgressBarUploadView.as_view(), name='progress_bar_upload'),
	path('draganddrop/', DragAndDropUploadView.as_view(), name='drag_and_drop_upload'),
	path('multipleupload/', views.multipleupload, name='multipleupload'), 
	path('view_profile/', views.view_profile, name='view_profile'),
	#path('change_profile_image/', views.change_profile_image, name='change_profile_image'),
	path('update_profile_image/', views.update_profile_image, name='update_profile_image'),
	path('view_user_profile/<int:pk>/', views.view_user_profile, name='view_user_profile'),

	
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
