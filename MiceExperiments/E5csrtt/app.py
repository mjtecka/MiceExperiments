from E5csrtt.mouse import Mouse
from E5csrtt.mouseSet import MouseSet
from E5csrtt.experimentSession import ExperimentSession
from E5csrtt.fiveChoicesSRTT import FiveChoicesSRTT

'''
Created on 30. 3. 2016

@author: blev
'''

if __name__ == '__main__':
    
    results1 = FiveChoicesSRTT()
#    results1.setCorrect([1,0,1,0,1])
    resultsArray = [1,0,1,0,1]
    results1.setCorrect(resultsArray)
    results2 = FiveChoicesSRTT()
    results2.setCorrect([1,0,0,0,0])
    results3 = FiveChoicesSRTT()
    results3.setCorrect([1,1,1,0,1])
    
    session1 = ExperimentSession("pokus1",results1,"1st july 2016");
    session2 = ExperimentSession("pokus2",results2,"2nd july 2016");
    session3 = ExperimentSession("pokus1",results3,"3rd july 2016");

    
    mys1 = Mouse("alois")
    mys1.addSession(session1)
    mys1.addSession(session2) 
    mys1.addSession(session3)

    mys2 = Mouse("cenda")
    mys2.addSession(session1)
    mys2.addSession(session3)
    
    testGroup = MouseSet()
    testGroup.addMouse(mys1)
    testGroup.addMouse(mys2)
    
    testGroup.removeMouse("alois")
    mys = testGroup.getMouse("cenda")
    
    print("Mouse identifier: " + mys.getIdentifier())
    print("Session types: " + str(mys.getSessionsKeys()))
    
    for key in mys.getSessionsKeys():
        sessionSet = mys.getSession(key)
        print ("experiment key: " + key)
        for sessionX in sessionSet :
            print("session date: " + str(sessionX.getSessionDate()))
            print("correct (sum): " + str(sessionX.getResults().getSumCorrect(0,20)) )
    
