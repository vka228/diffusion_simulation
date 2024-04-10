import numpy as np
from scipy.stats import maxwell
from func import calc_maxwell, vmax, dist_btw
import random
from air_cl import Air  # Assuming 'air_cl' module contains 'Air' class for molecules
from helium_cl import Helium

class Space:
    _temperature = 300
    _mass = 4.76 * 10 ** -26
    _helium = Helium(0, 0)

    def __init__(self, xdim, ydim, num_of_molecules):
        self._dim = [xdim, ydim]
        self._helium.__init__(xdim / 2, ydim / 2)
        #initializing air as nitrogen
        self._mol = [Air(0, 0, 0, 0, 4.6 * 10 ** -26, 0) for _ in range(num_of_molecules)]  # Initialize list of molecules

    def setmol(self):
        # setting air
        for mol in self._mol:
            mol.init(
                random.uniform(0, self._dim[0]),
                random.uniform(0, self._dim[1]),
                0.1,
                0.1
            )
        # setting helium



    def getscatx(self):
        return [mol.getx() for mol in self._mol]

    def getyscat(self):
        return [mol.gety() for mol in self._mol]

    def update(self):
        self._helium.track()
        self._helium.update_mol(self._dim[0], self._dim[1])
        for mol in self._mol:
            if (dist_btw(mol.getx(), mol.gety(), self._helium.getx(), self._helium.gety()) <= 0.0005):
                print("COLLISION AT " , mol.getx(), mol.gety(), self._helium.getx(), self._helium.gety())
                mol.collide(self._helium)

            mol.update_mol(self._dim[0], self._dim[1])

    def setmaxwell(self):
        #speeds = [calc_maxwell(_, self._temperature, self._mass) for _ in range(len(self._mol))]
        speeds = maxwell.rvs(vmax(self._temperature), 0, len(self._mol))
        cou = 0
        for mol in self._mol:
            cosa = random.random() * random.randint(-1, 1)
            sina = np.sqrt(1 - cosa ** 2) * random.randint(-1, 1)
            vxtmp = speeds[cou] * cosa
            vytmp = speeds[cou] * sina
            print(vxtmp, vytmp)
            mol.setspeed(vxtmp, vytmp)
            cou = cou + 1

    def get_he_cord(self):
        return [self._helium.getx(), self._helium.gety()]


