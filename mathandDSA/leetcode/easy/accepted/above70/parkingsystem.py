# Runtime: 136 ms, faster than 71.26% of Python3 online submissions for Design Parking System.
# Memory Usage: 14.7 MB, less than 81.72% of Python3 online submissions for Design Parking System.

class ParkingSystem:

    small = 0
    medium = 0
    big = 0

    def __init__(self, big: int, medium: int, small: int):
        self.big += big
        self.medium += medium
        self.small += small

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big != 0: # Big
            self.big -= 1
        elif carType == 2 and self.medium != 0: # Medium
            self.medium -= 1
        elif carType == 3 and self.small != 0: # Small
            self.small -= 1
        else:
            return False
        
        return True


x = ParkingSystem(0, 2, 1)
x.addCar(2)
