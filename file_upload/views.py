from django.shortcuts import render

# Create your views here.
def upload_file(request):
    if request.method == 'GET':
        return render(request, 'file_upload/upload_file.html')