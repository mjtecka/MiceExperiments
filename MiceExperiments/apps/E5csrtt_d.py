'''
Created on 1. 4. 2016

@author: mjtecka

Processes data from "5 Choice Serial Reaction Time Task (detailed)".
'''

import csv
from general.mouse import Mouse
from general.mouseSet import MouseSet
from E5csrtt_detailed.experimentSession import E5csrttExperimentSession
from E5csrtt_detailed.fiveChoicesSRTT import FiveChoicesSRTT

correctHeaders = []
incorrectHeaders = []
omissionHeaders = []

#inputFile="../data/sourceData/160205 side D detailed.csv"
#outputFile="../data/outputData/160205 side D detailed.csv"
inputFile="../data/sourceData/160205 side Ex detailed.csv"
outputFile="../data/outputData/160205 side Ex detailed.csv"


def createCorrectHeaders():
    for i in range(1,51) :
        header = "Trial Analysis - Correct (%s)" % i 
        correctHeaders.append(header)
    return 1

def createIncorrectHeaders():
    for i in range(1,51) :
        header = "Trial Analysis - Incorrect (%s)" % i 
        incorrectHeaders.append(header)
    return 1

def createOmissionHeaders():
    for i in range(1,51) :
        header = "Trial Analysis - Omission (%s)" % i 
        omissionHeaders.append(header)
    return 1


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
    createCorrectHeaders()
    createIncorrectHeaders()
    createOmissionHeaders()
    
    testGroup = MouseSet()
    
    with open(inputFile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
      
            #read data from row
            nameCsv = row['Animal ID']
            dateCsv = row['Schedule run date']
            scheduleNameCsv = normalizeScheduleName(row['Schedule name'])

            correctCsv = []            
            for ch in correctHeaders:
                correctCsv.append(int(row[ch]))
            print(correctCsv)
            
            incorrectCsv = []            
            for ih in incorrectHeaders:
                incorrectCsv.append(int(row[ih]))
            print(incorrectCsv)

            omissionCsv = []
            for oh in omissionHeaders:
                omissionCsv.append(int(row[oh]))
            
            #get mouse name, add to mouse set           
            m = testGroup.getMouse(nameCsv)
            if m == None :
                m = Mouse(nameCsv)
                            
            #create results sets, set data 
            results = FiveChoicesSRTT()
            results.setCorrect(correctCsv)
            results.setIncorrect(incorrectCsv)
            results.setOmission(omissionCsv)
            
            
            #create experiment session
            s = E5csrttExperimentSession(scheduleNameCsv,results,dateCsv)
                        
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
                print("correct (sum): " + str(sessionX.getResults().getSumCorrect(0,51)) )
                print("incorrect (sum): " + str(sessionX.getResults().getSumIncorrect(0,51)) )
                print("omission (sum): " + str(sessionX.getResults().getSumOmission(0,51)) )
                print ("counted correct (by 10): " + str(sessionX.getResults().getCorrect50by10()))

def doIt(inputFile,outputFile):
    testGroup = processDataFromCsv()
    
    csvKeys = ['Animal ID', "Schedule Name","Session Date", "Correct 1-10", "Correct 11-20", "Correct 21-30", "Correct 31-40", "Correct 41-50","Incorrect 1-10","Incorrect 11-20", "Incorrect 21-30", "Incorrect 31-40", "Incorrect 41-50", "Omission 1-10", "Omission 11-20", "Omission 21-30", "Omission 31-40", "Omission 41-50"]
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
                
                countCorrect = sessionX.getResults().getCorrect50by10()                
                mouseDict['Correct 1-10'] = countCorrect[0]
                mouseDict['Correct 11-20'] = countCorrect[1]
                mouseDict['Correct 21-30'] = countCorrect[2]
                mouseDict['Correct 31-40'] = countCorrect[3]
                mouseDict['Correct 41-50'] = countCorrect[4]
                
                countIncorrect = sessionX.getResults().getIncorrect50by10()                
                mouseDict['Incorrect 1-10'] = countIncorrect[0]
                mouseDict['Incorrect 11-20'] = countIncorrect[1]
                mouseDict['Incorrect 21-30'] = countIncorrect[2]
                mouseDict['Incorrect 31-40'] = countIncorrect[3]
                mouseDict['Incorrect 41-50'] = countIncorrect[4]
                
                countOmission = sessionX.getResults().getOmission50by10() 
                mouseDict['Omission 1-10'] =  countOmission[0]
                mouseDict['Omission 11-20'] = countOmission[1]
                mouseDict['Omission 21-30'] = countOmission[2]
                mouseDict['Omission 31-40'] = countOmission[3]
                mouseDict['Omission 41-50'] = countOmission[4]

                with open(outputFile, 'a') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csvKeys,extrasaction='ignore')        
                    writer.writerow(mouseDict)
            

if __name__ == '__main__':
    doIt(inputFile,outputFile)
    
    #testIt()
    
    
    