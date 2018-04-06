# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 01:58:29 2018

@author: Frostbete
"""

class Train:
    """
    a new datatpye which helps me solve fixed spacing problem
    """
    
    def __init__(self, fixed , jumble):
        """
        self.fixed is the fixed spacing array which is in the formal of ['a1' , '', 'a2]
        where 'a1', 'a2' are the letters and the '' representes fixed empty spaces between them
        in this case, a2 is 2 spaces after a1, or there is exaclty ONE fixed space between a1 and a2
        
        below a few more examples to make it more clear
        ['a1' , '' , '', '', 'a2' , '' , 'a3'] -> a1 + 3 empty spaces + a2 + 1 empty space + a3
        ['a1' , 'a2', '' , 'a3'] - > a1 + 0 empty space + a2 + 1 empty space + a3
              
        
        self.jumble is the array in which we have to insert the fixed words
        
        this function can be visualised in the following way
        
        Step 0 :
        fixed - > [c, ,p , ,d]
        jumble - >             | [p , o , t ,e, t]
        
        
        NOTE: The line you see between fixed and jumble is a seperator 
        Values before THE seperator HAVE A NEGATIVE INDEX IN self.ndx_dic (more on this later)
        The negative index COMBINED WITH self.jump (more on this later), helps recognise if the value is ready to be merged yet or not
        [the values in self.ndx_dic dont get updated 
        that means,
        in Step 1, youll see that d  has crossed the seperator, yet it will still have a negative index]
        .
        This means that every letter in self.fixed has a -ve index value in self.ndx_dic
        
        
        
        
        
        Step 1 (fixed moves forward by one, such that d is directly above p)
        fixed - >       [c, ,p, , d]
        jumble - >              |[p , o , t ,e, t]
        result - >  [d , p, o , t, e, t]  (d __merges__ with p) 
        result gets appended in self.storage
        

        
        Step 2 (fixed moves forwared by 2, )
        fixed - >         [c, ,p , ,  d]
        jumble - >             | [p , o , t ,e, t]
        result - >  [ p, d, o , t, e, t]  (d __merges__ with o AND blank space ( ,, ) merges with P
                                        
        result gets appended in self.storage
        

        
        Step 3 (fixed moves forwared by 3)
        fixed - >         [c, ,   p ,   , d]
        jumble - >             | [p , o , t ,e, t]
        result - >  [*p , p, o ,d, t, e, t]  (*p __merges__ with p, (,,) merges with o , t merges with d) 
        [used a *p to denote that it belongs to the foixed array and not jumble array]
        
        result gets appended in self.storage 
        
        
        
        iterating this process tells us that there will be a point when the merging process looks like this
        Step - K (fixed moves forward by K)
        fixed - >                   [c , , *p, , d]
        jumble - >                | [p, o, t, e, t] 
        result - >  [c , p , o , *p, t , e, d, t]
        after that step, d will not be able to merge with any letter in the jumble array
        but rather it will get appended at the end of the array
        
        
        Step - K+1 (fixed moves forward by K+1)
        fixed - >                      [c,  ,*p,  , d]
        jumble - >                | [p, o, t, e, t] 
        result - >  [ p , c , o, t , *p, e, t, d]
        
        NOTE: if d had MERGED with t, then d would have been before t
        This case doesnt represent merging, but it represents d getting appended at the end
        after that step, d will not be able to merge with any letter in the jumble array
        
  
        AFTER THIS STEP HOWEVER, 'd' will not get stored in the resultant array at all
        
        Step - K+2 (fixed moves forward by K+2)
        fixed - >                         [c,  ,*p,  , d]
        jumble - >                | [p, o, t, e, t] 
        result - >  [p , o , c, t, e, *p, t]
    
        
        
        
        This case continues till Step N such that the merging process looks like this
        fixed - >                                  [c , , p , , d]
        jumble - >                | [p, o, t, e, t]
        
        One can easily infer that the number of units by which any letter (in fixed) has moved forward = the step Number
       
        looking at 'c'
        it has moved forward the lenght of -fixed-  +  the length of -jumbled- + 1   [ plus 1 because it is being APPENDED AT THE END OF JUMBLED, It is NOT merging with t ]
        therefore the number of steps by which the fixed moves forward = len(fixed) + len(jumbled) + 1
        
        """
        self.fixed = fixed      #the array with fixed spacing
        self.jumble = jumble    #the array with your jumbled word
        self.storage  = []      #the array stores all the combinations possible with fixed and jumbled
        self.jump = 0           #this value tells you by how much will the self.fixed array will move forward
        self.ndx_dic = {}
        
        i = 0
        
        #gives every letter in self.fixed a -ve index in the dic
        for letter in self.fixed:
            self.ndx_dic[letter] = i - len(self.fixed)
            i += 1
        
    def merge(self,key, val, new_word):
        """
        this method is used for merging
        if there is an empty space then  it does nothing, otherwise it merges
        """
        if val == "":
            return
        else:
            new_word.insert(key, val)
            return
    
    def move(self):
        """
        move is basically used for Moving self.fixed forwards so that it can merge with self.jumbled
        """
        self.jump += 1  # increments self.jump
        word = self.jumble[:]
        for letter in self.fixed:
            key = self.jump + self.ndx_dic[letter]
            if letter != "" and key == -1:
                return
            if 0 <= key <= len(word):
                self.merge(key , letter, word)
        self.storage.append(word)
    
    def get_words(self):
        while self.ndx_dic[self.fixed[0]] + self.jump <= len(self.jumble):
            self.move()
        self.storage.pop(-1)