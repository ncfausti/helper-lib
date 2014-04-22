def getLocationsByPatientId():
    cnx = mysql.connector.connect(user='root', database='cgi_ontology')
    for i in range(len(patIds)):
        q = "select BOX, POSITION, SAMPLETYPE FROM `radr_samples` where PATIENT_ID like '{}'".format(patIds[i])
        with open('bmi_results.csv', 'a') as f:
            #f.write('{},{},'.format(patIds[i], bmis[i]))
            cursor = cnx.cursor()
            cursor.execute(q)
            for(box, position, sampletype) in cursor:
                f.write("{},{},{},{},{}\n".format(patIds[i], bmis[i],box, position, sampletype))
    cnx.close()
