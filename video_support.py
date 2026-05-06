import pygame
from moviepy import VideoFileClip

def iter_video_frames_timed(path, size=None):
    clip = VideoFileClip(path)
    fps = clip.fps
    next_t = 0.0
    dt = 1.0 / fps

    try:
        while next_t < clip.duration:
            frame = clip.get_frame(next_t)
            surf = pygame.surfarray.make_surface(frame.swapaxes(0, 1))

            if size is not None:
                surf = pygame.transform.smoothscale(surf, size)

            yield surf, dt
            next_t += dt
    finally:
        clip.close()