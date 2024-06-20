def transformation_matrix(turtle_list):
    turtle_str = f""
    mdd = "PREFIX mdd: <https://dictionary.mydata.org/#>"
    xsd = "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>"
    rdf = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>"
    cco = "PREFIX cco: <http://www.ontologyrepository.com/CommonCoreOntologies/>"
    pop = "PREFIX pop: <https://opensource.ieee.org/person-ontology-group/person-ontology-project/-/blob/master/dev/Person-Ontology-dev.ttl->"
    
    turtle_str += f"{mdd} \n{xsd} \n{rdf} \n{cco} \n{pop} \n"

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