from player import Player
from game_area import draw_game_area
from enemy import Enemy
from math import pi, sin, cos
import pyglet

def main():
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
        if button == 65361:
            player.vel_x += -2
        if button == 65362:
            player.vel_y += 2
        if button == 65363:
            player.vel_x += 2
        if button == 65364:
            player.vel_y += -2
        # print('Key press:', 'vel_x', player.vel_x, 'vel_y', player.vel_y)

    # Need to refactor how movement works. When a player dies they preserve the keypress
    # this causes issues with movement in the opposite direction when they release keys held
    @window.event
    def on_key_release(button, modifiers):
        # print("Button value:", button)
        if button == 65361:
            player.vel_x += 2
        if button == 65362:
            player.vel_y += -2
        if button == 65363:
            player.vel_x += -2
        if button == 65364:
            player.vel_y += 2
        # print('Key release:', 'vel_x', player.vel_x, 'vel_y', player.vel_y)

    pyglet.clock.schedule_interval(update, 0.01)
    pyglet.app.run()

if __name__ == '__main__':
    main()
