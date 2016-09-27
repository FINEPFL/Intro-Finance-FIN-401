import numpy as np
import matplotlib.pyplot as plt

class npvBankOnly():
    def __init__(self, givenRate=0.2, givenValue=1.0):
        self.givenRate = givenRate
        self.givenValue = givenValue

    def getOAValue(self, youthValue):
        '''
        Calculating future (old age here) value, given present value (PV).
        assuming there are only two phases: youth phase and old age phase
        and the bank is the only oppertunity for this person to mainipulate
        his money. The line functions as mapping the value of money between now
        and future (old age here).
        '''
        oldAgeValue = (1.0 + self.givenRate) * (self.givenValue - youthValue)
        return oldAgeValue

    def demoBudgetCont(self):
        youthValue = np.linspace(0.0, self.givenValue, 10)
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
    bankOnly = npvBankOnly()
    bankOnly.demoBudgetCont()
