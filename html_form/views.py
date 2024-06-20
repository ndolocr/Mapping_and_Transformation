from django.shortcuts import render
from Mapping_and_Transformation.utilities import transformation_form_matrix

# Create your views here.
def create_turtle_script(request):
    if request.method == "GET":
        return render(request, 'html_form/index.html')
    else:
        firstname = request.POST.get("firstname", "")
        lastname = request.POST.get("lastname", "")
        birthdate = request.POST.get("birthdate", "")
        mailingstreet = request.POST.get("mailingstreet", "")
        mailingcity = request.POST.get("mailingcity", "")
        mailingstate = request.POST.get("mailingstate", "")
        mailingcountry = request.POST.get("mailingcountry", "")
        mailingpostcode = request.POST.get("mailingpostcode", "")
        email = request.POST.get("email", "")
        mobilephonenumber = request.POST.get("mobilephonenumber", "")
        homephonenumber = request.POST.get("homephonenumber", "")
        employeetitle = request.POST.get("employeetitle", "")
        employername = request.POST.get("employername", "")
        employerindustry = request.POST.get("employerindustry", "")
        employerstreet = request.POST.get("employerstreet", "")
        employercity = request.POST.get("employercity", "")
        employerstate = request.POST.get("employerstate", "")
        employerpostcode = request.POST.get("employerpostcode", "")
        employercountry = request.POST.get("employercountry", "")
        employeremail = request.POST.get("employeremail", "")
        employerphone = request.POST.get("employerphone", "")
        employerfax = request.POST.get("employerfax", "")

        row_list = [firstname, lastname, birthdate, mailingstreet, mailingcity, mailingstate, 
                    mailingcountry, mailingpostcode, email, mobilephonenumber, homephonenumber, 
                    employeetitle, employername, employerindustry, employerstreet, employercity, 
                    employerstate, employerpostcode, employercountry, employeremail, employerphone, employerfax, ]
        turtle_str = transformation_form_matrix(row_list)

        # print(f"Row List --> {row_list}")

        context = { "turtle": turtle_str}
        return render(request, 'html_form/view.html', context)
