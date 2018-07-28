import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import wand
import pytest

from deuxmasbot.image import stitcher
from deuxmasbot.image.stitcher import InvalidCoordinateError

# ImageStitcher
def test_assigns_image_on_init():
    the_stitcher = stitcher.ImageStitcher('images/stocking-base.png', [])
    assert isinstance(the_stitcher.image, wand.image.Image)

def test_update_image():
    the_stitcher = stitcher.ImageStitcher('images/stocking-base.png', [])
    img = wand.image.Image(width=50,height=50)
    the_stitcher.update_image(img)

    assert the_stitcher.width is 50 and the_stitcher.height is 50 and the_stitcher.image is img
    
def test_draw_one_sprite():
    the_stitcher = stitcher.ImageStitcher('images/stocking-base.png', [(10, 10)])
    prev_img = the_stitcher.image
    test_sprite = wand.image.Image(filename='images/test-sprite.png')
    the_stitcher.draw_sprite(test_sprite)

    assert the_stitcher.image is not prev_img

def test_draw_given_coordinate():
    the_stitcher = stitcher.ImageStitcher('images/stocking-base.png')
    prev_img = the_stitcher.image
    test_sprite = wand.image.Image(filename='images/test-sprite.png')
    the_stitcher.draw_sprite(test_sprite, (10, 10))

    assert the_stitcher.image is not prev_img

def test_raises_on_bad_coordinate():
    the_stitcher = stitcher.ImageStitcher('images/stocking-base.png')
    prev_img = the_stitcher.image
    test_sprite = wand.image.Image(filename='images/test-sprite.png')

    with pytest.raises(InvalidCoordinateError):
        the_stitcher.draw_sprite(test_sprite)
