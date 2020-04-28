# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:33:46 2020

@author: cheng
"""

import docx2txt
import re
import pandas as pd
import os

result = docx2txt.process("CtoARubric-O'Grady&Sot.docx")
name = re.search('^\S*',result).group(0)
score = re.findall('_\d+_',result)
score_df=pd.DataFrame(score)
score_df = score_df[0].str.replace('_','')
score_df_t = pd.DataFrame()

result = docx2txt.process("CtoARubric-Crismon et al.docx")
name = re.search('^\S*',result).group(0)
score = re.findall('_\d+_',result)
score_df=pd.DataFrame(score)
score_df = score_df[0].str.replace('_','')
score_df_t=pd.concat([score_df_t, score_df],axis=1, ignore_index=True)

###test is right and try to put into a for loop
names=[]
score_df_t = pd.DataFrame()
file_list = os.listdir()
for file_name in file_list:
    result = docx2txt.process(file_name)
    name = re.search('^\S*',result).group(0)
    names.append(name)
    score = re.findall('_\d+_',result)
    score_df=pd.DataFrame(score)
    score_df = score_df[0].str.replace('_','')
    score_df_t=pd.concat([score_df_t, score_df],axis=1, ignore_index=True)

score_df_t.columns=names 
score_df_tran=score_df_t.T
score_df_tran.columns=['3a','3b','5a','5b','5b_som','3a_cl','total']
score_df_tran=score_df_tran.astype(int)
#3a problem
score_df_tran['3a-Problem']=1
score_df_tran['3a-Problem'].values[score_df_tran['3a'] >=17] = 5
score_df_tran['3a-Problem'].values[(score_df_tran['3a'] < 17) & (score_df_tran['3a']>=14)] = 4
score_df_tran['3a-Problem'].values[(score_df_tran['3a'] < 14) & (score_df_tran['3a']>=11)] = 3
score_df_tran['3a-Problem'].values[(score_df_tran['3a'] < 11) & (score_df_tran['3a']>=7)] = 2
#3b-Factsheet
score_df_tran['3b-Factsheet']=1
score_df_tran['3b-Factsheet'].values[score_df_tran['3b'] >=17] = 5
score_df_tran['3b-Factsheet'].values[(score_df_tran['3b'] < 17) & (score_df_tran['3b']>=14)] = 4
score_df_tran['3b-Factsheet'].values[(score_df_tran['3b'] < 14) & (score_df_tran['3b']>=11)] = 3
score_df_tran['3b-Factsheet'].values[(score_df_tran['3b'] < 11) & (score_df_tran['3b']>=7)] = 2  
#5a-Letter
score_df_tran['5a-Letter']=1
score_df_tran['5a-Letter'].values[score_df_tran['5a'] >=21] = 5
score_df_tran['5a-Letter'].values[(score_df_tran['5a'] < 21) & (score_df_tran['5a']>=16)] = 4
score_df_tran['5a-Letter'].values[(score_df_tran['5a'] < 16) & (score_df_tran['5a']>=11)] = 3
score_df_tran['5a-Letter'].values[(score_df_tran['5a'] < 11) & (score_df_tran['5a']>=6)] = 2      
#5b-Press Release
score_df_tran['5b-Press Release']=1
score_df_tran['5b-Press Release'].values[score_df_tran['5b'] >=21] = 5
score_df_tran['5b-Press Release'].values[(score_df_tran['5b'] < 21) & (score_df_tran['5b']>=16)] = 4
score_df_tran['5b-Press Release'].values[(score_df_tran['5b'] < 16) & (score_df_tran['5b']>=11)] = 3
score_df_tran['5b-Press Release'].values[(score_df_tran['5b'] < 11) & (score_df_tran['5b']>=6)] = 2    

#5b-Social media
score_df_tran['5b-Social media']=1
score_df_tran['5b-Social media'].values[score_df_tran['5b_som'] >=17] = 5
score_df_tran['5b-Social media'].values[(score_df_tran['5b_som'] < 17) & (score_df_tran['5b_som']>=14)] = 4
score_df_tran['5b-Social media'].values[(score_df_tran['5b_som'] < 14) & (score_df_tran['5b_som']>=11)] = 3
score_df_tran['5b-Social media'].values[(score_df_tran['5b_som'] < 11) & (score_df_tran['5b_som']>=7)] = 2

#3a-Client
score_df_tran['3a-Client']=1
score_df_tran['3a-Client'].values[score_df_tran['3a_cl'] >=9] = 5
score_df_tran['3a-Client'].values[(score_df_tran['3a_cl'] < 9) & (score_df_tran['3a_cl']>=7)] = 4
score_df_tran['3a-Client'].values[(score_df_tran['3a_cl'] < 7) & (score_df_tran['3a_cl']>=5)] = 3
score_df_tran['3a-Client'].values[(score_df_tran['3a_cl'] < 5) & (score_df_tran['3a_cl']>=3)] = 2     
    

