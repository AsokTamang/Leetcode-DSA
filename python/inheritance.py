class shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled
    def desc(self):
        print(f'It is {self.color} and {'is filled' if self.is_filled is True else 'not filled' }')
class circle(shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius
    def area(self):
        print(f'Its area is:{3.14*self.radius*self.radius}')
        super().desc()
class square(shape):
    def __init__(self,color,is_filled,length):
        super().__init__(color,is_filled)
        self.length=length
    def area(self):
        print(f'Its area is:{self.length*self.length}')
        super().desc()
class triangle(shape):
    def __init__(self,color,is_filled,heigth,width):
        super().__init__(color,is_filled)
        self.heigth=heigth
        self.width=width
    def area(self):
        print(f'Its area is:{(1/2) * self.heigth * self.width}')
        super().desc()
c=circle('red',True,5)
s=square('blue',False,10)
t=triangle('green',True,10,15)
c.area()
s.area()
t.area()
print(c.color)


