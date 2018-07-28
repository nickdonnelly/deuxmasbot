from enum import Enum

from wand.image import Image
from wand.color import Color
from wand.drawing import Drawing

class ImageStitcher:
   
    def __init__(self, base_image, sprite_coordinates = []):
        self.image = Image(filename=base_image, background=Color("transparent"))
        self.coords = sprite_coordinates

    def get_dimensions(self):
        return self.image.size

    def update_image(self, img):
        self.image = img
        self.width = img.width
        self.height = img.height

    def draw_sprite(self, sprite, position=-1, rounded=True):
        sprite.alpha_channel = True
        if rounded:
            with Image(width=sprite.width, height=sprite.height, 
                       background=Color('transparent')) as mask:
                with Drawing() as ctx:
                    if rounded:
                        ctx.fill_color = Color("black")
                        ctx.rectangle(left=0, top=0, 
                                      width=mask.width, height=mask.height, radius=mask.width / 2)
                        ctx(mask)
                    sprite.composite_channel('all_channels', mask, 'screen')
                    mask.negate()
                    sprite.composite_channel('alpha', mask, 'copy_opacity')

        x, y = self.__get_coordinate(position)
        new_image = self.image.clone() 
        new_image.watermark(image=sprite, transparency=0.0, left=x, top=y)
        self.update_image(new_image)

    def __get_coordinate(self, position):
        if len(self.coords) is 0 and position == -1:
            raise InvalidCoordinateError('No coordinates provided and none left in initializer')

        if position == -1:
            x, y = self.coords[0]
            del self.coords[0]
        else:
            x, y = position

        return x, y


class InvalidCoordinateError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, *kwargs)
