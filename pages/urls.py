from django.urls import path
from pages import views #importing views.py from the pages app

urlpatterns = [
    path('', views.about_me_view, name='about_me'),
    path('experince', views.experince, name='experince'),
]