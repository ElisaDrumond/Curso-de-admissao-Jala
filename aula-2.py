# print("Aula 2")

class Robot:

    def __init__(Self, name: str, colorCode: int):
        Self.name = name
        Self.colorCode = colorCode
        Self.energy = 100
        Self.on = True

    def greet(Self):
        print("Hello, My name is", Self.name)
        print("My color is:", Self.colorCode)
        print("My energy is:", Self.energy)
        print("My status is:", Self.on)

name = input("What is your name? ")
colorCode = input("What is your color? ")

robot = Robot(name, colorCode)
robot.greet()