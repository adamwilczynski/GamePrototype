from PIL import Image
import numpy as np

from config import TILE_SIZE

from PIL import Image
import numpy as np

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


def rgb(bool_matrix):
    palette = np.array([
        [0, 0, 0],  # Black
        [255, 255, 255],  # White
    ], dtype=np.uint8)
    pass


if __name__ == '__main__':
    for row in read_asset("./assets/player.png"):
        print(row)
