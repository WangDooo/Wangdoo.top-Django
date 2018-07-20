from django.urls import path
from django.views.generic import TemplateView

app_name = 'kaisai'
urlpatterns = [
	path('kaisai-manage/', TemplateView.as_view(template_name="course/about.html"), name='kaisai_manage'),
	
]