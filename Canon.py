import numpy as np
import pygame as pg
from random import randint, gauss

pg.init()
pg.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCREEN_SIZE = (800, 600)


def rand_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


class GameObject:
    pass


class Shell(GameObject):
    """
    The ball class. Creates a ball, controls it's movement and implements rendering.
    """
    def __init__(self, coord, vel, rad=20, color=None):
        """
        Constructor method. Initializes ball's parameters and initial values.
        """
        self.coord = coord
        self.vel = vel
        