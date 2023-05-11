import pygame



class GameClock:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.start_time = pygame.time.get_ticks()

    def update(self):
        self.dt = self.clock.tick_busy_loop(30) / 1000


