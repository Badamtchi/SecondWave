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
        if color == None:
            color = rand_color()
        self.color = color
        self.rad = rad
        self.is_alive = True

    def check_corners (self, refl_ort=0.8, refl_par=0.9):
        """
        Reflects ball's velocity when ball bumps into the screen corners. Implements inelastic rebounce.
        """
        for i in range(2):
            if self.coord[i] < self.rad:
                self.coord[i] = self.rad
                self.vel[i] = -int(self.vel[i] * refl_ort)
                self.vel[1-i] = int(self.vel[1-i] * refl_par)
            elif self.coord > SCREEN_SIZE[i] - self.rad:
                self.coord = SCREEN_SIZE[i] - self.rad
                self.vel[i] = -int(self.vel[i] * refl_ort)
                self.vel[1-i] = int(self.vel[1-i] * refl_par)

    def move(self, time=1, grav=0):
        """
        Moves the ball according to it's velocity and time step.
        Changes the ball velocity due to gravitational force.
        """
        self.vel[1] += grav
        for i in range(2):
            self.coord[i] += time * self.vel[i]
        self.check_corners()
        if self.vel[0]**2 + self.vel[1]**2 < 2**2 and self.coord[1] > SCREEN_SIZE[1] - 2*self.rad:
            self.is_alive = False

    def draw(self, screen):
        """
        Draws the ball on appropriate surface.
        """
        pg.draw.circle(screen, self.color, self.coord, self.rad)

class Canon(GameObject):
    """
    Canon Class, Manages it's rendering, movement and striking.
    """
    def __init__(self, coord=[30, SCREEN_SIZE[1]//2], angle=0, max_pow=50, min_pow=10, color=RED):
        """
        Coordinator method, Sets coordinate, direction, minimun and maximum power and color of the gun.
        """
        self.coord = coord
        self.angel = angle
        self.max_pow = max_pow
        self.min_pow = min_pow
        self.color = color
        self.active = False
        self.pow = min_pow

    def activate(self):
        """
        Activates gun's charge.
        """
        self.active = True

    def gain(self, inc=2):
        """
        Increase current gun charge power.
        """
        if self.active and self.pow < self.max_pow:
            self.pow += inc

    def strike(self):
        """
        Created ball, according to gun's direction and current charge power.
        """
        vel = self.pow
        angle = self.angel
        ball = Shell(list(self.coord), [int(vel * np.cos(angle)), int(vel * np.sin(angle))])
        self.pow = self.min_pow
        self.active = False
        return ball

    def set_angle(self, target_pos):
        """
        Sets gun's direction to target position.
        """
        self.angel = np.arctan2(target_pos[1] - self.coord[1], target_pos[0], - self.coord[0])

    def move(self, inc):
        """
        Changes vertival positin of the gun.
        """
        if (self.coord[1] > 30 or inc > 0) and (self.coord[1] < SCREEN_SIZE[1] - 30 or inc < 0):
            self.coord[1] += inc

    def draw(self, screen):
        """
        Draws the gun on the screen.
        """
        gun_shape = []
        