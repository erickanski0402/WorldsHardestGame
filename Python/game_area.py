from pyglet.gl import *

# [Line1 x, line1 y, line2 x, line2 y]
GAME_BOUNDARY_FRAME = [
    [50, 400, 50, 100],
    [50, 100, 300, 100],
    [300, 100, 300, 150],
    [300, 150, 750, 150],
    [750, 150, 750, 350],
    [750, 350, 800, 350],
    [800, 350, 800, 100],
    [800, 100, 950, 100],
    [950, 100, 950, 400],
    [950, 400, 700, 400],
    [700, 400, 700, 350],
    [700, 350, 250, 350],
    [250, 350, 250, 150],
    [250, 150, 200, 150],
    [200, 150, 200, 400],
    [200, 400, 50, 400],
]

# [Bottom Left x, Bottom Left y, Width, Height]
GAME_COLLISION_BOUNDARIES = [
    [200, 150, 50, 300],
]

def draw_game_area():
    glClear(GL_COLOR_BUFFER_BIT)

    for line in GAME_BOUNDARY_FRAME:
        glBegin(GL_LINES)
        glVertex2i(line[0], line[1])
        glVertex2i(line[2], line[3])
        glEnd()

def will_collide(player):
    # [Colliding on x-axis, Colliding on y-axis]
    colliding = [False, False]
    future_x = player.pos_x + player.vel_x
    future_y = player.pos_y + player.vel_y
    player_w = player.width

    # Collision between x-axis seems to be working. But collision on the y-axis seems funky
    for boundary in GAME_COLLISION_BOUNDARIES:
        boundary_x = boundary[0]
        boundary_y = boundary[1]
        boundary_w = boundary[2]
        boundary_h = boundary[3]

        if (future_x + player_w >= boundary_x) and (future_x <= boundary_x + boundary_w):
            colliding[0] = True
        if (future_y + player_w >= boundary_y) and (future_y <= boundary_y + boundary_h):
            colliding[1] = True

        # if (future_left_x > boundary[0] and future_left_x < (boundary[0] + boundary[2])):
        #     colliding[0] = True
        # if future_right_x > boundary[0] and future_right_x < (boundary[0] + boundary[2]):
        #     colliding[0] = True
        # if future_upper_y < boundary[1] + boundary[3] and future_upper_y > boundary[1]:
        #     colliding[1] = True
        # if future_lower_y < boundary[1] + boundary[3] and future_lower_y > boundary[1]:
        #     colliding[1] = True


    return colliding
