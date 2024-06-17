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
        """
        Finds the direction with the largest movement (largest integer) and stores it in `self.__biggest`.
        """
        biggest_value = 0
        for direction in self.__data:
            value = int(direction[1:])
            if value > biggest_value:
                biggest_value = value
                self.__biggest = direction

    def finalPosition(self):
        """
        Calculates and returns the final position after following the sequence of directions.
        """
        x, y = 0, 0
        for direction in self.__data:
            char, value = direction[0], int(direction[1:])
            if char == 'U':
                y += value
            elif char == 'D':
                y -= value
            elif char == 'L':
                x -= value
            elif char == 'R':
                x += value
        return (x, y)
            


######################################################################################

def main():
    # You can test your solutions by calling them from here
    data = ['U13', 'D2', 'L3', 'R4']
    testObj = Directions(data)
    testObj.biggestStep()
    print(f"The largest step: {testObj.getBiggest()}")  # Output: The largest step: U13

    final_position = testObj.finalPosition()
    print(f"The final position: {final_position}")  # Output: The final position: (11, 11)

    # Add more tests here
   
if __name__ == "__main__":
    main()
