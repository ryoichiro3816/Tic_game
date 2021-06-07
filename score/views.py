from django.views.generic import ListView, TemplateView
from .models import User 


# Create your views here.
# class PostDetailView(DetailView):
# 	model = Post 
# 	template_name = 'score/detail.html'

class UserListView(ListView):
	model = User
	template_name = 'score/home.html'

class UserDetailView(TemplateView):
	template_name = 'score/detail.html'