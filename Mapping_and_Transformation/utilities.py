def transformation_matrix(turtle_list):
    turtle_str = f""
    mdd = "PREFIX mdd: <https://dictionary.mydata.org/#>"
    xsd = "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>"
    rdf = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>"
    cco = "PREFIX cco: <http://www.ontologyrepository.com/CommonCoreOntologies/>"
    pop = "PREFIX pop: <https://opensource.ieee.org/person-ontology-group/person-ontology-project/-/blob/master/dev/Person-Ontology-dev.ttl->"
    
    turtle_str += f"{mdd} \n{xsd} \n{rdf} \n{cco} \n{pop} \n"

    for row in turtle_list:
        turtle_str += f"\n cco:Person rdf:type cco:OccupationRole ; \n"
        if row[0] != "":
            turtle_str += f'mdd:my-firstname "{row[0]}" ; \n'
        if row[1] != "":
            turtle_str += f'mdd:my-lastname "{row[1]}" ; \n'
        if row[2] != "":
            turtle_str += f'mdd:my-birthdate "{row[2]}"^^xsd:date ; \n'
        if row[3] != "":
            turtle_str += f'mdd:my-mailingstreet "{row[3]}" ; \n'
        if row[4] != "":
            turtle_str += f'mdd:my-mailingcity "{row[4]}" ; \n'
        if row[5] != "":
            turtle_str += f'mdd:my-mailingstate "{row[5]}" ; \n'
        if row[6] != "":
            turtle_str += f'mdd:my-mailingcountry "{row[6]}" ; \n'
        if row[7] != "":
            turtle_str += f'mdd:my-mailingpostcode "{row[7]}" ; \n'
        if row[8] != "":
            turtle_str += f'mdd:my-email "{row[8]}" ; \n'
        if row[9] != "":
            turtle_str += f'mdd:my-mobilephonenumber "{row[9]}" ; \n'
        if row[10] != "":
            turtle_str += f'mdd:my-homephonenumber "{row[10]}" . \n'
        if row[11] != "":
            turtle_str += f'\n cco:OccupationRole mdd:my-employeetitle "{row[11]}" ; \n'
        if row[12] != "":
            turtle_str += f'mdd:my-employername "{row[12]}" ; \n'
        if row[13] != "":
            turtle_str += f'mdd:my-employerindustry "{row[13]}" ; \n'
        if row[14] != "":
            turtle_str += f'mdd:my-employerstreet "{row[14]}" ; \n'
        if row[15] != "":
            turtle_str += f'mdd:my-employercity "{row[15]}" ;\n'
        if row[16] != "":
            turtle_str += f'mdd:my-employerstate "{row[16]}" ; \n'
        if row[17] != "":
            turtle_str += f'mdd:employerpostcode "{row[17]}" ; \n'
        if row[18] != "":
            turtle_str += f'mdd:employercountry "{row[18]}" ; \n'
        if row[19] != "":
            turtle_str += f'mdd:employerphone "{row[19]}" ; \n'
        if row[20] != "":
            turtle_str += f'mdd:employerfax "{row[20]}" .\n'
      
    turtle_str += "\n\n # END!"
    print(turtle_str)

    return turtle_str

def transformation_form_matrix(row):
    turtle_str = f""
    mdd = "PREFIX mdd: <https://dictionary.mydata.org/#>"
    xsd = "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>"
    rdf = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>"
    cco = "PREFIX cco: <http://www.ontologyrepository.com/CommonCoreOntologies/>"
    pop = "PREFIX pop: <https://opensource.ieee.org/person-ontology-group/person-ontology-project/-/blob/master/dev/Person-Ontology-dev.ttl->"
    
    turtle_str += f"{mdd} \n{xsd} \n{rdf} \n{cco} \n{pop} \n"

    turtle_str += f"\n cco:Person rdf:type cco:OccupationRole ; \n"
    if row[0] != "":
        turtle_str += f'mdd:my-firstname "{row[0]}" ; \n'
    if row[1] != "":
        turtle_str += f'mdd:my-lastname "{row[1]}" ; \n'
    if row[2] != "":
        turtle_str += f'mdd:my-birthdate "{row[2]}"^^xsd:date ; \n'
    if row[3] != "":
        turtle_str += f'mdd:my-mailingstreet "{row[3]}" ; \n'
    if row[4] != "":
        turtle_str += f'mdd:my-mailingcity "{row[4]}" ; \n'
    if row[5] != "":
        turtle_str += f'mdd:my-mailingstate "{row[5]}" ; \n'
    if row[6] != "":
        turtle_str += f'mdd:my-mailingcountry "{row[6]}" ; \n'
    if row[7] != "":
        turtle_str += f'mdd:my-mailingpostcode "{row[7]}" ; \n'
    if row[8] != "":
        turtle_str += f'mdd:my-email "{row[8]}" ; \n'
    if row[9] != "":
        turtle_str += f'mdd:my-mobilephonenumber "{row[9]}" ; \n'
    if row[10] != "":
        turtle_str += f'mdd:my-homephonenumber "{row[10]}" . \n'
    if row[11] != "":
        turtle_str += f'\n cco:OccupationRole mdd:my-employeetitle "{row[11]}" ; \n'
    if row[12] != "":
        turtle_str += f'mdd:my-employername "{row[12]}" ; \n'
    if row[13] != "":
        turtle_str += f'mdd:my-employerindustry "{row[13]}" ; \n'
    if row[14] != "":
        turtle_str += f'mdd:my-employerstreet "{row[14]}" ; \n'
    if row[15] != "":
        turtle_str += f'mdd:my-employercity "{row[15]}" ;\n'
    if row[16] != "":
        turtle_str += f'mdd:my-employerstate "{row[16]}" ; \n'
    if row[17] != "":
        turtle_str += f'mdd:employerpostcode "{row[17]}" ; \n'
    if row[18] != "":
        turtle_str += f'mdd:employercountry "{row[18]}" ; \n'
    if row[19] != "":
        turtle_str += f'mdd:employerphone "{row[19]}" ; \n'
    if row[20] != "":
        turtle_str += f'mdd:employerfax "{row[20]}" .\n'
      
    turtle_str += "\n\n # END!"
    # print(turtle_str)

    return turtle_str