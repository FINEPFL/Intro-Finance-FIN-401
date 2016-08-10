import numpy as np
import matplotlib.pyplot as plt

class npvSample():
    def __init__(self, givenRate=0.2, givenValue=1):
        self.rate = givenRate
        self.givenValue = givenValue

    def getOAValue(self, youthValue):
        oldAgeValue = 1.2 * (self.givenValue - youthValue)
        return oldAgeValue

    def demoBudgetCont(self):
        youthValue = np.linspace(0.0, 1.0, 10)
        oldAgeValue = []
        for value in youthValue:
            oldAgeValue.append(self.getOAValue(value))

        legdStr = 'Budget Constraint, rate=' + str(self.rate)
        plt.plot(youthValue, oldAgeValue,'k', label=legdStr)
        plt.xlabel('Consumption Youth')
        plt.ylabel('Consumption Old Age')
        plt.plot(0.5, self.getOAValue(0.5), 'go', label='(0.5, 0.6)')
        plt.grid('on')
        legend = plt.legend(loc='upper center', shadow=True)
        plt.show()

if __name__ == "__main__":
    sample1 = npvSample()
    sample1.demoBudgetCont()
