import numpy as np

import config

def create_random_matrix():
    return np.random.choice([False, True], size=(config.TILE_SIZE, config.TILE_SIZE))


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





if __name__ == '__main__':
    pass
