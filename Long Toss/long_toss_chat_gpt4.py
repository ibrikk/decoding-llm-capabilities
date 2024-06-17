class LongToss:
    def __init__(self, initialVelocity, targetDistance, windResistance):
        self.__initialVelocity = initialVelocity
        self.__targetDistance = targetDistance
        self.__windResistance = windResistance

    def farEnough(self):
        # Initialize variables
        distanceTraveled = 0
        currentVelocity = self.__initialVelocity
        
        # Loop until the ball stops
        while currentVelocity > 0:
            # Add current velocity to the total distance traveled
            distanceTraveled += currentVelocity
            
            # Check if the distance traveled meets or exceeds the target
            if distanceTraveled >= self.__targetDistance:
                return True
            
            # Decrease velocity by wind resistance
            currentVelocity = max(0, currentVelocity - self.__windResistance)
        
        # Return False if the loop ends without reaching the target
        return False

    def totalDistance(self):
        # Initialize variables
        distanceTraveled = 0
        currentVelocity = self.__initialVelocity
        
        # Loop until the ball stops
        while currentVelocity > 0:
            # Add current velocity to the total distance traveled
            distanceTraveled += currentVelocity
            
            # Decrease velocity by wind resistance
            currentVelocity = max(0, currentVelocity - self.__windResistance)
        
        # Return the total distance traveled when the ball stops
        return distanceTraveled

# Example Usage
def main():
    # Example given in the instructions
    toss = LongToss(5, 10, 2)
    print("Far Enough:", toss.farEnough())  # Should print False
    print("Total Distance:", toss.totalDistance())  # Should print 9
   
if __name__ == "__main__":
    main()
