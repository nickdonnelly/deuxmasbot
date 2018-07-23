import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import wand

from deuxmasbot.image import stitcher as stitcher

# ImageStitcher
def test_assigns_image_on_init():
    the_stitcher = stitcher.ImageStitcher('images/stocking-base.png', [])
    assert isinstance(the_stitcher.image, wand.image.Image)


