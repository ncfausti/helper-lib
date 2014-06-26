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




### Update column on multiple rows in a database with some transformed value from another column

#get list of values that you might want to use as a base to update

cnx = mysql.connector.connect(user='root', database='cgi_ontology')
cursor = cnx.cursor()
q = "select DATE_OF_BIRTH, DATE_OF_BIRTH2 from `radr_baseline`"
cursor.execute(q)

#store values returned in a list
oldDateList = []
for (oldDate, somethingElse) in cursor:
    oldDateList.append(oldDate)


def updateRowsExample():
    #create connection
    cnx = mysql.connector.connect(user='root', database='cgi_ontology')
    #set cursor
    cursor = cnx.cursor()

    # iterate through each item in local list and update each row in the database
    for oldDate in oldDateList:
        if not (oldDate == ""):
            newYear = "19" + oldDate[-2:]
            newDate = oldDate[:-2] + newYear
            q = "UPDATE `radr_baseline` SET DATE_OF_BIRTH2=STR_TO_DATE('"+ newDate + "', '%d-%M-%Y') WHERE DATE_OF_BIRTH like '"+oldDate+"';"
            cursor.execute(q)