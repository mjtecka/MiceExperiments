'''
Created on 4. 4. 2016

@author: mjtecka
'''
import abc

class ExperimentSession:
    __metaclass__ = abc.ABCMeta

    def __init__(self, sessionType, results, sessionDate):
        return

    @abc.abstractclassmethod
    def getSessionDate(self):
        return       
    
    @abc.abstractclassmethod    
    def getType(self):
        return 

    @abc.abstractclassmethod
    def getResults(self):
        return 