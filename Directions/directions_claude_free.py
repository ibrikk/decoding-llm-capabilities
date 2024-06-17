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
        biggest = 0
        for d in self.__data:
            step = int(d[1:])
            if step > biggest:
                biggest = step
                self.__biggest = d



    def finalPosition(self):
        x = 0
        y = 0
        for d in self.__data:
            if d[0] == 'U':
                y += int(d[1:])
            elif d[0] == 'D':
                y -= int(d[1:])
            elif d[0] == 'L':
                x -= int(d[1:])
            elif d[0] == 'R':
                x += int(d[1:])
        return (x, y)
            


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