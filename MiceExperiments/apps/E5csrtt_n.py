'''
Created on 4. 4. 2016

@author: mjtecka
'''

import csv
from general.mouse import Mouse
from general.mouseSet import MouseSet
from general.experimentSessionAbstract import ExperimentSession


resultHeaders = []

inputFile="../data/sourceData/160215 side D normal.csv"
outputFile="../data/outputData/160215 side D normal.csv"

def createHeaders():
    
    #we want to use all from CSV headers (we don't need to know them)... 
    with open(inputFile) as csvfile:
            reader = csv.DictReader(csvfile)
            headers = reader.fieldnames.copy()
    
    #... except 3 which are removed        
    headers.remove("Animal ID")
    headers.remove("Schedule run date")
    headers.remove("Schedule name")
    resultHeaders.extend(headers)
        

def normalizeScheduleName(name):
    #correct - new - values
    if name in ['5CSRTT_1000ms_var1', '5CSRTT_1500ms_Var1'] :
        return name
    #old values
    if name in ['5CSRTT_600ms_var1',"5CSRTT_06_var1"] :
        return "5CSRTT_0600ms_var1"
    if name in ['5CSRTT_800ms_var1',"5CSRTT_08_var1"] :
        return "5CSRTT_0800ms_var1"
    if name == "5CSRTT_1s_var1" :
        return "5CSRTT_1000ms_var1"
    if name == "5CSRTT_1,5_Var1" :
        return "5CSRTT_1500ms_Var1"


def processDataFromCsv():
    createHeaders()
    
    testGroup = MouseSet()
    
    with open(inputFile) as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
      
            #read data from row
            nameCsv = row['Animal ID']
            dateCsv = row['Schedule run date']
            scheduleNameCsv = normalizeScheduleName(row['Schedule name'])

            resultsCsv = []
            for x in resultHeaders:
                resultsCsv.append(str(row[x]))
            
            #get mouse name, add to mouse set           
            m = testGroup.getMouse(nameCsv)
            if m == None :
                m = Mouse(nameCsv)
                            
            #create results sets, set data 
            ## no need to process data in this case
            
            #create experiment session
            s = ExperimentSession(scheduleNameCsv,resultsCsv,dateCsv)
          
            #add session to mouse
            m.addSession(s)
            testGroup.addMouse(m)
    
    return testGroup

def testIt():
    testGroup = processDataFromCsv()
          
    for m in testGroup :
        print("\n-------------------------------\n")
        print("Mouse identifier: " + m.getIdentifier())
        print("Session types: " + str(m.getSessionsKeys()))
    
        for key in sorted(m.getSessionsKeys()) :
            sessionSet = m.getSession(key)
            print ("experiment key: " + key)
            for sessionX in sessionSet :
                print("session date: " + str(sessionX.getSessionDate()))
                print("session results: " + str(sessionX.getResults()))


def doIt(outputFile):
    testGroup = processDataFromCsv()
    
    csvKeys = ['Animal ID', "Schedule Name","Session Date"] + resultHeaders
    print("csvKeys:" + str(csvKeys))
    
    with open(outputFile, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csvKeys,extrasaction='ignore')        
        writer.writeheader()          
    
    for m in testGroup :
        mouseId = m.getIdentifier()
        mouseDict = {}
   
        for key in sorted(m.getSessionsKeys()) :
            sessionSet = m.getSession(key)
            mouseDict['Animal ID'] = mouseId
            mouseDict['Schedule Name'] = key
            print ("experiment key: " + mouseId + " " +key)
            
            for sessionX in sessionSet :
                mouseDict['Session Date'] = str(sessionX.getSessionDate())
                resultSet = sessionX.getResults()
       
                for idx,val in enumerate(resultHeaders):
                    mouseDict[val] = resultSet[idx]
            
                with open(outputFile, 'a') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csvKeys,extrasaction='ignore')        
                    writer.writerow(mouseDict)




if __name__ == '__main__':
    testIt()
     
#   doIt()