from enum import Enum

from wand.image import Image

class ImageSide(Enum):
    Top = 0
    Right = 1
    Bottom = 2
    Left = 4

class ImageStitcher:
   
    def __init__(self, base_image, sprite_coordinates):
        self.image = Image(filename=base_image)
        self.coords = sprite_coordinates

    def get_dimensions(self):
        return self.image.size

    def update_image(self, img):
        self.image = img
        self.width = img.width
        self.height = img.height

    def draw_sprite(self, sprite):
        x, y = self.coords[0]
        del self.coords[0]
        new_image = self.image.clone() 
        new_image.watermark(image=sprite, transparency=0.0, left=x, top=y)
        self.update_image(new_image)
