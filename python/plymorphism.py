class shape():
   is_shape=True

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(f'Area is :{3.14*self.radius**2}')


class square(shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(f'Area is :{self.length ** 2}')
class triangle(shape):
    def __init__(self, length,breadth):
        self.length = length
        self.breadth=breadth

    def area(self):
        print(f'Area is :{self.length * self.breadth * 0.5}')
class pizza(circle):
    def __init__(self,radius,toppings):
        super().__init__(radius)
        self.toppings=toppings
class rubber:
    is_shape=False
    def area(self):
        print('It dont have an area.')
shapes=[circle(10),square(20),triangle(10,20),pizza(7,8),rubber()]
for item in shapes:
    item.area()
    print(item.is_shape)