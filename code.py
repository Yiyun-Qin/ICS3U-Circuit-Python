# /usr/bin/env python3

# Created by: Yiyun Qin
# Created in: April 2022
# This is the star wars game

import constants
import stage
import ugame


def game_scene():
    # main game function

    # grab the image, is image bank for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    # 10 x 8 tiles for size 16 x 16
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # pick the 5th picture and shown up at (75, 66)
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    # create a stage to display background, frame rate 60 fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layer, items show up in order
    game.layers = [ship] + [background]
    # take layers to show on the screen
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # K_X: constants of button A
        # Ship will not move up or down
        # Check: ship will not move outside the screen
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            if ship.x < constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x > 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass

        # update game logic

        # redraw Sprites
        game.render_sprites([ship])
        # wait until 60 tick and loop again
        game.tick()


if __name__ == "__main__":
    game_scene()
