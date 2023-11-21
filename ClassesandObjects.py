#Classes and Objects Part 1

class Robot:
    def __init__(self, name:str, color:str, weight:int):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print(f"My name is {self.name}.")


class Person:
    
    robot_owned:Robot
    def __init__(self, name:str, persona:str, isSitting:bool):
        self.name = name
        self.persona = persona
        self.isSitting = isSitting

    def sitDown(self):
        self.isSitting = True

    def standUp(self):
        self.isSitting = False



robo1 = Robot("Tom", "red", 30)
robo2 = Robot("Jerry", "blue", 40)

robo1.introduce_self()
robo2.introduce_self()

p1 = Person("Samantha", "Talkative", True)
p2 = Person("Mark", "Gentle", False)

p1.robot_owned = robo1
p2.robot_owned = robo2

p1.robot_owned.introduce_self()
p2.robot_owned.introduce_self()

# Classes and Objects Part 2
