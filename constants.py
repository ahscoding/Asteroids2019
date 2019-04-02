"""Module to contain constants."""

# General constants #
BACKGROUND_COLOUR = 0
SCORE_COLOUR = 7
STORED_COLOUR = 5
DEATH_COLOUR = 0
DEATH_STRIP_COLOUR = 8
DEATH_TEXT_COLOUR = 0
DEATH_HEIGHT = 134

INITIAL_SPAWN_FREQUENCY = 100
SPAWN_FREQUENCY_MOVEMENT = 0.95 
MAX_SPAWN_SPEED = 30

INITIAL_MINERAL_RATE = 50
MINERAL_RATE_MOVEMENT = 0.9 #May introduce later
MIN_MINERAL_RATE = 10

HIGH_SCORE_FILE = "score.txt"
SOUND_FILE = "sound.pyxel"

# Ship related constants #
SHIP_COLOUR = 10
SHIP_INITIAL_POSITION = (100, 100)
SHIP_POINTS = [(0, -8), (4, 4), (0, 2), (-4, 4)]
SHIP_ACCELERATION_POINTS = 6, 13
SHIP_ACCELERATION_COLOUR = 10
ROTATION = 0.1
DRAG = 0.98
ACCELERATION = 0.4
MAX_ACCELERATION = 6
SHIP_RADIUS = 4
BUFFER = 7
SHIP_DRIFT_VELOCITY = 0.6
SHIP_BREAKUP_ROTATION = 0.01
SHIP_BREAKUP_DRAG = 0.997

# Bullet related constants #
BULLET_COLOUR = 8
BULLET_VELOCITY = 5
BULLET_RADIUS = 1
BULLET_SHOOT_FREQUENCY = 5

# Asteroid related constants #
ASTEROID_COLOUR = 8
ASTEROID_INITIAL_QUANTITY = 3
ASTEROID_ROTATION = 0.02
ASTEROID_RADIUS = 8
ASTERPOD_INITIAL_SIZE = 0
ASTEROID_SPLITS = 3
ASTEROID_VELOCITY = 0.7
ASTEROID_BUFFER = 16
ASTEROID_SPAWN_BUFFER = (SHIP_RADIUS + ASTEROID_RADIUS) * 4

ASTEROID_SHAPES = [
    [
        (0, 15),
        (4, 9),
        (11, 5),
        (15, 1),
        (5, -3),
        (0, -14),
        (-6, -4),
        (-17, -4),
        (-12, 9),
    ],
    [
        (1, 16),
        (6, 12),
        (6, 6),
        (17, 2),
        (9, -12),
        (1, -17),
        (-4, -2),
        (-18, -4),
        (-11, 8),
    ],
    [
        (0, 17),
        (7, 10),
        (4, 8),
        (14, -1),
        (5, -2),
        (1, -16),
        (-6, -2),
        (-16, -4),
        (-11, 6),
    ],
]

#Mineral-related constants
MINERAL_RADIUS = 6
MINERAL_INITIAL_SIZE = 0
MINERAL_VELOCITY = 0.5
MINERAL_COLOUR = 7
MINERAL_INITIAL_QUANTITY = 20

#Planet-related constants
PLANET_RADIUS = 16
PLANET_INITIAL_SIZE = 0
PLANET_VELOCITY = 0
PLANET_COLOUR = 10
