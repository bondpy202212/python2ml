
class Transport:
    def __init__(self):
        self.can_drive = True
        self.have_cabin = True
        self. have_windows = ''
        self. have_wheels = ''
        self.have_body = False

    def print_abitilies(self):
        print(type(self).__name__ + ':')
        print("Can drive    :", self.can_drive)
        print("Have cabin   :", self.have_cabin)
        print('Have windows :', self.have_windows)
        print('Have wheels  :', self.have_wheels)
        print('Have body    :', self.have_body)
        print()


class Avto(Transport):
    def __init__(self):
        super().__init__()
        self.have_windows = 'six'
        self.have_wheels = 'four'


class Track(Transport):
    def __init__(self):
        super().__init__()
        self.have_windows = 'three'
        self.have_wheels = 'six'
        self.have_body = True


class SportCar(Transport):
    def __init__(self):
        super().__init__()
        self.have_cabin = 'only pilot'
        self.have_windows = 1
        self.have_wheels = 4



if __name__ == '__main__':
    avto = Avto()
    avto.print_abitilies()

    track = Track()
    track.print_abitilies()

    sportcar = SportCar()
    sportcar.print_abitilies()