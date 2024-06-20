from django.shortcuts import render
from Mapping_and_Transformation.utilities import transformation_matrix

# Create your views here.
def create_turtle_script(request):
    if request.method == "GET":
        return render(request, 'html_form/index.html')
    else:
        pass
