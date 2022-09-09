#print("Aula 4")

class Robot:
    def __init__(self, name: str, colorCode: int, energy: int):
      self.name = name
      self.colorCode = colorCode
      self.energy = energy
      self.batteryTime = 0
      self.on = False

    def turnOnTheRobot(self):

        if self.energy > 0 and not(self.on):
            self.on = True
            print("À ligar", self.name)

    def remainingBatteryTime(self):
        self.batteryTime = float((self.energy * 6)/60)
        print(self.batteryTime, "horas restantes")

        if self.energy < 15:
                print("Atenção: ", self.energy, "% de bateria restante!")

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

    def greet(self):
        print("Hello World!")
        print("My name is", self.name)
        print("My color is:", self.colorCode)
        print("My energy is:", self.energy,"%")
        print("ON?", self.on)

    def off(self):
        print("Robot", self.name, "says: ")
        print("My energy is", self.energy,"%")
        print("ON?", self.on)

robots = []

robots.append(  Robot("Monday", 31, 90))
robots.append(  Robot("Tuesday", 32, 5))
robots.append(  Robot("Wednesday", 33, 12))
robots.append(  Robot("Thursday", 34, 0))
robots.append(  Robot("Friday", 35, 75))
robots.append(  Robot("Saturday", 36, 0))
robots.append(  Robot("Sunday", 37, 69))


for obj in robots:
    robot = Robot(obj.name, obj.colorCode, obj.energy)
    robot.turnOnTheRobot()

    if obj.energy > 0:
        robot.greet()
    else:
        robot.off()

    robot.remainingBatteryTime()
    robot.colorCodeTerminal()