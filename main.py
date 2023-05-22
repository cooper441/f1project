import setup
import pygame
import pygame_menu
import Track
import game_clock
import time
import datetime
from colors import *

pygame.init()
driver = setup.driverList[0]
track = setup.trackList[0]
car = setup.carList[1]
clock = game_clock.GameClock()
screen = pygame.display.set_mode((1280, 720))
main_menu = pygame_menu.Menu('Welcome', 800, 600,
                             theme=pygame_menu.themes.THEME_BLUE)
main_menu.add.text_input('Number of Laps: ', default='1', onchange=lambda x: set_number_of_laps(x))

selected_driver = None
time_scale = 10
SIMULATED_TIME_SCALE = 10
laps_to_complete = 1


def select_color(color):
    return tuple(RGB.rgb_format(color))


def display_time(start_time):
    font = pygame.font.Font(None, 36)
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    minutes, remainder = divmod(elapsed_time, 60000)  # Convert milliseconds to minutes and remainder
    seconds, ms = divmod(remainder, 1000)  # Convert remainder to seconds and milliseconds
    time_display = f"{minutes:02}:{seconds:02}.{ms // 10:02}"  # Format the time string
    internal_time = elapsed_time

    text = font.render(f"Time Elapsed: {time_display}", True, (0, 0, 0))

    screen.blit(text, (20, 20))

    return internal_time


def display_laps(laps_completed, total_laps):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Laps Completed: {laps_completed}/{total_laps}", True, (0, 0, 0))
    screen.blit(text, (20, 60))


def display_current_lap_progress(car_position, track_length):
    font = pygame.font.Font(None, 36)
    remaining_length = round(track_length - car_position)
    text = font.render(f"Remaining Lap Distance: {remaining_length}", True, (0, 0, 0))
    screen.blit(text, (20, 100))


def display_text(text, size, position, color):
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    text_surface = font.render(text, True, select_color(color))
    text_rect = text_surface.get_rect()
    text_rect.center = position
    screen.blit(text_surface, text_rect)


def display_multiline_text(text, size, position, color, line_spacing=1.5):
    words = text.split(' ')
    lines = ['']
    line_index = 0

    font = pygame.font.Font(pygame.font.get_default_font(), size)

    # Break words into multiple lines
    for word in words:
        temp_line = lines[line_index] + ' ' + word
        text_surface = font.render(temp_line, True, select_color(color))

        # If line is too long, start a new line
        if text_surface.get_width() > screen.get_width() - 40:  # 40 is for a margin on both sides
            lines.append(word)
            line_index += 1
        else:
            lines[line_index] = temp_line

    # Display each line
    for index, line in enumerate(lines):
        text_surface = font.render(line, True, select_color(color))
        text_rect = text_surface.get_rect()
        line_pos = (position[0], position[1] + index * size * line_spacing)
        text_rect.center = line_pos
        screen.blit(text_surface, text_rect)


def display_fuel(fuel_level):
    font = pygame.font.Font(None, 36)

    text = font.render(f"Fuel: ", True, (0, 0, 0))
    screen.blit(text, (20, 140))

    # Bar dimensions
    bar_width = 100
    bar_height = 10

    # Calculate fuel percentage
    fuel_percentage = fuel_level / 100

    # Draw the background of the bar
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(80, 140, bar_width, bar_height))

    # Draw the fuel level on top of the background
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(80, 140, fuel_percentage * bar_width, bar_height))


def count_down():
    for i in range(3, 0, -1):
        screen.fill((0, 0, 0))
        display_text(str(i), 72, (screen.get_width() // 2, screen.get_height() // 2), ANTIQUEWHITE)
        pygame.display.flip()
        pygame.time.delay(1)

    screen.fill((0, 0, 0))
    display_text("START", 72, (screen.get_width() // 2, screen.get_height() // 2), ANTIQUEWHITE)
    pygame.display.flip()
    pygame.time.delay(1)


def change_attribute(d, attr, new_value):
    try:
        if attr in ['FirstName', 'LastName', 'Abbrev', 'Nat', 'Team']:
            setattr(d.Driver, attr, new_value)
        else:
            setattr(d.Driver, attr, float(new_value))
    except Exception as e:
        print(f"Couldn't change attribute. Error: {str(e)}")


def create_driver_menu(d):
    driver_menu = pygame_menu.Menu('Attributes', 800, 600,
                                   theme=pygame_menu.themes.THEME_BLUE)

    for attr, value in vars(d.Driver).items():
        driver_menu.add.text_input(f'{attr} : ', default=str(value),
                                   onchange=lambda new_value, attr=attr: change_attribute(d, attr, new_value))

    driver_menu.add.button('Start Game',
                           lambda widget: start_the_game(False, driver_menu),
                           pygame.font.Font(pygame_menu.font.FONT_FRANCHISE, 30),
                           font_color=(0, 255, 0))

    driver_menu.add.button('Return', pygame_menu.events.BACK)

    while True:
        clock.update()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if driver_menu.is_enabled():
            driver_menu.mainloop(screen, main_background)

        pygame.display.flip()
        return driver_menu


def start_the_game(sim_state: bool, menu_to_disable=None):
    global laps_to_complete
    push_level = 5
    base_increment_value = 10
    base_fuel_consumption = 0.0025

    increment_value = base_increment_value
    fuel_consumption = base_fuel_consumption

    try:
        car_image = pygame.image.load('racecar.png').convert_alpha()
        car_image = pygame.transform.scale(car_image, (50, 50))
        car_image_rect = car_image.get_rect()
        car_image_rect.center = (screen.get_width() // 2, screen.get_height() // 2)

        selected_driver.FuelLevel = 100

        if menu_to_disable:
            menu_to_disable.disable()
            menu_to_disable.full_reset()

        main_menu.disable()
        main_menu.full_reset()

        display_multiline_text("Only one car is available, this has been set automatically!", 60,
                               (screen.get_width() // 2, screen.get_height() // 2 - 200),
                               RED1)
        pygame.display.flip()
        pygame.time.delay(1000)

        count_down()
        track.car_position = {selected_driver: 0}
        laps_completed = 0
        start_time = pygame.time.get_ticks()

        current_segment_index = 0
        current_segment = track.track_segments[current_segment_index]
        print(current_segment.length)

        processed_segment = False  # Flag variable to track whether the current segment has been processed

        while True:
            if sim_state:
                print("Feature not implemented")
                # simulated_time += 1 / SIMULATED_TIME_SCALE  # simulated time moves slower
                # if track.car_position[selected_driver] <= track.total_length:
                #     increment_value = 5 * SIMULATED_TIME_SCALE  # car moves faster in simulated state
                #     track.car_position[selected_driver] += increment_value
                # else:
                #     track.car_position[selected_driver] = 0  # reset car position to start of track
                #     laps_completed += 1  # increment laps completed
                #     if laps_completed >= laps_to_complete:
                #         minutes, remainder = divmod(simulated_time,
                #                                     60000)  # Convert simulated time to minutes and remainder
                #         seconds, ms = divmod(remainder, 1000)  # Convert remainder to simulated seconds and milliseconds
                #         time_display = f"{minutes:02}:{seconds:02}.{ms // 10:02}"  # Format the time string
                #         print("finished" + " in " + str(time_display))
                #         main_menu.enable()
                #         break
            else:
                clock.update()

                if track.car_position[selected_driver] <= track.total_length:

                    if track.car_position[selected_driver] >= current_segment.length and not processed_segment:

                        current_segment_index = (current_segment_index + 1) % len(track.track_segments)
                        current_segment = track.track_segments[current_segment_index]


                    else:
                        processed_segment = False

                    if isinstance(current_segment, Track.Corner):
                        increment_value /= 3

                    track.car_position[selected_driver] += increment_value
                    selected_driver.FuelLevel -= fuel_consumption

                else:
                    track.car_position[selected_driver] = 0
                    laps_completed += 1
                    if laps_completed >= laps_to_complete:
                        main_menu.enable()
                        break

                if selected_driver.FuelLevel <= 0:
                    main_menu.enable()
                    break

                events_game = pygame.event.get()
                for e in events_game:
                    if e.type == pygame.QUIT:
                        exit()
                    elif e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_ESCAPE:
                            main_menu.enable()
                            return
                        elif e.key == pygame.K_UP:
                            push_level = min(10, push_level + 1)
                        elif e.key == pygame.K_DOWN:
                            push_level = max(1, push_level - 1)

                if main_menu.is_enabled():
                    main_menu.update(events_game)

                screen.fill("purple")

                display_time(start_time)
                display_laps(laps_completed, laps_to_complete)
                display_current_lap_progress(track.car_position[selected_driver], track.total_length)
                display_fuel(selected_driver.FuelLevel)
                display_text("Press ESC to stop and return to menu", 15,
                             (screen.get_width() // 2, screen.get_height() // 2 - 350),
                             ANTIQUEWHITE)
                increment_value = base_increment_value * push_level
                fuel_consumption = base_fuel_consumption * push_level

                brightness_factor = push_level / 10.0
                bright_car_image = car_image.copy()
                bright_car_image.fill(
                    (brightness_factor * 255, brightness_factor * 255, brightness_factor * 255, 255),
                    special_flags=pygame.BLEND_RGBA_MULT)
                screen.blit(bright_car_image, car_image_rect)

                display_text(f"Push Level: {push_level}", 36,
                             (screen.get_width() // 2, screen.get_height() // 2 + 200),
                             ANTIQUEWHITE)

                instructions = "Use UP and DOWN arrow keys to change push level and speed.\nHigher push level " \
                               "increases speed and fuel consumption."
                display_multiline_text(instructions, 18, (screen.get_width() // 2, screen.get_height() - 100),
                                       ANTIQUEWHITE)

                elapsed_time = pygame.time.get_ticks() - start_time

                minutes, remainder = divmod(elapsed_time, 60000)  # Convert milliseconds to minutes and remainder
                seconds, ms = divmod(remainder, 1000)  # Convert remainder to seconds and milliseconds
                time_display = f"{minutes:02}:{seconds:02}.{ms // 10:02}"  # Format the time string

                pygame.display.flip()



    except AttributeError:
        display_text("You have not selected a driver!", 60,
                     (screen.get_width() // 2, screen.get_height() // 2 - 200),
                     RED1)
        pygame.display.flip()
        pygame.time.delay(1)
        main_menu.enable()
        main_menu.full_reset()


def main_background() -> None:
    screen.fill(select_color(CORNSILK3))

    if selected_driver is None:
        display_text("You have not selected a driver", 15,
                     (screen.get_width() // 2, screen.get_height() // 2 - 350), color=CORNFLOWERBLUE)
    else:
        display_text(f"Selected driver is {selected_driver.Driver.FirstName} {selected_driver.Driver.LastName}", 15,
                     (screen.get_width() // 2, screen.get_height() // 2 - 350), color=CORNFLOWERBLUE)


def set_driver(d):
    global selected_driver
    selected_driver = d
    main_menu.enable()
    main_menu.full_reset()


def set_driver_and_open_menu(d):
    set_driver(d)
    driver_menu = create_driver_menu(d)
    if driver_menu.is_enabled():
        driver_menu.mainloop(screen)


def set_number_of_laps(number_of_laps):
    global laps_to_complete
    try:
        laps_to_complete = int(number_of_laps)
    except ValueError:
        print("Invalid number of laps, defaulting to 1.")
        laps_to_complete = 1


def main():
    main_menu.enable()

    submenu_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    submenu_theme.widget_font_size = 15
    play_submenu = pygame_menu.Menu('Welcome', 800, 600,
                                    theme=pygame_menu.themes.THEME_BLUE)

    for i in setup.carList:
        play_submenu.add.button(str(i.Driver.FirstName + " " + i.Driver.LastName),
                                lambda d=i: set_driver_and_open_menu(d))

    play_submenu.add.button('Return to main menu', pygame_menu.events.RESET, font_color=select_color(CYAN4))

    main_menu.add.button('Start',
                         lambda widget: start_the_game(False),
                         pygame.font.Font(pygame_menu.font.FONT_FRANCHISE, 30))
    main_menu.add.button('Choose Driver', play_submenu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)

    while True:
        clock.update()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if main_menu.is_enabled():
            main_menu.mainloop(screen, main_background)

        pygame.display.flip()


main()

