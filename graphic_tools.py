from PIL import Image
import numpy as np

import numpy
import pygame

def read_asset(filename):
    """False if transparent, True if non-transparent"""
    img = Image.open(filename).convert('RGBA')
    arr = np.array(img)
    if arr.ndim != 3 or arr.shape[2] != 4:
        raise ValueError("Converted image must be RGBA")
    alpha = arr[:,:,3]
    binary_mask = (alpha > 0)
    h, w = binary_mask.shape
    scale_h = 64 / h
    scale_w = 64 / w
    if not (scale_h == scale_w and scale_h == int(scale_h)):
        raise ValueError("Cannot scale to 64x64 by integer factor")
    scale = int(scale_h)
    new_mask = np.repeat(np.repeat(binary_mask, scale, axis=0), scale, axis=1)
    return new_mask


def rgb(bool_matrix, debug: bool=False):
    palette = np.array([
        [0, 0, 0],  # Black
        [255, 255, 255],  # White
    ], dtype=np.uint8)

    rgb_values = palette[bool_matrix.astype(np.uint8)]

    if debug:
        # Set frame borders to True
        rgb_values[0, :] = True  # Top row
        rgb_values[-1, :] = True  # Bottom row
        rgb_values[:, 0] = True  # Left column
        rgb_values[:, -1] = True  # Right column
    return rgb_values


def create_rgba(rgb_matrix, bool_matrix):
    """
    Convert RGB + boolean mask to RGBA.

    Args:
    rgb_matrix: np.array of shape (width, height, 3), uint8 dtype expected
    bool_matrix: np.array of shape (width, height), boolean

    Returns:
    np.array of shape (width, height, 4)
    """
    print(rgb_matrix.shape)
    print(bool_matrix.shape)
    alpha = np.where(bool_matrix, 255, 0).astype(np.uint8)[:, :, np.newaxis]
    return np.concatenate((rgb_matrix, alpha), axis=2)


def make_surface_rgba(rgb_matrix, bool_matrix):
    rgba_matrix = create_rgba(rgb_matrix, bool_matrix)
    print(rgba_matrix.shape)
    # Ensure the array has 4 channels
    shape = rgba_matrix.shape
    surface = pygame.Surface(shape[0:2], pygame.SRCALPHA, 32)

    # Copy the RGB part
    pygame.pixelcopy.array_to_surface(surface, rgba_matrix[:, :, 0:3])

    # Copy the Alpha part
    surface_alpha = numpy.array(surface.get_view('A'), copy=False)
    surface_alpha[:, :] = rgba_matrix[:, :, 3]
    return surface


if __name__ == '__main__':
    for row in read_asset("./assets/player.png"):
        print(row)
