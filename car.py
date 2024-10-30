class Car:
    def __init__(self, plate_number , colour):
        self.plate_number = plate_number
        self.colour = colour

class PaintShop:
    def paint(self, car, colour):
        car.colour = colour

paint_shop=PaintShop()
car=Car("ABC-124" , "blue")
print(f"The car is {car.colour} colour now. ")
paint_shop.paint(car,  "black")
print (f"The car is changed to {car.colour}  colour. ")
