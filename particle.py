"""
Particle physics system
"""
import numpy as np
from numpy import typing

from random import seed, uniform

class Particle():

    def __init__(self, WIDTH: int, HEIGHT: int, SEED: int):
        # Set seed 
        seed(SEED)
        
        # Init particles with random position
        x = uniform(0, WIDTH)
        y = uniform(0, HEIGHT)

        self.position = np.array([x, y])
        self.velocity = np.array([0, 0])
        self.acceleration = np.array([0, 0])

    def update(self):
        """
        Update velocity and position, and reset acceleration to zero
        """
        self.velocity += self.acceleration
        self.position += self.velocity
        
        self.acceleration *= 0

    def apply_force(self, force: np.ndarray):
        """
        Apply a force to update the acceleration
        """
        self.acceleration @= force
