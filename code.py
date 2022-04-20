# /usr/bin/env python3

# Created by: Yiyun Qin
# Created in: April 2022
# This is the star wars game

import constants
import stage
import ugame


def menu_scene():
    # main game function

    # grab the image, is image bank for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add text objects
    text = []
    text1 = stage.Text(width = 29, height = 12, font = None, palette = constants.RED_PALETTE, buffer = None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(width = 29, height = 12, font = None, palette = constants.RED_PALETTE, buffer = None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # 10 x 8 tiles for size 16 x 16
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # create a stage to display background, frame rate 60 fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layer, items show up in order
    game.layers = text + [background]
    # take layers to show on the screen
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # Start button selected
        if keys & ugame.K_START != 0:
            game_scene()

        # wait until 60 tick and loop again
        game.tick()


def game_scene():
    # main game function

    # grab the image, is image bank for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # 10 x 8 tiles for size 16 x 16
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # pick the 5th picture and shown up at (75, 66)
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )
    # another sprite
    alien = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        constants.SPRITE_SIZE
    )

    # create a stage to display background, frame rate 60 fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layer, items show up in order
    game.layers = [ship] + [alien] + [background]
    # take layers to show on the screen
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # a button to fire
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        # b button

        # K_X: constants of button A
        # Ship will not move up or down
        # Check: ship will not move outside the screen
        if keys & ugame.K_RIGHT != 0:
            if ship.x < constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)

        # update game logic
        # play sound if A was just button_just_pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # redraw Sprites
        game.render_sprites([ship] + [alien])
        # wait until 60 tick and loop again
        game.tick()


if __name__ == "__main__":
    menu_scene()
