'''
Created on 30. 3. 2016

@author: blev
'''
from E5csrtt.experimentSession import ExperimentSession 

class Mouse:
    '''
    classdocs
    '''
    #id
    #list of experiments

    def __init__(self, identifier):
        '''
        Constructor
        '''
        self.identifier = identifier
        self.sessions = dict()
    
    def getIdentifier(self):
        return self.identifier

    def addSession(self, ExperimentSession):
        sessionKey = ExperimentSession.getType()
        try:
            self.sessions[sessionKey].add(ExperimentSession)
        except KeyError:
            self.sessions[sessionKey]=set()
            self.sessions[sessionKey].add(ExperimentSession)

        
    def getSessionsKeys(self):
        sessionKeys =[]
        for k in self.sessions.keys():
            sessionKeys.append(k)
        return sessionKeys
    
    def getSession(self,key):
        return self.sessions[key]