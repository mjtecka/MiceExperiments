'''
Created on 30. 3. 2016

@author: mjtecka
'''

from general.experimentSessionAbstract import ExperimentSession
from E5csrtt_detailed.fiveChoicesSRTT import FiveChoicesSRTT


class E5csrttExperimentSession(ExperimentSession):
    '''
    Experiment session for "5 Choice Serial Reaction Time Task (detailed)"
    includes sessionType (some parameters can be different for given task), sessionDate and results
    '''

    results = FiveChoicesSRTT()

    def __init__(self, sessionType, results, sessionDate):
        self.sessionType=sessionType
        self.results=results
        self.sessionDate = sessionDate
     
    def getSessionDate(self):
        return self.sessionDate
       
        
    def getType(self):
        return self.sessionType
    
    def getResults(self):
        return self.results