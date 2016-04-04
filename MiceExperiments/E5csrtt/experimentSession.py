'''
Created on 30. 3. 2016

@author: blev
'''
from E5csrtt.fiveChoicesSRTT import FiveChoicesSRTT

class ExperimentSession:
    '''
    classdocs
    '''

    #date - date
    #varianta [string - enum]
    #results - five choices
    results = FiveChoicesSRTT()

    def __init__(self, sessionType, results, sessionDate):
        '''
        Constructor
        '''
        self.sessionType=sessionType
        self.results=results
        self.sessionDate = sessionDate
     
    def getSessionDate(self):
        return self.sessionDate
       
        
    def getType(self):
        return self.sessionType
    
    def getResults(self):
        return self.results