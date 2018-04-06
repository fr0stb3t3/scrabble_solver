# -*- coding: utf-8 -*-
import heapq
from Train import Train
"""
Created on Mon Nov 27 16:57:08 2017

@author: Frostbete
"""

# making the dictionary of all words allowed in scrabble

f = open('scrabble_dict.txt' , 'r')

py_dic = {}
for word in f:
    py_dic[word.strip()] = 1
#####
    
    
# making a dictionary of letters and their corresponding values
letter_dic = {}
letter_dic =  dict.fromkeys(['a','e','i','o','u','l','n','s','t','r'] , 1)
letter_dic.update(dict.fromkeys(['d','g'],2))
letter_dic.update(dict.fromkeys(['b','c','m','p'],3))
letter_dic.update(dict.fromkeys(['f','h','v','w','y'],4))
letter_dic.update(dict.fromkeys(['k'],5))
letter_dic.update(dict.fromkeys(['j','x'],8))
letter_dic.update(dict.fromkeys(['q','z'],10))
letter_dic.update(dict.fromkeys(['*a','*b','*c','*d','*e','*f','*g','*h','*i','*j','*k','*l','*m','*n','*o','*p','*q','*r','*s','*t','*u','*v','*w','*x','*y','*z'],0))

def scrabbled_gegs(array, fixed_spacing = None ,max_len = False, starting_string = ''): #scrabbled , scrmabled eggs -- pun. ye
    """
    fixed_spacing parameter needs to be in the format of 
        [[a1 , a2, a3.. , aN] , [n1 , n2, n3 ..n(N-1)]]
        where the space between a1, a2 = n1 , a2,a3 = n2 ... , a(N-1),aN = n(N-1)
    """
    array_start = []
    return_array = []
    
    for letter in array:
        array_start.append([[letter] , [not_letter for not_letter in array if not_letter != letter]])
        return_array.append([letter])
   
    def recursive_scrabbled_gegs(arr, ret_arr):
        
        if arr[0][1] == []:
            return 
        
        new_array = []
        for elem_lvl1 in arr:  
            
            for a in elem_lvl1[1]:
                 
                 elem_copy = elem_lvl1[0][:]
                 arr_copy = elem_lvl1[1][:]
                 
                 elem_copy.append(a)
                 new_elem = elem_copy
                 
                 # code modification
                 ######
                 # using train dataType for fixed spacing shit
                 if fixed_spacing and fixed_spacing != []:
                         
                     new_arr = []
                     x = Train(fixed_spacing , new_elem)
                     x.get_words()
                     new_arr = x.storage
                     
                     for elem in new_arr:
                             
                         ret_arr.append(elem)
                 else:
                     
                     ret_arr.append(new_elem)
                ##### train modification ends #######
                 
                 arr_copy.remove(a)
                 new_array.append([new_elem, arr_copy])
            
        recursive_scrabbled_gegs(new_array , ret_arr)
    
    
    recursive_scrabbled_gegs(array_start , return_array)
    
    #the next block is just to control the length of the words in the returned arrays
    if max_len and max_len < len(array):
        new_arr = []
        for each in return_array:
            if len(each) > max_len:
                continue
            else:
                new_arr.append(each)
        return_array = new_arr
    
    return return_array 

# test input
farr = ['a']
starting_string = 'po'
x = scrabbled_gegs(['l' , 'r' , 'e' ,'i','c', 'a', 'p', 'o'] )


def validate_words(x, starting_string = ''):
    new = []
    
    # checks for the word's existence in dictionary
    for word in x:
        word.insert(0, starting_string)
        if ''.join(word) in py_dic:
            new.append(''.join(word))
    return new

def score_em(new):
    # counts the score and stores words in a min_heap
    # multiplies the score by -ve 1 so that my higest score can come at the top of MIN_heap (couldnt find thr module for max_heap)
    heap = []
    for word in new:
        score = 0
        for letter in word:
            score += letter_dic[letter]
        heapq.heappush(heap , [score , word ])
#    
#    for i in range(len(heap)):
#        l = heapq.heappop(heap)
#        print(l)
    return heap

result = score_em(validate_words(x , starting_string))
while result != []:
    var = heapq.heappop(result)
    if var[1] == 'police':
        print(True)
    print(var)


