from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt

class pushBgtConstr():
    ''' These codes are intent to show how we can maximise net present value (NPV).
    The implicit assumptions is that there are only two time phases and there is a
    bank that allows people to map the value of money between now and then.
    The principle is that when the rate of return of project is smaller than rate
    of bank, stop investing. In addition, it is assumed that the investments are
    not decided by preferences.
    '''
    def __init__(self, bankRate=0.2, iniVal=1, prjRateList=[.5, .4, .3, .2, .1]
                                    , prjCostList=[.01, .05, .1, .15, .2]):
        ''' Initialing parameters.
        prjRateList contains rate of return of different proposed investing prjs.
        prjCostList contains corresponding cost of prjs.
        '''
        self.bankRate = bankRate
        self.prjRateList = prjRateList
        self.prjCostList = prjCostList
        self.iniVal = iniVal

    def getOAVbank(self, sumCurrent):
        ''' It is the bank that allows you to manipulate the money '''
        OAVbank = (1 + self.bankRate) * sumCurrent
        return OAVbank

    def getOAVprj(self):
        ''' we do prjs whose rate of return is larger than that of the bank'''
        info = np.asarray([self.prjRateList, self.prjCostList]).T
        info = np.asarray(sorted(info, key=lambda rateList: rateList[0],
                                                    reverse=True))
        returnPrjOA = 0
        returnCombined = 0
        currentValYA = self.iniVal
        investments = 0

        for i in xrange(0, info.shape[0]):
            if info[i][0] >= self.bankRate:
                returnPrjOA = returnPrjOA + (info[i][0]+1)*info[i][1]
                currentValYA = currentValYA - info[i][1]
                returnCombined = returnPrjOA
                investments = investments + info[i][1]
            else:
                returnCombined = returnCombined + (self.bankRate+1) * currentValYA
                break

        self.returnCombined = returnCombined
        self.returnPrjOA = returnPrjOA
        self.amountOfInvestment = investments

if __name__ == '__main__':
    ele1 = pushBgtConstr()
    ele1.getOAVprj()
    print ("The combined (maximised) NPV is: ", ele1.returnCombined)
    print ("The amount of return from project is: ", ele1.returnPrjOA)
    print ("The amount of investments is: ", ele1.amountOfInvestment)
