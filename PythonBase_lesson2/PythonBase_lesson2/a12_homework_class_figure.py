
class Figure(object):
    def __init__(self, hight =- 0.0, width = 0.0):
        self.hight = hight
        self.width = width


class Rectangle(Figure):
    def draw(self):
        for i in range(self.hight):
            print('/ ' * self.width)

class MouseClick(Figure):
    def numberclick(self):
        self.hight = int(input("Click left button (enter num click) - hight: "))
        self.width = int(input("Click left button (enter num click) - width: "))
        return self.hight, self.width

if __name__ == "__main__":
    rect1 = Rectangle(3, 5)
    rect1.draw()

    fig1 = MouseClick()
    sizefig = fig1.numberclick()
    print(sizefig)

    rect2 = Rectangle(sizefig[0], sizefig[1])
    rect2.draw()
