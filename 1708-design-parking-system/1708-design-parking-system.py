'''
keep track of:
car: car type, number of parked car

parking lot: car type, # of each size, # avail lot of each size, only allow to parked in the matching lot vs car type (small car - small lot, no small car in big lot)

action:
define the # of avail lot of each car type -> static or dynamically? via input

check matching available parking lot with the current car (size), return true false otherwise




'''
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.slots = 30 #given 

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big > 0:
            self.big -= 1
            return True
        elif carType == 2 and self.medium > 0:
            self.medium -= 1
            return True
        elif carType == 3 and self.small > 0:
            self.small -= 1
            return True
        else:
            return False
        

        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)