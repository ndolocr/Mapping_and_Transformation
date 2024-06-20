from django.urls import path
from api_call import views

app_name = "api_call"
urlpatterns = [
    path('call',views.create_turtle_script, name='upload_file')
]