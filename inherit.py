class Vehicle:
    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed
    
    def accelerate(self, amount):
        self.speed += amount
        print("Acceleration Finished.... New speed of the vehicle is : ", self.speed)
    
    def apply_break(self,amount):
        self.speed = max(self.speed - amount, 0.0)
        print("Breaks applied.....  New speed of the vehicle is : ", self.speed)

class SportsCar(Vehicle):
    def __init__(self, model, color, speed, mode):
        self.mode = mode
        Vehicle.__init__(self, model, color, speed)

    def change_mode(self, mode):
        self.mode = mode
        print("Mode of your sports car has changed to :", self.mode)

class SchoolBus(Vehicle):
    def accelerate(self, amount):
        print("sdfdsdfs")
        if self.speed + amount < 50.0:
            self.speed += amount
            print("Acceleration Finished.... New speed of the  is : ", self.speed)
        else:
            print("You cant overspeed a school bus")
    




car = Vehicle(model = "S Cross", color = "red", speed = 0.0)
car2 = SportsCar(model = "Ferrari", color = "red", speed = 0.0, mode = "echo")

car2.accelerate(30.0)
car2.change_mode("sports")


bus = Vehicle(model = "TATA", color = "orange", speed = 40.0)

bus.accelerate(40.0)