import csv
from io import TextIOWrapper
from django.shortcuts import render

# Create your views here.
def upload_file(request):
    if request.method == 'POST':
        myFile = request.FILES["myFile"]
        if myFile.name.endswith('.csv'):
            turtle_list = []
            csv_file = TextIOWrapper(myFile.file, encoding='utf-8')            
            csv_reader = csv.reader(csv_file)
            next(csv_reader)

            for row in csv_reader:
                firstname = row[0]
                lastname = row[1]
                birthdate = row[2]
                mailingstreet = row[3]
                mailingcity = row[4]
                mailingstate = row[5]
                mailingcountry = row[6]
                mailingpostcode = row[7]
                email = row[8]
                mobilephonenumber = row[8]
                homephonenumber = row[9]
                employeetitle = row[10]
                employername = row[11]
                employerindustry = row[12]
                employerstreet = row[13]
                employercity = row[14]
                employerstate = row[15]
                employerpostcode = row[16]
                employercountry = row[17]
                employeremail = row[18]
                employerphone = row[19]
                employerfax = row[20]

                row_list = [firstname, lastname, birthdate, mailingstreet, mailingcity, mailingstate, 
                            mailingcountry, mailingpostcode, email, mobilephonenumber, homephonenumber, 
                            employeetitle, employername, employerindustry, employerstreet, employercity, 
                            employerstate, employerpostcode, employercountry, employeremail, employerphone, employerfax, ]
                
                print(f"Row list --> {row_list}")
                turtle_list.append(row_list)

            print(f"Turtle List --> {turtle_list}")
            turtle_str = transformation_matrix(turtle_list)

            context = { "turtle": turtle_str}

        return render(request, 'file_upload/upload_file.html', context)
    else:
        return render(request, 'file_upload/upload_file.html')

def transformation_matrix(turtle_list):
    turtle_str = f""
    mdd = "PREFIX mdd: <https://dictionary.mydata.org/#>"
    xsd = "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>"
    rdf = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>"
    cco = "PREFIX cco: <http://www.ontologyrepository.com/CommonCoreOntologies/>"
    pop = "PREFIX pop: <https://opensource.ieee.org/person-ontology-group/person-ontology-project/-/blob/master/dev/Person-Ontology-dev.ttl->"
    
    turtle_str += f"{mdd} \n{xsd} \n{rdf} \n{cco} \n{pop} \n"

    # [firstname, lastname, birthdate, mailingstreet, mailingcity, mailingstate, 
    #                         mailingcountry, mailingpostcode, email, mobilephonenumber, homephonenumber, 
    #                         employeetitle, employername, employerindustry, employerstreet, employercity, 
    #                         employerstate, employerpostcode, employercountry, employeremail, employerphone, employerfax, ]
                

    for row in turtle_list:
        turtle_str += f"""
            cco:Person rdf:type cco:OccupationRole ;	
                cco:ProperName "{row[0]} {row[1]}" ;
                mdd:my-firstname "{row[0]}" ;
                mdd:my-lastname "{row[1]}" ;
                mdd:my-birthdate "{row[2]}"^^xsd:date ;
                mdd:my-mailingstreet "{row[3]}" ;
                mdd:my-mailingcity "{row[4]}" ;
                mdd:my-mailingstate "{row[5]}" ;
                mdd:my-mailingcountry "{row[6]}" ;
                mdd:my-mailingpostcode "{row[7]}" ;
                mdd:my-email "{row[8]}" ;
                mdd:my-mobilephonenumber "{row[9]}" ;
                mdd:my-homephonenumber "{row[10]}" .

            cco:OccupationRole mdd:my-employeetitle "{row[11]}" ;
                mdd:my-employername "{row[12]}" ;
                mdd:my-employerindustry "{row[13]}" ;
                mdd:my-employerstreet "{row[14]}" ;
                mdd:my-employercity "{row[15]}" ;
                mdd:my-employerstate "{row[16]}" ;
                mdd:employerpostcode "{row[17]}" ;
                mdd:employercountry "{row[18]}" ;
                mdd:employerphone "{row[19]}" ;
                mdd:employerfax "{row[20]}" .
        """
    turtle_str += "\n\n # END!"
    print(turtle_str)

    return turtle_str

