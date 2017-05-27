# -*- coding: utf-8 -*-
"""
Created on Sun May 28 00:34:22 2017

@author: ChunJi
"""

import jieba
import pandas as pd
import jieba.posseg as pseg

dic = pd.read_table('dict.txt',sep=' ',header=None)
dic = list(dic[0]) 
diary = pd.read_table('diary.txt',encoding = 'utf-8')

name = []
for i in range(0,len(diary)):
    text = diary['Content '][i]
    result3 = list(pseg.cut(text))
    name_candi = []
    for word, flag in result3:
        if('ns' in flag):  #people 'nr'   place 'ns'
            name_candi.append(word)
            
    for j in range(0,len(name_candi)):
        if(name_candi[j] not in dic):
            name.append(name_candi[j])
            
name_set = list(set(name))
del_idx = []
for i in range(0,len(name_set)):
    if(len(name_set[i])==1):
        del_idx.append(i)

for i in range(0,len(del_idx)):
    del name_set[del_idx[i] - i]
    

import csv
savename = 'place.csv'
predict1 = zip(list(map(str,name_set)))
with open(savename,'w',newline='') as f:
    writer = csv.writer(f, delimiter =',')
    writer.writerows(predict1)
    

p = pd.read_csv('place.csv',header=None,encoding = 'utf-8')
n = pd.read_csv('names.csv',header=None,encoding = 'utf-8')
