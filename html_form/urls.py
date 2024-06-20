from django.urls import path
from html_form import views

app_name = "html_form"
urlpatterns = [
    path('',views.create_turtle_script, name='create'),
]