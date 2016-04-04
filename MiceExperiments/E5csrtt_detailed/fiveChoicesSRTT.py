'''
Created on 30. 3. 2016

@author: mjtecka
'''

class FiveChoicesSRTT(object):
    '''
    "5 Choice Serial Reaction Time Task (detailed)" - test results
    '''
    correct = []
    incorrect = []
    omissions = []


    def __init__(self):
        '''
        Constructor
        '''
        
# set array
# reset array
# sumSubArray

#--------CORRECT----------
    def setCorrect(self,correct):
        self.correct = correct
        
    def resetCorrect(self):
        self.correct = []
        
    def getSumCorrect(self,rangeFrom, rangeTo):
        index = rangeFrom
        count = 0
        myArray = self.correct[rangeFrom:rangeTo]
        for i in myArray :
            if i == 1:
                count = count +1
            index = index +1
        return count

    def getCorrect50by10(self):
        result = []
        counter  = 0; 
        while (counter < 50) :
            result.append(self.getSumCorrect(counter, counter+10))
            counter=counter+10
        return result

#--------INCORRECT----------
    def setIncorrect(self,incorrect):
        self.incorrect = incorrect
        
    def resetIncorrect(self):
        self.incorrect = []
        
    def getSumIncorrect(self,rangeFrom, rangeTo):
        index = rangeFrom
        count = 0
        myArray = self.incorrect[rangeFrom:rangeTo]
        for i in myArray :
            if i == 1:
                count = count +1
            index = index +1
        return count

    def getIncorrect50by10(self):
        result = []
        counter  = 0; 
        while (counter < 50) :
            result.append(self.getSumIncorrect(counter, counter+10))
            counter=counter+10
        return result

#----------OMISSION-----------
    def setOmission(self,omissions):
        self.omissions = omissions
        
    def resetOmission(self):
        self.omissions = []
        
    def getSumOmission(self,rangeFrom, rangeTo):
        index = rangeFrom
        count = 0
        myArray = self.omissions[rangeFrom:rangeTo]
        for i in myArray :
            if i == 1:
                count = count +1
            index = index +1
        return count
 
    def getOmission50by10(self):
        result = []
        counter  = 0; 
        while (counter < 50) :
            result.append(self.getSumOmission(counter, counter+10))
            counter=counter+10
        return result        
