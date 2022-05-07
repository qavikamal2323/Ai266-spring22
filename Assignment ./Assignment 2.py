# -*- coding: utf-8 -*-
"""
Created on Sat May  7 12:28:31 2022
@author: Ashar khan

"""
import pandas as pd
import numpy as np
#Read CSV File  
test_data_frame = pd.read_csv('C:\\Users\\Ashar khan\\Desktop\\test.csv');

#Get just single column name 'id' in CSV file
id_data_frame = test_data_frame[['id']];

#Insert Column name 'target' in CSV file on index 1
id_data_frame.insert(1,"target",0);

#Generated random number probability in each row id 
id_data_frame['target'] = np.random.rand(700000,1)

#Save this CSV file on Desktop 
id_data_frame.to_csv('C:\\Users\\Ashar khan\\Desktop\\out.csv',index=False);