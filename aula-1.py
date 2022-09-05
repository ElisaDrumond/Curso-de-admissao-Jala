# print("Aula 1")

class Poligono:
    side = 0
    numberOfSide = 0
    apothem = 0.0

    def calculatePerimeter(Self):
        print("The perimeter of the polygon is:", Self.side *Self.numberOfSide)

square = Poligono()
square.side = 4
square.numberOfSide = 4

triangle = Poligono()
triangle.side = 5
triangle.numberOfSide = 3

square.calculatePerimeter()
triangle.calculatePerimeter()