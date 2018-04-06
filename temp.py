# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def scrabbled_gegs(arr): #scrambled eggs and scrabbled      pun
   
   def scrambled_words(arr):
   # defining a recursive function to re-arrange the letters in every 
   # combination possible
   # the algorithim I am using is based on the following idea:-
   # 
   # if you have a list of every combination of K lettered words 
   # 
   # (for example, if your word is 'abc', then your list will be 
   # [abc, bac, bca, acb, cab, cba] )
   #
   # Then by adding another letter in every word, at every position , (in our list), and storing it somewhere
   # we will get every combination of a (K+1) lettered word
   # 
   # (for example, if we want to get every combination of the word, 'abcd', then we take the list in our previous example
   # ,which was every combination of 'abc', and then add 'd' at every position of every word,
   # .
   # abc -> dabc , adbc, abdc, abcd
   # bac -> dbac , bdac , badc , bacd
   # bca -> dbca , bdca , bcda , bcad
   # acb -> dacb , adcb , acdb , acbd
   # cab -> dcab , cdab , cadb , cabd
   # cba -> dcba , cdba , cbda , cbad
   #.
   # a list of all the words stated above will be a list of every combination of 'abcd')
   # 
   # To prove that there will be no duplication of words in our process, given that every letter is unique :
   #  since each of our K lettered combinatins are unique  ----- lets name this fact_1
   # then when we add another element or a letter (given, it should be unique)
   # the fact that the relative position of every letter didnt change and due to fact_1,
   # the combination of every relative position for any one word, will be unique ---- name this fact_2
   # Due to fact_2 , adding an extra letter anywhere wont change it, which is why, every combination will be unique (given that every letter is unique)
   # (for example, for the list [ab , ba] (list of combination of two lettered words)
   #   adding c , would make the list [(cab , cba) , (bca . bac)] 
   #    now because in the two lettered list combination, in one case position_of_a < position_of_b and in the other case position_of_b < position_of_a 
   #    so when we add 'c' anywhere in the list and there are two elements where c has the same position, the fact that position of a and position of b have different relative positions throughout the list will 
   #    take care that the word is not duplicated
   #    
   # Now the algorithim
   # 1. to get every combination of a N lettered array , lets name it as temp_arr
   #    divide the arr into two parts
   #    arr1 = arr[:-2]
   #    arr2 = arr[-2:] , arr2 will be an array of two letters
   # 2. get the combination of the two letters in arr2 and store them in a list
   #    temp_arr = [arr2 , arr2[::-1]]
   # 3. remove the last element from arr1, store it, and insert it in temp_arr's every element's every position (making it the new temp_arr)
   # 4. repeat until arr1 is empty    
       
       def swap_last_with_all(arr_word, copy_list):
           #making this a recursive function just to practice recursion
           #swaps the last letter with every other letter
           pos_counter = len(arr_word)-1
           x = arr_word[:]  #using x like this to avoid side effect since arr_word is an array
           copy_list.append(x)

           def aux_swap(arr_word , copy_list, pos_counter):
               
               if pos_counter == 0:
                   return
        
               temp_var = arr_word[pos_counter]
               arr_word[pos_counter] = arr_word[pos_counter - 1]
               arr_word[pos_counter - 1] = temp_var
               
               pos_counter -= 1
               
               x = arr_word[:] #using x like this to avoid side effect since arr_word is an array
               copy_list.append(x)
               
               aux_swap(arr_word , copy_list, pos_counter)
            
           aux_swap(arr_word , copy_list , pos_counter)
               
               
       arr1 = arr[:-2]
       arr2 = arr[-2:]
       
       scrabbled_list = [arr2 , arr2[::-1]]
       
       while arr1 != []:
           
           letter_to_insert = arr1.pop()
           scrabbled_list_copy = []
           
           for word in scrabbled_list:
             
               word.append(letter_to_insert)
               swap_last_with_all(word , scrabbled_list_copy)
           
           scrabbled_list = scrabbled_list_copy[:]
       
       return scrabbled_list
    
   return scrambled_words(arr)