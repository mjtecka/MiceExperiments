'''
Created on 4. 4. 2016

@author: mjtecka
'''
import abc

class ExperimentSession:
    __metaclass__ = abc.ABCMeta


    def __init__(self, sessionType, results, sessionDate):
        self.sessionType = sessionType
        self.results = results
        self.sessionDate = sessionDate
        return

    def getSessionDate(self):
        return self.sessionDate
          
    def getType(self):
        return self.sessionType

    def getResults(self):
        return self.results