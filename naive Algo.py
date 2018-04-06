# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 21:16:04 2017

@author: Frostbete
"""


"""
New algorithim
-will probably remove the temp.py file

-pseudo-version
- if , lets say you have the letters abcd
    - initially make an array [[[a], [b,c,d]] , [[b] , [a,c,d]] , [[c] , [a,b,d]] , [[d] , [a,b,c]]]
        - that is each element of an array (say elem_lvl1) would be another array containing two more arrays (elem_lvl2_a , elem_lvl2_b)
        - elem_lvl2_a  will (initially) contain one letter from abcd
        - elem_lvl2_b will contain all the letters in the initial string/array (abcd) 
            except any letter which is in elem_lvl2_a
                - for example a valid combination pair of [elem_lvl2_a , elem_lvl2_b] = elem_lvl1_a is
                        [[a,b,c] , [d]
                        [[a,d] , [b,c]]
                - invalid combination's example will be
                        [[a,b,c] , [a,d]]
        - A new temporary list will be made with the same format of elem_lvl1 and elem_lvl2
            such that elem_lvl2_a will be the entire elem_lvl2_a from the previous list appended with one element from elem_lvl2_b
            (this will be done for each element in elem_lvl2_b)
            - example:
                a random element from list_1 = [[a.b], [c,d]]
                correspondong element in new_temp_list = [[a,b,c] , [d]] , [[a,b,d] , [c]]
        - keep doing this until elem_lvl2_b is an empty list
        - all the elem_lvl2_a elements formed during this process will be every permutation and combination of the words
"""        