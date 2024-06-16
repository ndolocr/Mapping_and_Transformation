from django.urls import path
from file_upload import views

urlpatterns = [
    path('',views.upload_file, name='upload_file')
]