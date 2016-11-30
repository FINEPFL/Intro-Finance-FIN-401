from __future__ import division
from scipy.stats import linregress as lr

import numpy as np
import os
import io

def parser(filename):
    with open(filename, 'rb') as f:
        rows = f.readlines()[1:10]
        rows.pop(0)
        pre_price = 1
        Date = []
        r_risk = []
        SP500 = []
        for row in rows:
            try:
                date, _, _, _, stock_price, _, _, sp500 = row.strip().split(",")
                Date.append(date)
                SP500.append(float(sp500))
                r_risk.append(float(stock_price)/pre_price - 1)
                pre_price = float(stock_price)
                # print r_risk, SP500
            except BaseException:
                print 'skipping one line!'
        r_risk.pop(0)
        SP500.pop(0)

        return r_risk, SP500

ibm_r, SP500 = parser('ibm.csv')

slope, intercept, r_value, p_value, std_err = lr(SP500, ibm_r)
print slope, r_value
