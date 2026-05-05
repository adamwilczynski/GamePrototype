import numpy as np

tile_codes = np.array([
    [0,0,1,1,1,1,0,0],
    [0,1,2,2,2,2,1,0],
    [1,2,1,1,1,1,2,1],
    [1,2,1,0,0,1,2,1],
    [1,2,1,0,0,1,2,1],
    [1,2,1,1,1,1,2,1],
    [0,1,2,2,2,2,1,0],
    [0,0,1,1,1,1,0,0],
], dtype=np.uint8)

palette = np.array([
    [0, 0, 0],        # 0 -> black
    [34, 177, 76],    # 1 -> green
    [255, 242, 0],    # 2 -> yellow
], dtype=np.uint8)

rgb_tile = palette[tile_codes]

print(rgb_tile)
