import setup
import pygame
import pygame_menu
import logic
from colors import *

driver = setup.driverList[0]
track = setup.trackList[0]
car = setup.carList[1]

clock = pygame.time.Clock()
dt = 0
last_action_time = pygame.time.get_ticks()
interval = 10
main_menu = pygame_menu.Menu



def select_color(color):
    return (str(RGB.rgb_format(color)))

print(type(select_color(CORNFLOWERBLUE)))
print(select_color(CORNFLOWERBLUE))

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


def display_text(text, size, position, screen, color):
    c = select_color(color)
    print(c)
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    text_surface = font.render(text, True, (100, 149, 237))
    text_rect = text_surface.get_rect()
    text_rect.center = position
    screen.blit(text_surface, text_rect)
    pygame.display.flip()


def count_down(screen):
    for i in range(3, 0, -1):
        screen.fill((0, 0, 0))
        display_text(str(i), 72, (screen.get_width() // 2, screen.get_height() // 2), screen)
        pygame.time.delay(100)

    screen.fill((0, 0, 0))
    display_text("START", 72, (screen.get_width() // 2, screen.get_height() // 2), screen)
    pygame.time.delay(100)


def set_difficulty(value, difficulty):
    # Do the job here !
    pass


def start_the_game(*args):
    global main_menu
    global screen
    global clock
    global selected_driver

    main_menu.disable()
    main_menu.full_reset()

    count_down(screen)
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    start_time = pygame.time.get_ticks()
    logic.start(selected_driver, track)
    while True:
        clock.tick_busy_loop(30) / 1000

        #logic


        # Application events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    main_menu.enable()

                    # Quit this function, then skip to loop of main-menu on line 221
                    return

        if main_menu.is_enabled():
            main_menu.update(events)

        screen.fill("purple")

        pygame.draw.circle(screen, "red", player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        display_time(start_time)
        display_text("Press ESC to stop and return to menu", 15,
                     (screen.get_width() // 2, screen.get_height() // 2 - 350),
                     screen, color="chartreuse1")

        # flip() the display to put your work on screen
        pygame.display.flip()


def main_background() -> None:
    global screen
    """
    Function used by menus, draw on background while menu is active.
    """

    screen.fill((255, 255, 255))

    if 'selected_driver' in globals():
        display_text(f"Selected driver is {selected_driver.Driver.FirstName} {selected_driver.Driver.LastName}", 15,
                     (screen.get_width() // 2, screen.get_height() // 2 - 350),
                     screen, color=CORNFLOWERBLUE)
    else:
        display_text("You have not selected a driver", 15,
                     (screen.get_width() // 2, screen.get_height() // 2 - 350),
                     screen, color=CORNFLOWERBLUE)


def set_driver(driver):
    global selected_driver
    selected_driver = driver
    print(selected_driver.Driver.Abbrev)


def main():
    pygame.init()
    global dt
    global clock
    global screen
    global main_menu
    global selected_driver

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    main_menu = pygame_menu.Menu('Welcome', 400, 300,
                                 theme=pygame_menu.themes.THEME_BLUE)

    submenu_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    submenu_theme.widget_font_size = 15
    play_submenu = pygame_menu.Menu('Welcome', 400, 300,
                                    theme=pygame_menu.themes.THEME_BLUE)

    for i in setup.carList:
        play_submenu.add.button(str(i.Driver.FirstName + " " + i.Driver.LastName),
                                action=lambda driver=i: set_driver(driver))

    play_submenu.add.button('Return to main menu', pygame_menu.events.RESET)

    main_menu.add.button('Start',
                         start_the_game,
                         pygame.font.Font(pygame_menu.font.FONT_FRANCHISE, 30))
    main_menu.add.button('Choose Driver', play_submenu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)

    while True:

        # Tick
        dt = clock.tick_busy_loop(30) / 1000

        # Paint background

        main_background()

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        # Main menu
        if main_menu.is_enabled():
            main_menu.mainloop(screen, main_background)

        # Flip surface
        pygame.display.flip()


main()
