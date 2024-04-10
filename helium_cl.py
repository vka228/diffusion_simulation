from air_cl import Particle

class Helium(Particle):
    _mass = 6.6 * 10 ** -24
    def __init__(self, crd_x, crd_y):
        self._coord[0] = crd_x
        self._coord[1] = crd_y
        print("HELIUM INITIALIZED")
        print("X = ", crd_x)
        print("Y = ", crd_y)

    def track(self):
        print("HELIUM X = ", self.get_coord()[0])
        print("HELIUM Y = ", self.get_coord()[1])
