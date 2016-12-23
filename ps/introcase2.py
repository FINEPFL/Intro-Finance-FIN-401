from __future__ import division
import numpy as np

tao = 0.4409

def getDE(leverage):
    return leverage/(1-leverage)

def getRatioList(revenue_list):
    rev_sum = sum(revenue_list)
    return [x / rev_sum for x in revenue_list]

def getRelevedBeta(rawbeta, leverage, tarLev, revenue_list):
    DE_relev = getDE(tarLev)
    ratio_list = getRatioList(revenue_list)
    releved_beta_list = []

    for idx in xrange(len(rawbeta)):
        DE_raw = getDE(leverage[idx])
        beta_asset = rawbeta[idx]/(1 + DE_raw * (1 - tao))
        releved_beta_list.append(beta_asset * (1 + DE_relev * (1-tao)))
        print "rawbeta:", rawbeta[idx], "beta_asset:", beta_asset, "beta_releved:", beta_asset * (1 + DE_relev * (1-tao))
    # return beta_releved

    return np.asarray(ratio_list).dot(np.asarray(releved_beta_list))

if __name__ == "__main__":
    tarLev_Lodge = 0.74
    L_rawbeta_list = [0.76, 1.35, 0.89, 1.36]
    L_leverage_list = [0.14, 0.79, 0.69, 0.65]
    L_revenue_list = [0.77, 1.66, 0.17, 0.75]

    L_weighted_releved_beta = getRelevedBeta(L_rawbeta_list, L_leverage_list, tarLev_Lodge, L_revenue_list)
    print "Lodge weighted releveraged beta:", L_weighted_releved_beta

    tarLev_Lodge = 0.42
    R_rawbeta_list = [1.45, 1.45, 0.57, 0.76, 0.94, 1.32]
    R_leverage_list = [0.04, 0.1, 0.06, 0.01, 0.23, 0.21]
    R_revenue_list = [0.39, 0.57, 0.14, 0.23, 4.89, 1.05]

    R_weighted_releved_beta = getRelevedBeta(R_rawbeta_list, R_leverage_list, tarLev_Lodge, R_revenue_list)
    print "Restaurant weighted releveraged beta:", R_weighted_releved_beta
