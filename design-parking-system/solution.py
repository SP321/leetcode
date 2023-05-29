class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.c={}
        self.c[1]=big
        self.c[2]=medium
        self.c[3]=small

    def addCar(self, carType: int) -> bool:
        if self.c[carType]>0:
            self.c[carType]-=1
            return True
        return False


        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)