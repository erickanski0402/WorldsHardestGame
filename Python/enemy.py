from math import pi, sin, cos, sqrt
from pyglet.gl import *

class Enemy:
    def __init__(self, pos_x, pos_y, vel_x, vel_y, radius):
        self.set(pos_x, pos_y, vel_x, vel_y, radius, False)

    def draw(self):
        iterations = int(2 * self.radius * pi)
        s = sin(2 * pi / iterations)
        c = cos(2 * pi / iterations)

        dx, dy = self.radius, 0

        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(self.pos_x, self.pos_y)
        for i in range(iterations + 1):
            glVertex2f(self.pos_x + dx, self.pos_y + dy)
            dx, dy = (dx * c - dy * s), (dy * c + dx * s)
        glEnd()

    def set(self, pos_x, pos_y, vel_x, vel_y, radius, colliding):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.radius = radius
        self.colliding = False

    def move(self, player):
        # print(f"Current position {self.pos_x}")
        if self.pos_x < 275 or self.pos_x > 725:
            self.vel_x *= -1

        self.set(
            self.pos_x + self.vel_x,
            self.pos_y + self.vel_y,
            self.vel_x,
            self.vel_y,
            self.radius,
            False
            # self.check_collisions(player)
        )
        self.draw()

    def check_collisions(self, player):
        # Needs some work
        player_height = 10
        player_width = 10
        player_pos_x = player.pos_x + player_width
        player_pos_y = player.pos_y + player_height

        test_x = self.pos_x
        test_y = self.pos_y

        if self.pos_x < player_pos_x:
            test_x = player_pos_x
        elif self.pos_x > player_pos_x + player_width:
            test_x = player_pos_x + player_width
        if self.pos_y < player_pos_y:
            test_y = player_pos_x
        elif self.pos_y > player_pos_y + player_height:
            test_y = player_pos_y + player_height

        dist_x = player_pos_x - test_x
        dist_y = player_pos_y - test_y
        # print();
        distance = sqrt((dist_x * dist_x) + (dist_y * dist_y))

        if(distance <= self.radius):
            return True
        else:
            return False
