import numpy as np
import pygame
import config
import utils

from PIL import Image

class ImageArray:
    def __init__(self, filename: str):
        self.image_matrix = utils.create_random_matrix()
        self.transparency_matrix = read_asset(filename)
        self.transparency_matrix = self.rotate_right()

    def updated_image(self, look_direction):
        self._update()
        transparency_matrix = self.transparency_matrix
        if look_direction:
            if look_direction.x < 0:
                transparency_matrix = self.rotate_left()
            if look_direction.x > 0:
                transparency_matrix = self.rotate_right()
            if look_direction.y < 0:
                transparency_matrix = self.rotate_up()
            if look_direction.y > 0:
                transparency_matrix = self.rotate_down()

        return make_surface_rgba(
            utils.rgb(self.image_matrix),
            transparency_matrix
        )

    def _update(self, axis=0):
        self.image_matrix = np.roll(self.image_matrix, 1, axis)

    def rotate_right(self):
        return np.rot90(self.transparency_matrix, k=1)

    def rotate_down(self):
        return np.rot90(self.transparency_matrix, k=2)

    def rotate_left(self):
        return np.rot90(self.transparency_matrix, k=3)

    def rotate_up(self):
        return np.rot90(self.transparency_matrix, k=4)



def read_asset(filename):
    """
    Convert image into a scaled
    False if transparent, True if non-transparent
    """
    img = Image.open(filename).convert('RGBA')
    arr = np.array(img)
    if arr.ndim != 3 or arr.shape[2] != 4:
        raise ValueError("Converted image must be RGBA")
    alpha = arr[:, :, 3]
    binary_mask = (alpha > 0)
    h, w = binary_mask.shape
    scale_h = config.TILE_SIZE / h
    scale_w = config.TILE_SIZE / w
    if not (scale_h == scale_w and scale_h == int(scale_h)):
        raise ValueError("Cannot scale by integer factor")
    scale = int(scale_h)
    new_mask = np.repeat(np.repeat(binary_mask, scale, axis=0), scale, axis=1)
    return new_mask


def create_rgba(rgb_matrix, bool_matrix):
    """
    Convert RGB + boolean mask to RGBA.

    Args:
    rgb_matrix: np.array of shape (width, height, 3), uint8 dtype expected
    bool_matrix: np.array of shape (width, height), boolean

    Returns:
    np.array of shape (width, height, 4)
    """
    alpha = np.where(bool_matrix, 255, 0).astype(np.uint8)[:, :, np.newaxis]
    return np.concatenate((rgb_matrix, alpha), axis=2)


def make_surface_rgba(rgb_matrix, bool_matrix):
    """
    False -> non-transparent True -> transparent
    """
    rgba_matrix = create_rgba(rgb_matrix, bool_matrix)
    # Ensure the array has 4 channels
    shape = rgba_matrix.shape
    surface = pygame.Surface(shape[0:2], pygame.SRCALPHA, 32)

    # Copy the RGB part
    pygame.pixelcopy.array_to_surface(surface, rgba_matrix[:, :, 0:3])

    # Copy the Alpha part
    surface_alpha = np.array(surface.get_view('A'), copy=False)
    surface_alpha[:, :] = rgba_matrix[:, :, 3]
    return surface



