import numpy as np

class calIRR():
    def __init__(self, cashFlows):

        self.costList = np.asarray(cashFlows)
        self.irr = -0.1

    def calculator(self):
        tryDCF = 0.0
        tryList = np.linspace(0.01, 50, 5000000)
        costListLen = len(self.costList)
        for i in xrange(0, len(tryList)):
            for j in xrange(0, costListLen):
                tryDCF = tryDCF + self.costList[j]/((tryList[i]+1.0)**j)
            if(abs(tryDCF - 0.0) < 0.1):
                self.irr = tryList[i]
                break
            tryDCF = 0.0
        print self.irr

if __name__ == '__main__':
    obj1 = calIRR([-1000, 1250, 1700 , -2000])
    obj1.calculator()
