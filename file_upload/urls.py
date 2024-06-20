from django.urls import path
from file_upload import views

app_name = "file_upload"
urlpatterns = [
    path('',views.upload_file, name='upload_file')
]