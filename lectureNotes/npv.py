import numpy as np
import matplotlib.pyplot as plt

class npvSampleBank():
    def __init__(self, givenRate=0.2, givenValue=1):
        self.givenRate = givenRate
        self.givenValue = givenValue

    def getOAValue(self, youthValue):
        # assuming there are only two phases: youth phase and old age phase
        oldAgeValue = 1.2 * (self.givenValue - youthValue)
        return oldAgeValue

    def demoBudgetCont(self):
        youthValue = np.linspace(0.0, 1.0, 10)
        oldAgeValue = []
        for value in youthValue:
            oldAgeValue.append(self.getOAValue(value))

        legdStr = 'Budget Constraint, rate=' + str(self.givenRate)
        plt.plot(youthValue, oldAgeValue,'k', label=legdStr)
        plt.xlabel('Consumption Youth')
        plt.ylabel('Consumption Old Age')
        plt.plot(0.5, self.getOAValue(0.5), 'go', label='(0.5, 0.6)')
        plt.grid('on')
        legend = plt.legend(loc='upper center', shadow=True)
        plt.show()

if __name__ == "__main__":
    bankOnly = npvSampleBank()
    bankOnly.demoBudgetCont()
