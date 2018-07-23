from wand.image import Image

class ImageStitcher:
   
    def __init__(self, base_image, sprite_coordinates):
        self.image = Image(filename=base_image)
        self.coords = sprite_coordinates

