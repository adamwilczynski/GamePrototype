import wave
import numpy as np
import pygame


class SpeedControlledBGM:
    def __init__(self, wav_filename, speed=1.0, volume=0.5, channel_id=0):
        self.wav_filename = wav_filename
        self.speed = speed
        self.volume = volume
        self.channel = pygame.mixer.Channel(channel_id)

        self.original_rate, self.original_audio = self._load_wav(wav_filename)
        self.sound = self._build_sound(self.speed)
        self.sound.set_volume(self.volume)

    def _load_wav(self, filename):
        with wave.open(filename, "rb") as wf:
            channels = wf.getnchannels()
            sample_width = wf.getsampwidth()
            sample_rate = wf.getframerate()
            nframes = wf.getnframes()
            raw = wf.readframes(nframes)

        if sample_width != 2:
            raise ValueError("Only 16-bit PCM WAV files are supported")

        audio = np.frombuffer(raw, dtype=np.int16)

        if channels == 2:
            audio = audio.reshape(-1, 2)
        else:
            audio = audio.reshape(-1, 1)

        return sample_rate, audio

    def _resample_audio(self, audio, speed):
        if speed <= 0:
            raise ValueError("speed must be > 0")

        old_length = len(audio)
        new_length = max(1, int(old_length / speed))

        old_indices = np.arange(old_length)
        new_indices = np.linspace(0, old_length - 1, new_length)

        if audio.shape[1] == 1:
            resampled = np.interp(new_indices, old_indices, audio[:, 0]).astype(np.int16)
            return resampled.reshape(-1, 1)
        else:
            left = np.interp(new_indices, old_indices, audio[:, 0])
            right = np.interp(new_indices, old_indices, audio[:, 1])
            return np.stack([left, right], axis=1).astype(np.int16)

    def _build_sound(self, speed):
        resampled = self._resample_audio(self.original_audio, speed)

        mixer_info = pygame.mixer.get_init()
        if mixer_info is None:
            raise RuntimeError("pygame.mixer is not initialized")

        frequency, size, channels = mixer_info

        if size != -16:
            raise ValueError("This example expects pygame.mixer.init(..., size=-16)")

        if channels != resampled.shape[1]:
            raise ValueError(
                f"Mixer channels ({channels}) do not match WAV channels ({resampled.shape[1]})"
            )

        return pygame.sndarray.make_sound(np.ascontiguousarray(resampled))

    def play(self):
        self.channel.play(self.sound, loops=-1)

    def stop(self):
        self.channel.stop()

    def set_speed(self, new_speed):
        was_playing = self.channel.get_busy()
        self.stop()
        self.speed = new_speed
        self.sound = self._build_sound(self.speed)
        self.sound.set_volume(self.volume)
        if was_playing:
            self.play()

    def set_volume(self, volume):
        self.volume = max(0.0, min(1.0, volume))
        self.sound.set_volume(self.volume)

# pygame.init()
# pygame.mixer.init(frequency=44100, size=-16, channels=2)
#
# screen = pygame.display.set_mode((700, 200))
# clock = pygame.time.Clock()
# font = pygame.font.SysFont(None, 32)
#
# bgm = SpeedControlledBGM("./assets/core_ambient.wav", speed=1.0, volume=0.5)
# bgm.play()
#
# speed = 1.0
# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 speed = min(10.0, speed + 0.1)
#                 bgm.set_speed(speed)
#             elif event.key == pygame.K_DOWN:
#                 speed = max(0.1, speed - 0.1)
#                 bgm.set_speed(speed)
#
#     screen.fill((20, 20, 30))
#     txt = font.render(f"Speed: {speed:.1f}  (UP/DOWN)", True, (240, 240, 240))
#     screen.blit(txt, (40, 80))
#     pygame.display.flip()
#     clock.tick(60)
#
# pygame.quit()