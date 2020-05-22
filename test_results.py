# -*- coding: utf-8 -*-
"""
Created on Tue May 19 20:52:50 2020

@author: vignesh
"""

import pandas as pd
import numpy as np

def score(df, promo_pred_col = 'Discount'):
    n_treat       = df.loc[df[promo_pred_col] == 1,:].shape[0]
    n_control     = df.loc[df[promo_pred_col] == 0,:].shape[0]
    n_treat_purch = df.loc[df[promo_pred_col] == 1, 'Response'].sum()
    n_ctrl_purch  = df.loc[df[promo_pred_col] == 0, 'Response'].sum()
    nir = 11*n_treat_purch - 3 * n_treat + 11*n_ctrl_purch
    return (nir)

def test_results(promotion_strategy):
    test_data = pd.read_csv('test.csv')
    df = test_data[['AcceptedCmp1','AcceptedCmp2','AcceptedCmp3','AcceptedCmp4','AcceptedCmp5','Income','Recency','NumWebVisitsMonth']]
    promos = promotion_strategy(df)
    score_df = test_data.iloc[np.where(promos == 1)]    
    nir= score(score_df)
    print()
    print('Your Revenue generated with this strategy is {:0.2f}.'.format(nir))
    print()
    return nir

# added this function to test our irr and nlr on the validation set
def valid_results(promotion_strategy, valid_data):
    df = valid_data[['AcceptedCmp1','AcceptedCmp2','AcceptedCmp3','AcceptedCmp4','AcceptedCmp5','Income','Recency','NumWebVisitsMonth']]
    promos = promotion_strategy(df)
    score_df = valid_data.iloc[np.where(promos == 1)]    
    nir = score(score_df)
    print()
    print('Your Revenue generated with this strategy is {:0.2f}.'.format(nir))
    print()
    return nir