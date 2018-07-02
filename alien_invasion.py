import sys
import pygame


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # Set the background color.
    bg_color = (230, 230, 230)

    # Start the main loop of game
    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(bg_color)

        # make the most recently drawn screen available
        pygame.display.flip()

        
run_game()
