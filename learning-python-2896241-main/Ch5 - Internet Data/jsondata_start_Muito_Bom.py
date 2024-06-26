# 
# Example file for parsing and processing JSON
# LinkedIn Learning Python course by Joe Marini
#

import urllib.request
import json
from datetime import datetime
from datetime import date

def printResults(data,spec_date):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)
    
    # now we can access the contents of the JSON like any other Python object

    
    # Test 1 - output the number of events, plus the magnitude and each event name  
    #key_word="id"
    #cont=0
    #cont=sum(1 for obj in theJSON if key_word in obj)
    #print(cont," events recorded")
    
    # for each event, print the place where it occurred

    str1=set()

    for obj in theJSON:

        #Test 2
        #print(obj["titulo"]," \n")

        #date_hour=(datetime.strptime(obj["fim_execucao"],"%Y-%m-%d")).date()
        #if date_hour > spec_date:
        #    print(obj["titulo"],"\n",obj["foco_tecnologico"],"\n\n")
        
        #Test 3 - must use the for loop from Test 2
        str1.add(obj["foco_tecnologico"])
    
    cont2=0
    dict1={"Foco_Tecnologico":"Numero de projetos"}
    for element1 in str1:
        cont1=0
        for obj in theJSON:
            if element1==obj["foco_tecnologico"]:
                cont1+=1
        dict1.update({element1:cont1})
        cont2+=cont1
    
    #print(cont2) #Just to compare with the output of test 1



    # print the events that only have a magnitude greater than 4


    # print only the events where at least 1 person reported feeling something

  
def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    #urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    urlData = "https://dados.ifrn.edu.br/dataset/c62bdea1-7880-4a31-84a0-481472066373/resource/a46d370b-d9a9-497d-a58c-5b5b399f960d/download/dados_extraidos_recursos_projetos-de-extensao.json"

    # Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print ("result code: " + str(webUrl.getcode()))
    specific_date=date(2019,12,1)
    if (webUrl.getcode()==200):
        data = webUrl.read()
        printResults(data,specific_date)
    else:
        print("ERROR", webUrl.getcode())

if __name__ == "__main__":
    main()
