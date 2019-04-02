"""The asteroid class definition."""


import math
import random

import pyxel

import sound
from utils import check_bounds, rotate_around_origin, Point
import constants


class Asteroid:
    """The asteroid class.

    The asteroid class describes the behaviour and rendering of the asteroids. This includes:
    - initial creation
    - spawning of new asteroids
    - splitting of asteroids into smaller asteroids
    - movement and rotation

    There are three different asteroid shapes described in the constants file.

    On the class level, it also keeps track of all asteroids in play (and can
    render all at once), and the asteroid score."""

    asteroids = []
    mineral_score = 0
    minerals_stored = 0

    def __init__(
        self,
        size=constants.ASTERPOD_INITIAL_SIZE,
        radius=constants.ASTEROID_RADIUS,
        position=None,
        rock_type="asteroid",
    ):
        """Initialise the asteroid, including the position, size, and points.

        By default, the asteroid is the largest size and randomly placed, but
        this is overriden for smaller asteroids."""

        self.colour = constants.ASTEROID_COLOUR
        self.size = size
        self.radius = radius
        self.rock_type = rock_type

        self.init_position(position)

        self.direction = random.random() * math.pi * 2
        self.velocity = rotate_around_origin(
            (0, -constants.ASTEROID_VELOCITY), self.direction
        )

        self.spin_direction = random.choice((-1, 1))

        asteroid_points = random.choice(constants.ASTEROID_SHAPES)
        scale = radius / constants.PLANET_RADIUS

        self.points = []
        for x, y in asteroid_points:
            point_new = Point(x * scale, y * scale)
            point_new.rotate_point(self.direction)
            self.points.append(point_new)

        Asteroid.asteroids.append(self)

    
    
    def init_position(self, position):
        """Create the position, either as defined, or random.

        If the position is random, positions are tried until one
        is found which doesn't overlap the ship."""

        if position:
            x, y = position
            self.x = x
            self.y = y
        else:
            ship_x = Asteroid.ship.x
            ship_y = Asteroid.ship.y

            while True:
                self.x = random.randint(0, pyxel.width)
                self.y = random.randint(0, pyxel.height)

                if (
                    math.hypot(self.x - ship_x, self.y - ship_y)
                    > constants.ASTEROID_SPAWN_BUFFER
                ):
                    break

    @classmethod
    def init_class(cls, ship):
        """An initial method called before the asteroids are first placed to
        give the class the ship position for reference."""
        cls.ship = ship

    def update(self):
        """Update the position and rotation of the asteroid. Also checks bounds."""

        rotation_angle = constants.ASTEROID_ROTATION * self.spin_direction

        for point in self.points:
            point.rotate_point(rotation_angle)

        x_vol, y_vol = self.velocity
        self.x += x_vol
        self.y += y_vol

        self.x = check_bounds(self.x, pyxel.width, constants.ASTEROID_BUFFER)
        self.y = check_bounds(self.y, pyxel.height, constants.ASTEROID_BUFFER)

    def destroy(self):
        """Destroy asteroid and place new smaller asteroids if appropriate."""
        if self.size > 0:
            for _ in range(constants.ASTEROID_SPLITS):
                Asteroid(self.size - 1, self.radius / 2, (self.x, self.y))

        Asteroid.asteroids.remove(self)
        del self

    def display(self):
        """Display the asteroid by iterating through the points and drawing lines."""
        for point1, point2 in zip(self.points, self.points[1:] + [self.points[0]]):
            pyxel.line(
                x1=point1.x + self.x,
                y1=point1.y + self.y,
                x2=point2.x + self.x,
                y2=point2.y + self.y,
                col=self.colour,
            )

    @staticmethod
    def initiate_game():
        """Place the initial three asteroids and reset score."""
        Asteroid.asteroids.clear()
        Asteroid.mineral_score = 0
        Asteroid.minerals_stored = 0
        Planet()
        for _ in range(constants.MINERAL_INITIAL_QUANTITY):
            Mineral()

    @staticmethod
    def update_all():
        """Convenience function to update all asteroids."""
        for asteroid in Asteroid.asteroids:
            asteroid.update()

    @staticmethod
    def display_all():
        """Convenience function to display all asteroids."""
        for asteroid in Asteroid.asteroids:
            asteroid.display()

    def get_colour(self):
        return self.colour

    def get_size(self):
        return self.size

class Mineral(Asteroid):
    def __init__(
        self,
        size=constants.MINERAL_INITIAL_SIZE,
        radius=constants.MINERAL_RADIUS,
        position=None,
        rock_type="mineral",
    ):
        """Initialise the mineral, including the position, size, and points.

        By default, the asteroid is the largest size and randomly placed, but
        this is overriden for smaller asteroids."""

        self.colour = constants.MINERAL_COLOUR
        self.size = size
        self.radius = radius
        self.rock_type = rock_type

        self.init_position(position)

        self.direction = random.random() * math.pi * 2
        self.velocity = rotate_around_origin(
            (0, -constants.MINERAL_VELOCITY), self.direction
        )

        self.spin_direction = random.choice((-1, 1))

        asteroid_points = random.choice(constants.ASTEROID_SHAPES)
        scale = radius / constants.PLANET_RADIUS

        self.points = []
        for x, y in asteroid_points:
            point_new = Point(x * scale, y * scale)
            point_new.rotate_point(self.direction)
            self.points.append(point_new)

        Asteroid.asteroids.append(self)

    def harvest(self):
        """Add mineral to harvested minerals, then destroy."""
        Asteroid.minerals_stored += 1
        Asteroid.asteroids.remove(self)
        del self

class Planet(Asteroid):
    def __init__(
        self,
        size=constants.PLANET_INITIAL_SIZE,
        radius=constants.PLANET_RADIUS,
        position=(100,100),
        rock_type="planet",
    ):
        """Initialise the mineral, including the position, size, and points.

        By default, the asteroid is the largest size and randomly placed, but
        this is overriden for smaller asteroids."""

        self.colour = constants.PLANET_COLOUR
        self.size = size
        self.radius = radius
        self.rock_type = rock_type

        self.init_position(position)

        self.direction = random.random() * math.pi * 2
        self.velocity = rotate_around_origin(
            (0, -constants.PLANET_VELOCITY), self.direction
        )

        self.spin_direction = random.choice((-1, 1))

        asteroid_points = random.choice(constants.ASTEROID_SHAPES)
        scale = radius / constants.PLANET_RADIUS

        self.points = []
        for x, y in asteroid_points:
            point_new = Point(x * scale, y * scale)
            point_new.rotate_point(self.direction)
            self.points.append(point_new)

        Asteroid.asteroids.append(self)

    def deliver():
        """Add mineral to harvested minerals, then destroy."""
        Asteroid.mineral_score += Asteroid.minerals_stored
        Asteroid.minerals_stored = 0
    


    
