'''
Created on 30. 3. 2016

@author: blev
'''

class MouseSet:
    '''
    classdocs
    '''
    #set of mice - set of Mouse
    mouseSet = set()

    def __init__(self):
        '''
        Constructor
        '''
    
    def __iter__(self):
        return self.mouseSet.__iter__()
    
    def __next__(self):
        self.mouseSet().__next__()

    
    def addMouse(self,mouse):
        self.mouseSet.add(mouse)
    
    def getMouse(self,identifier):
        for m in self.mouseSet:
            if m.getIdentifier() == identifier:
                return m 
        return
    
    def removeMouse(self,identifier):
        for m in self.mouseSet:
            if m.getIdentifier() == identifier:
                self.mouseSet.discard(m)
                return True
        return False
    
        