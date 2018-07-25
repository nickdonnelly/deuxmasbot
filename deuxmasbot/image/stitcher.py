from enum import Enum

from wand.image import Image
from wand.color import Color
from wand.drawing import Drawing

class ImageSide(Enum):
    Top = 0
    Right = 1
    Bottom = 2
    Left = 4

class ImageStitcher:
   
    def __init__(self, base_image, sprite_coordinates):
        self.image = Image(filename=base_image, background=Color("transparent"))
        self.coords = sprite_coordinates

    def get_dimensions(self):
        return self.image.size

    def update_image(self, img):
        self.image = img
        self.width = img.width
        self.height = img.height

    def draw_sprite(self, sprite, rounded=True):
        sprite.alpha_channel = True
        if rounded:
            with Image(width=sprite.width, height=sprite.height, 
                       background=Color('transparent')) as mask:
                with Drawing() as ctx:
                    ctx.fill_color = Color("black")
                    ctx.rectangle(left=0, top=0, 
                                  width=mask.width, height=mask.height, radius=mask.width / 2)
                    ctx(mask)
                    sprite.composite_channel('all_channels', mask, 'screen')
                    mask.negate()
                    sprite.composite_channel('alpha', mask, 'copy_opacity')

        x, y = self.coords[0]
        del self.coords[0]
        new_image = self.image.clone() 
        new_image.watermark(image=sprite, transparency=0.0, left=x, top=y)
        self.update_image(new_image)
