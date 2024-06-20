import json
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from Mapping_and_Transformation.utilities import transformation_matrix

# Create your views here.

@api_view(['POST'])
def create_turtle_script(request):
    if request.method == "POST":
        turtle_list = []
        results = json.loads(request.body)

        for result_dict in results:
            firstname = result_dict["firstname"]
            lastname = result_dict["lastname"]
            birthdate = result_dict["birthdate"]
            mailingstreet = result_dict["mailingstreet"]
            mailingcity = result_dict["mailingcity"]
            mailingstate = result_dict["mailingstate"]
            mailingcountry = result_dict["mailingcountry"]
            mailingpostcode = result_dict["mailingpostcode"]
            email = result_dict["email"]
            mobilephonenumber = result_dict["mobilephonenumber"]
            homephonenumber = result_dict["homephonenumber"]
            employeetitle = result_dict["employeetitle"]
            employername = result_dict["employername"]
            employerindustry = result_dict["employerindustry"]
            employerstreet = result_dict["employerstreet"]
            employercity = result_dict["employercity"]
            employerstate = result_dict["employerstate"]
            employerpostcode = result_dict["employerpostcode"]
            employercountry = result_dict["employercountry"]
            employeremail = result_dict["employeremail"]
            employerphone = result_dict["employerphone"]
            employerfax = result_dict["employerfax"]

            row_list = [firstname, lastname, birthdate, mailingstreet, mailingcity, mailingstate, 
                            mailingcountry, mailingpostcode, email, mobilephonenumber, homephonenumber, 
                            employeetitle, employername, employerindustry, employerstreet, employercity, 
                            employerstate, employerpostcode, employercountry, employeremail, employerphone, employerfax, ]            
            turtle_list.append(row_list)

        turtle_str = transformation_matrix(turtle_list)
    
    return JsonResponse({"Turtle": turtle_str})