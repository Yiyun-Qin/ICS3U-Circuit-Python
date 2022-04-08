# /usr/bin/env python3

# Created by: Yiyun Qin
# Created in: April 2022
# This is the star wars game

import stage
import ugame


def game_scene():
    # main game function

    # grab the image, is image bank for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    # 10 x 8 tiles for size 16 x 16
    background = stage.Grid(image_bank_background, 10, 8)

    # pick the 5th picture and shown up at (75, 66)
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # create a stage to display background, frame rate 60 fps
    game = stage.Stage(ugame.display, 60)
    # set the layer, items show up in order
    game.layers = [ship] + [background]
    # take layers to show on the screen
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # K_X: constants of button A
        if keys & ugame.K_X:
            print("A")
        if keys & ugame.K_O:
            print("B")
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)


        # update game logic

        # redraw Sprites
        game.render_sprites([ship])
        # wait until 60 tick and loop again
        game.tick()


if __name__ == "__main__":
    game_scene()
