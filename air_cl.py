dim = 0.01
resx = []
resy = []

class Particle:
    _mass = 0
    _coord = [0, 0]
    _velocity = [0, 0]
    _size = 0

    def __init__(self, x, y, vx, vy, mass, size):
        self._mass = mass
        self._coord = [x, y]
        self._velocity = [vx, vy]
        self._size = size

    def collide(self, other_particle):
        omass = other_particle.get_mass()
        ovel = other_particle.get_velocity()

        tomass = omass + self._mass

        momx1 = self._mass * self._velocity[0]
        momy1 = self._mass * self._velocity[1]

        momx2 = omass * ovel[0]
        momy2 = omass * ovel[1]

        momx = momx1 + momx2
        momy = momy1 + momy2

        momx1_f = momx * self._mass / tomass
        momy1_f = momy * self._mass / tomass

        momx2_f = momx * omass / tomass
        momy2_f = momy * omass / tomass

        self.set_velocity(momx1_f / self._mass, momy1_f / self._mass)
        other_particle.set_velocity(momx2_f / omass, momy2_f / omass)

        self.update_mol(dim, dim)
        other_particle.update_mol(dim, dim)
        resx.append(other_particle.get_coord()[0])
        resy.append(other_particle.get_coord()[1])




        print("COLLISION RESULT:")
        print("MASSES are", self._mass,other_particle.get_mass() )
        print("HELIUM VELOCITY:", other_particle.get_velocity() )
        print("AIR VELOCITY:", self._velocity)
        print("HELIUM COORD", other_particle.get_coord())

    '''def collide(self, other_particle):
        # Calculate total mass
        total_mass = self._mass + other_particle.getmass()

        momentum1_x = self._mass * self._velocity[0]
        momentum1_y = self._mass * self._velocity[1]

        momentum2_x = other_particle.getmass() * other_particle.get_velocity()[0]
        momentum2_y = other_particle.getmass() * other_particle.get_velocity()[0]

        total_mom_x = momentum1_x + momentum2_x
        total_mom_y = momentum1_y + momentum2_y'''


    def getx(self):
        return self._coord[0]

    def gety(self):
        return self._coord[1]

    def get_mass(self):
        return self._mass

    def get_velocity(self):
        return self._velocity
    def get_coord(self):
        return self._coord
    def set_velocity(self, vx, vy):
        self._velocity = [vx, vy]

    def update_mol(self, xdim, ydim):
        if(self._coord[0] + self._velocity[0] > xdim):
            self._coord[0] = 0
        if (self._coord[1] + self._velocity[1] > ydim):
            self._coord[1] = 0
        if (self._coord[0] + self._velocity[0] < 0):
            self._coord[0] = xdim
        if (self._coord[1] + self._velocity[1] < 0):
            self._coord[1] = ydim
        self._coord[0] = self._coord[0] + self._velocity[0]
        self._coord[1] = self._coord[1] + self._velocity[1]




class Air(Particle):
    _mass = 4.76 * 10 ** -26

    def init(self, x, y, vx, vy):
        self._coord = [x, y]
        self._velocity = [vx, vy]
        print("MOLECULE INITIALIZED:")
        print("X = ", self._coord[0])
        print("Y = ", self._coord[1])
        print("VX = ", self._velocity[0])
        print("VY = ", self._velocity[1])








# setting velocities 1000 times lower as we want to see a slowed process
    def setspeed(self, vx, vy):
        self._velocity = [vx * 10 ** -6 , vy * 10 ** -6]
