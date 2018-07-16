from django.urls import path
from django.views.generic import TemplateView
from .views import CourseListView

app_name = 'course'
urlpatterns = [
	path('about/', TemplateView.as_view(template_name="course/about.html"), name='about'),
	path('course-list/', CourseListView.as_view(), name='course_list'),
]