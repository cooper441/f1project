import pygame


class GameClock:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.start_time = pygame.time.get_ticks()

    def update(self):
        self.dt = self.clock.tick_busy_loop(30) / 1000



# start_time = time.perf_counter()
# elapsed_time = 0
# track.car_position = {selected_driver: 0}
# simulation_speed = 2  # Increase this value to make the simulation run faster
#
# while True:
#     elapsed_time = time.perf_counter() - start_time
#
#     if track.car_position[selected_driver] < track.total_length:
#         increment_value = 1
#         track.car_position[selected_driver] += increment_value
#     else:
#         formatted_time = str(datetime.timedelta(seconds=int(elapsed_time)))
#         print("finished" + " in " + str(formatted_time))
#         break
#
#     time.sleep(0.10)  # Pause for 0.10 seconds (real-time)
#
#     # Adjust the elapsed time to account for the simulation speed
#     elapsed_time *= simulation_speed