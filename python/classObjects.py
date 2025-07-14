class Coding:  #here we are defining a class called Coding
    def __init__(self,language,fields,pace):  #then we are initializing with language,fields and pace which are the attributes
        self.language=language
        self.fields=fields
        self.pace=pace
    def description(self):  #then here we are defining a function or method called description

        print(f'{self.language} is used in {self.fields} which is {self.pace}')


js=Coding('javascript','software development','fast and effetive')      #here we are just filling the attributes of class coding and storing them in a var called js
python=Coding('Python','Aritficial Intelligence','fast and scalable')       #same here with python

Coding.description(python)   #then we are calling the method called description of class coding with var js lets see what this gonna do



class Player:
    def __init__(self,name,health,motion,rest):
        self.name=name
        self.health=health
        self.motion=motion
        self.rest=rest
    def move(self):
        print(f'{self.name}\'s  initial health was {self.health}')
        self.health-=5
        self.motion=True
        self.rest=False
        print(f'{self.name} moved, his health is: {self.health} ')
class Healer(Player):
    def healing(self):
        self.health+=5
        self.rest=True
        self.motion=False
        print(f'{self.name} rested, his health is {self.health} ')


messi=Healer('Messi',45,True,False)   #here we are passing attributes wth 45 , true and false using class Player
messi.move()  #then we are passing the method called move on messi 
messi.healing()