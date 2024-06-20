from django.shortcuts import render
from Mapping_and_Transformation.utilities import transformation_matrix

# Create your views here.
def create_turtle_script(request):
    if request.method == "GET":
        return render(request, 'html_form/index.html')
    else:
        firstname = request.POST.get("firstname", None)
        lastname = request.POST.get("lastname", None)
        birthdate = request.POST.get("birthdate", None)
        mailingstreet = request.POST.get("mailingstreet", None)
        mailingcity = request.POST.get("mailingcity", None)
        mailingstate = request.POST.get("mailingstate", None)
        mailingcountry = request.POST.get("mailingcountry", None)
        mailingpostcode = request.POST.get("mailingpostcode", None)
        email = request.POST.get("email", None)
        mobilephonenumber = request.POST.get("mobilephonenumber", None)
        homephonenumber = request.POST.get("homephonenumber", None)
        employeetitle = request.POST.get("employeetitle", None)
        employername = request.POST.get("employername", None)
        employerindustry = request.POST.get("employerindustry", None)
        employerstreet = request.POST.get("employerstreet", None)
        employercity = request.POST.get("employercity", None)
        employerstate = request.POST.get("employerstate", None)
        employerpostcode = request.POST.get("employerpostcode", None)
        employercountry = request.POST.get("employercountry", None)
        employeremail = request.POST.get("employeremail", None)
        employerphone = request.POST.get("employerphone", None)
        employerfax = request.POST.get("employerfax", None)

        row_list = [firstname, lastname, birthdate, mailingstreet, mailingcity, mailingstate, 
                    mailingcountry, mailingpostcode, email, mobilephonenumber, homephonenumber, 
                    employeetitle, employername, employerindustry, employerstreet, employercity, 
                    employerstate, employerpostcode, employercountry, employeremail, employerphone, employerfax, ]            
        turtle_str = transformation_matrix(row_list)

        return render(request, 'html_form/view.html')
