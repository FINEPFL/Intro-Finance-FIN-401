import numpy as np
import matplotlib.pyplot as plt

class pushBgtConstr():
    def __init__(self, bankRate=0.2, iniVal=1):
        self.rate = bankRate
        self.oriCapital = iniVal
        self.oriYouthVal = np.linspace(0.0, 1.0, 10)

    def getOAValue(self, youthVal, capital):
        oldAgeValue = (1+self.rate)*capital - (1+self.rate)*youthVal
        return oldAgeValue

    def prjInvest(self, prjProfit):
        profitPV = prjProfit/(1 + self.rate)
        newCapital = self.oriCapital + profitPV
        newYouthVal = np.append(self.oriYouthVal, newCapital)
        self.demon(newYouthVal, newCapital)

    def demon(self, newYouthVal, newCapital):
        plt.plot(self.oriYouthVal, self.getOAValue(self.oriYouthVal, self.oriCapital))
        plt.plot(newYouthVal, self.getOAValue(newYouthVal, newCapital))
        plt.grid('on')
        plt.show()


if __name__ == '__main__':
    ele1 = pushBgtConstr()
    ele1.prjInvest(0.4)
