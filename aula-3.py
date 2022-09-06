#print("Aula 3")

class Robot:
    def __init__(self, name: str, colorCode: int, energy: int):
      self.name = name
      self.colorCode = colorCode
      self.energy = energy
      self.on = False

    def greet(self):
        print("Hello World!")
        print("My name is", self.name)
        print("My color is:", self.colorCode)
        print("My energy is:", self.energy,"%")
        print("ON?", self.on)

    def off(self):
        print("My energy is:", self.energy,"%")
        print("ON?", self.on)

    def turnOn(self):
      if self.energy > 0 and not(self.on):
        self.on = True
        print("")
        print("À ligar", self.name, "\n")

    def colorCodeTerminal(self):
        match self.colorCode:
            case 31:
                print("\33[31m")
            case 32:
                print("\33[32m")
            case 33:
                print("\33[33m")
            case 34:
                print("\33[34m")
            case 35:
                print("\33[35m")
            case 36:
                print("\33[36m")
            case 37:
                print("\33[37m")

name = input("What is your name? ")

print("Color code: 30 to 37")
colorCode = int(input("What is your color? "))

energy = int(input("What is your energy? "))

robot = Robot(name, colorCode, energy)

robot.turnOn()
robot.colorCodeTerminal()

if energy > 0:
    robot.greet()
else:
    robot.off()