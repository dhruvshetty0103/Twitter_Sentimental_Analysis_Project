# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 11:11:48 2020

@author: Dhruv Shetty
"""

import pandas as pd

dataframe=pd.read_csv("unlockone 2.8k.csv", header=None)
dataframe=dataframe[0]
dataframe.to_csv("ready_unlockone 2.8k.csv", index=False, float_format='{:f}', header=None)