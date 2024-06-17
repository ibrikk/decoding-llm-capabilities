class LongToss:
    def __init__(self, initialVelocity, targetDistance, windResistance):
        self.__initialVelocity = initialVelocity
        self.__targetDistance = targetDistance
        self.__windResistance = windResistance

    def farEnough(self):
        '''
        Given the values that are provided in the constructor, will the ball 
        reach the target distance?  Return True if it does, False if it does not.
        '''
        return self.totalDistance() >= self.__targetDistance

    def totalDistance(self):
        '''
        Given the values that are provided in the constructor, how far will the
        ball travel before it stops moving?  Return that distance.
        '''
        distance_travelled = 0
        velocity = self.__initialVelocity

        while velocity > 0:
            distance_travelled += velocity
            velocity -= self.__windResistance
            if velocity < 0:
                velocity = 0

        return distance_travelled

def main():
    # Example test cases
    toss1 = LongToss(5, 10, 2)
    print(toss1.totalDistance())  # Expected output: 9
    print(toss1.farEnough())      # Expected output: False
    
    toss2 = LongToss(10, 20, 1)
    print(toss2.totalDistance())  # Expected output: 55
    print(toss2.farEnough())      # Expected output: True

if __name__ == "__main__":
    main()
