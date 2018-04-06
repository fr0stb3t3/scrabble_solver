# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 18:48:02 2018

@author: Frostbete

"""

f = open('scrabble_dictionary.txt' , 'r')

py_dic = {}
for word in f:
    py_dic[word.strip()] = 1

if 'ADMINISTRATIVE' in py_dic:
    print('true')
else:
    print('false')
