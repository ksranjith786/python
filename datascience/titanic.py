# -*- coding: utf-8 -*-


import pandas as pd
titf = pd.read_csv('http://bit.ly/kaggletrain')

titf.to_csv(path_or_buf='./titanic.csv')