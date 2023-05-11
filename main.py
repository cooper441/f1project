import setup
import pygame
import pygame_menu
import logic
import game_clock
from colors import *

pygame.init()
driver = setup.driverList[0]
track = setup.trackList[0]
car = setup.carList[1]
clock = game_clock.GameClock()
screen = pygame.display.set_mode((1280, 720))
main_menu = pygame_menu.Menu('Welcome', 400, 300,
                             theme=pygame_menu.themes.THEME_BLUE)
selected_driver = None


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


def display_text(text, size, position, color):
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    text_surface = font.render(text, True, select_color(color))
    text_rect = text_surface.get_rect()
    text_rect.center = position
    screen.blit(text_surface, text_rect)


def count_down():
    for i in range(3, 0, -1):
        screen.fill((0, 0, 0))
        display_text(str(i), 72, (screen.get_width() // 2, screen.get_height() // 2), ANTIQUEWHITE)
        pygame.time.delay(100)

    screen.fill((0, 0, 0))
    display_text("START", 72, (screen.get_width() // 2, screen.get_height() // 2), ANTIQUEWHITE)
    pygame.time.delay(100)


def start_the_game():
    try:
        main_menu.disable()
        main_menu.full_reset()

        player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        start_time = pygame.time.get_ticks()
        logic.start(selected_driver, track)
        count_down()

        while True:
            clock.update()

            events_game = pygame.event.get()
            for e in events_game:
                if e.type == pygame.QUIT:
                    exit()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        main_menu.enable()

                        # Quit this function, then skip to loop of main-menu on line 221
                        return

            if main_menu.is_enabled():
                main_menu.update(events_game)

            screen.fill("purple")

            pygame.draw.circle(screen, "red", player_pos, 40)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                player_pos.y -= 300 * clock.dt
            if keys[pygame.K_s]:
                player_pos.y += 300 * clock.dt
            if keys[pygame.K_a]:
                player_pos.x -= 300 * clock.dt
            if keys[pygame.K_d]:
                player_pos.x += 300 * clock.dt

            display_time(start_time)
            display_text("Press ESC to stop and return to menu", 15,
                         (screen.get_width() // 2, screen.get_height() // 2 - 350),
                         ANTIQUEWHITE)

            pygame.display.flip()
    except NameError:
        main_menu.enable()
        main_menu.full_reset()
        display_text("You have not selected a driver!", 60,
                     (screen.get_width() // 2, screen.get_height() // 2 - 200),
                     RED1)
        pygame.time.delay(3000)


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


def main():
    submenu_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    submenu_theme.widget_font_size = 15
    play_submenu = pygame_menu.Menu('Welcome', 400, 300,
                                    theme=pygame_menu.themes.THEME_BLUE)

    for i in setup.carList:
        play_submenu.add.button(str(i.Driver.FirstName + " " + i.Driver.LastName),
                                action=lambda d=i: set_driver(d))

    play_submenu.add.button('Return to main menu', pygame_menu.events.RESET, font_color=select_color(CYAN4))
    print(type(play_submenu))

    main_menu.add.button('Start',
                         lambda widget: start_the_game(),
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
