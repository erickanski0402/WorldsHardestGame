from player import Player
from game_area import draw_game_area
from enemy import Enemy
from math import pi, sin, cos
import pyglet

UP_ARROW = 65362
DOWN_ARROW = 65364
LEFT_ARROW = 65361
RIGHT_ARROW = 65363
ARROW_KEYS = [UP_ARROW, DOWN_ARROW, LEFT_ARROW, RIGHT_ARROW]

def main():
    keys = []
    player = Player(100, 300)
    # player = Player(300,300)
    enemies = [
        Enemy(275, 175, 4, 0, 8),
        Enemy(725, 225, -4, 0, 8),
        Enemy(275, 275, 4, 0, 8),
        Enemy(725, 325, -4, 0, 8),
    ]
    window = pyglet.window.Window(height = 500, width = 1000)

    def update(self):
        window.clear()
        draw_game_area()
        player.move()

        # print(f"For enemy at y position {enemies[0].pos_y}, Colliding: {enemies[0].check_collisions(player)}")

        for enemy in enemies:
            enemy.move(player)
            # enemy.draw()

            if enemy.colliding:
                player.set(player.initial_x, player.initial_y, 0, 0, 30, False)

    @window.event
    def on_key_press(button, modifiers):
        # print("Button value:", button)
        if button in ARROW_KEYS:
            keys.append(button)
            determine_movement_vector()

    @window.event
    def on_key_release(button, modifiers):
        # print("Button value:", button)
        if button in ARROW_KEYS:
            keys.remove(button)
            determine_movement_vector()

    # Could use a bit more work. Player cant move if more than 3 buttons are being pressed
    def determine_movement_vector():
        length = len(keys)
        if (UP_ARROW in keys) and (RIGHT_ARROW in keys) and length is 2:
            # Up-right
            player.vel_x = 2
            player.vel_y = 2
        elif (DOWN_ARROW in keys) and (RIGHT_ARROW in keys) and length is 2:
            # Down-right
            player.vel_x = 2
            player.vel_y = -2
        elif (DOWN_ARROW in keys) and (LEFT_ARROW in keys) and length is 2:
            player.vel_x = -2
            player.vel_y = -2
            # Down-left
        elif (UP_ARROW in keys) and (LEFT_ARROW in keys) and length is 2:
            player.vel_x = -2
            player.vel_y = 2
            # Up-Left
        elif (UP_ARROW in keys) and length is 1:
            player.vel_x = 0
            player.vel_y = 2
            # Up
        elif (DOWN_ARROW in keys) and length is 1:
            player.vel_x = 0
            player.vel_y = -2
            # Down
        elif (LEFT_ARROW in keys) and length is 1:
            player.vel_x = -2
            player.vel_y = 0
            # left
        elif (RIGHT_ARROW in keys) and length is 1:
            player.vel_x = 2
            player.vel_y = 0
            # right
        else:
            player.vel_x = 0
            player.vel_y = 0
            # No movement

    pyglet.clock.schedule_interval(update, 0.01)
    pyglet.app.run()

if __name__ == '__main__':
    main()
