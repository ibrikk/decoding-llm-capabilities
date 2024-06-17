class LongToss:
    def __init__(self, initialVelocity, targetDistance, windResistance):
        self.__initialVelocity = initialVelocity
        self.__targetDistance = targetDistance
        self.__windResistance = windResistance

    def farEnough(self):
        distance = 0
        velocity = self.__initialVelocity
        while velocity > 0:
            distance += velocity
            velocity = max(0, velocity - self.__windResistance)
        return distance >= self.__targetDistance

    def totalDistance(self):
        distance = 0
        velocity = self.__initialVelocity
        while velocity > 0:
            distance += velocity
            velocity = max(0, velocity - self.__windResistance)
        return distance