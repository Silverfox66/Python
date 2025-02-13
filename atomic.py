#Physics mixed with python

class Particle:
    def __init__(self, name, charge, mass):
        self.name = name
        self.charge = charge
        self.mass = mass

class Atom:
    def __init__(self, name):
        self.name = name
        self.protons = []
        self.neutrons = []
        self.electrons = []