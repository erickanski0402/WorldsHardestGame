import pyglet
from game_area import will_collide

class Player:
    def __init__(self, pos_x, pos_y):
        self.set(pos_x = pos_x, pos_y = pos_y, vel_x = 0, vel_y = 0, width = 30, alive = True)

    def draw(self):
        # Square is drown from the bottom left corner
        # print(f"Drawing player at position: ({self.pos_x}, {self.pos_y})")
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, self._quad)

    def set(self, pos_x, pos_y, vel_x, vel_y, width, alive):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.width = width
        self.alive = alive
        self._quad = (('v2f', (self.pos_x, self.pos_y,
                    self.pos_x + self.width, self.pos_y,
                    self.pos_x + self.width, self.pos_y + self.width,
                    self.pos_x, self.pos_y + self.width)))

    def move(self):
        colliding = will_collide(self)
        print('Colliding:', colliding )

        self.set(
            self.pos_x + self.vel_x if not colliding[0] else self.pos_x,
            self.pos_y + self.vel_y if not colliding[1] else self.pos_y,
            self.vel_x,
            self.vel_y,
            30,
            True
        )
        self.draw()
