class Directions:
    def __init__(self, data):
        self.__data = data
        self.__biggest = ''

    def getBiggest(self):
        return self.__biggest

    def biggestStep(self):
        biggest_value = 0
        for direction in self.__data:
            value = int(direction[1:])
            if value > biggest_value:
                biggest_value = value
                self.__biggest = direction

    def finalPosition(self):
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