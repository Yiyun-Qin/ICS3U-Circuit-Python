# /usr/bin/env python3

# Created by: Yiyun Qin
# Created on: March 2022
# This is the star wars game

import ugame
import stage


def game_scene():
    # main game function

    # grab the image, is image bank for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # 10 x 8 tiles for size 16 x 16
    background = stage.Grid(image_bank_background, 10, 8)

    # create a stage to display background, frame rate 60 fps
    game = stage.Stage(ugame.display, 60)
    # set the layer for background
    game.layers = [background]
    # take layers to show on the screen
    game.render_block()

    # repeat forever, game loop
    while True:
        pass  # just a placeholder now


if __name__ == "__main__":
    game_scene()
