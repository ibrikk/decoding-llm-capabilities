# -*- coding: utf-8 -*-
""" Programming 13 Template 
Refer to the instructions on Canvas for more information. 
"""

version = 1

class LongToss:
    '''
    A player is trying to throw a ball across a line that is self.__targetDistance away. When the player throws the ball, it leaves their hand with an initial speed of self.__initialVelocity per second. After each second, the ball slows by self.__windResistance until it reaches 0, because physics is evidently quite strange here. For example:
    
    - self.__initialVelocity = 5 (feet/sec) 
    - self.__targetDistance = 10 (feet)
    - self.__windResistance = 2 (feet/sec)
    
    After 1 second, the ball has traveled 5 feet. The ball slows to 3 feet/sec.
    After 2 seconds, the ball has traveled 8 feet. The ball slows to 1 foot/sec. 
    After 3 seconds, the ball has traveled 9 feet. The ball slows to 0 feet/sec. (it can't go to -1)
    '''

    def __init__(self, initialVelocity, targetDistance, windResistance):
        self.__initialVelocity = initialVelocity
        self.__targetDistance = targetDistance
        self.__windResistance = windResistance

    def farEnough(self):
        '''
        Given the values that are provided in the constructor, will the ball reach the target distance? 
        Return True if it does, False if it does not. In the example above, it does not (return False).
        '''
        distance = self.totalDistance()
        return distance >= self.__targetDistance

    def totalDistance(self):
        '''
        Given the values that are provided in the constructor, how far will the ball travel before it stops moving? 
        Return that distance (in the example above, you would return 9).
        '''
        velocity = self.__initialVelocity
        distance = 0
        while velocity > 0:
            distance += velocity
            velocity = max(0, velocity - self.__windResistance)
        return distance
        
######################################################################################

def main():
    # You can test your solutions by calling them from here
    pass

if __name__ == "__main__":
    main()