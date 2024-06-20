from django.urls import path
from api_call import views

app_name = "html_form"
urlpatterns = [
    path('create',views.create_turtle_script, name='create'),
]