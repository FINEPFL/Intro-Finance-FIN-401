from __future__ import division
from scipy.stats import linregress as lr
from matplotlib import pyplot as plt

import numpy as np
import os
import io

def parser(filename):
    with open(filename, 'rb') as f:
        rows = f.readlines()
        rows.pop(0)
        pre_price = 1
        pre_rm = 1
        r_risk = []
        rm_rate = []
        for row in rows:
            try:
                date, _, _, _, stock_price, _, _, r_m = row.strip().split(",")

                rm_rate.append(float(r_m)/pre_rm - 1)
                r_risk.append(float(stock_price)/pre_price - 1)

                pre_price = float(stock_price)
                pre_rm = float(r_m)

            except BaseException:
                print 'skipping one line!'

        r_risk.pop(0)
        rm_rate.pop(0)
        return r_risk, rm_rate

ibm_r, SP500_rate = parser('ibm.csv')
us_risk_free_rate = 0.77/365
SP500_rate[:] = [x * 100 - us_risk_free_rate for x in SP500_rate]
ibm_r[:] = [x * 100 - us_risk_free_rate for x in ibm_r]

slope_us, intercept_us, _, _, _ = lr(SP500_rate, ibm_r)
print slope_us, intercept_us
print np.cov(SP500_rate, ibm_r)[1,1]/np.var(SP500_rate)

swisscom_r, SMI_rate = parser('swisscom.csv')
swiss_risk_free_rate = -0.8
SMI_rate[:] = [x * 100 - swiss_risk_free_rate for x in SMI_rate]
swisscom_r[:] = [x * 100 - us_risk_free_rate for x in swisscom_r]

slope_swi, intercept_swi, _, _, _ = lr(SMI_rate, swisscom_r)
print slope_swi, intercept_swi
print np.cov(SMI_rate, swisscom_r)[1,1]/np.var(SMI_rate)




#
