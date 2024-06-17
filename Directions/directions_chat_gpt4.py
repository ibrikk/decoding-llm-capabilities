# -*- coding: utf-8 -*-
"""
Programming 11 Template

Refer to the instructions on Canvas for more information.
"""
__version__ = 1

class Directions:
    
    def __init__(self, data):
        self.__data = data
        self.__biggest = ''

    def getBiggest(self):
        return self.__biggest

    def biggestStep(self):
        max_distance = 0
        for direction in self.__data:
            distance = int(direction[1:])
            if distance > max_distance:
                max_distance = distance
                self.__biggest = direction

    def finalPosition(self):
        x, y = 0, 0
        for direction in self.__data:
            move = int(direction[1:])
            if direction[0] == 'U':
                y += move
            elif direction[0] == 'D':
                y -= move
            elif direction[0] == 'L':
                x -= move
            elif direction[0] == 'R':
                x += move
        return (x, y)

######################################################################################

def main():
    # Test for biggestStep
    data = ['U1','D2','L3','R4']
    testObj = Directions(data)
    testObj.biggestStep()
    assert testObj.getBiggest() == 'R4', "The largest step from the sequence ['U1','D2','L3','R4'] is R4."
    
    # Test for finalPosition
    assert testObj.finalPosition() == (1,-1), "The final position reached after sequence ['U1','D2','L3','R4'] is (1,-1)."

    print("All tests passed!")

if __name__ == "__main__":
    main()
