class RadiusInputError(Exception):
    pass

class Circle(Exception):
    def __init__(self,radius=0):
    	self.radius=radius
    try:
        radius = input("Enter the radius: ")
        if type(radius) != int:
             raise RadiusInputError
        break
    except RadiusInputError:
        print(x+" is not a number")

Circle('hello')
