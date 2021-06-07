from django.urls import path
from . import views
urlpatterns = [
	path('', views.UserListView.as_view(), name='score-home'),
	path('post/', views.UserDetailView.as_view(), name='score-detail'),
	
]