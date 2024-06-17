# -*- coding: utf-8 -*-
"""
Programming 11 Template

Refer to the instructions on Canvas for more information.
"""
__version__ = 1

class Directions:
    
    '''
    The data parameter will contain a non-empty list of directions made up of strings of
    the form <char><int>; for example, ['U13','D2','L6','R12'].  Characters will always be
    either U (up), D (down), L (left), or R (right).  Integers will always be non-negative
    values (0s are possible).
    '''
    def __init__(self, data):
        self.__data = data
        self.__biggest = ''

    def getBiggest(self):
        return self.__biggest

    def biggestStep(self):    
        '''
        Objects that are created from this Directions class will be initialized with a
        list of directions that are stored in self.__data (see the specification above).
        This method should store the string that contains the largest amount of movement
        (i.e., the largest integer) into self.__biggest.  (The value will then be accessible
        using the getBiggest() method.)  You can assume that there are no ties; there will be
        one unique largest distance.
        
        Hint:  Given directions ['U13','D2']:
                 - self.__data[0] will yield the first item in the list:  'U13'
                 - self.__data[0][1:] will yield everything except for the first character in
                            the first item in the list:  '13'
                 - int(self.__data[0][1:]) will yield the integer representation of the 
                            integer component of the string:  13
                 - The function should store 'U13' into self.__biggest
        '''
        pass



    def finalPosition(self):
        '''
        Objects that are created from this Directions class will be initialized with a
        list of directions that are stored in self.__data (see the specification above).
        Assume that the starting point is at position (0,0).  This method should RETURN
        a tuple (x,y) that contains the final position reached after following the sequence
        of directions in the list.
             - The direction U (up)    should increase y
             - The direction D (down)  should decrease y
             - The direction L (left)  should decrease x
             - The direction R (right) should increase x
        '''
        pass
            


######################################################################################

def main():
    # You can test your solutions by calling them from here
    '''
    Here is an example of a test that you can write for biggestStep:
        data = ['U1','D2','L3','R4']
        testObj = Directions(data)
        testObj.biggestStep()
        assert testObj.getBiggest() == 'R4', "The largest step from the sequence ['U1','D2','L3','R4'] is R4."
        
    Here is an example of a test that you can write for findPosition:
        data = ['U1','D2','L3','R4']
        testObj = Directions(data)
        assert testObj.finalPosition() == (1,-1), "The final position reached after sequence ['U1','D2','L3','R4'] is (1,-1)."
    '''
    pass
   
if __name__ == "__main__":
    main()    