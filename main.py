import pygame

pygame.init()

# Each tile will be X pixels, and we'll multiply that size against display_width and display_height for screen size
tile_size = 48
display_width = 10
display_height = 14

# Create the game window
game_display = pygame.display.set_mode((display_width*tile_size, display_height*tile_size))
pygame.display.set_caption("Robo Simulator")

# Initialize the frame-rate clock, this lets it run at 60 FPS
clock = pygame.time.Clock()

# Color palette
light_cyan = (85,255,255)
dark_cyan = (0,170,170)
dark_green = (0,170,0)
light_green = (85,255,85)
magenta = (255,85,255)
dark_magenta = (170,0,170)
black = (0,0,0)

# Load the graphic for our Robomaster
robomaster = pygame.image.load("images/robomaster_48px.png")

# Tile setup, each number can be a different tile, which will each have it's own texture graphic.
# So if you have a list like  game_area = [2,2,2,2]  it would display a row of floor tiles.
blank_tile = 0
wall_tile = 1

# Tile texture setup, each tile number should have it's own graphic.
# aka very cool way to use dictionaries.
tile_textures = {
    blank_tile: pygame.image.load("images/blank.png"),
    wall_tile: pygame.image.load("images/wall.png")
}

# Literally drawing out our map here.
# Probably a better way to do this, but it's kinda fun.
tile_map = [
    [1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,1],
    [1,1,0,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,1,0,0,0,0,1],
    [1,1,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,1,0,0,0,0,1],
    [1,1,1,1,1,0,0,0,0,1],
    [1,1,1,1,1,0,0,0,0,1],
]

# Setup the main simulation loop as a function, then we'll run the function.
# This is handy in case you'd like to make a title screen appear first. Just add it as a function later!
def simulation_loop():

    # Set the start location for the robot
    robot_pos = [((display_width*tile_size)/2)+tile_size,(display_height*tile_size)-tile_size]
    sim_exit = False

    while not sim_exit:

        # Check for events, mainly keypresses and exit-button
        for event in pygame.event.get():

            # Clicking the close button will exit the window now
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # And here we're checking for any keypresses
            elif event.type == pygame.KEYDOWN:

                # So we add X pixels to the Y coordinate of robot's position if UP button is pressed
                if event.key == pygame.K_UP:
                    robot_pos[1] -= tile_size
                elif event.key == pygame.K_DOWN:
                    robot_pos[1] += tile_size
                elif event.key == pygame.K_LEFT:
                    robot_pos[0] -= tile_size
                elif event.key == pygame.K_RIGHT:
                    robot_pos[0] += tile_size

        # Fill the background in with a color
        game_display.fill(dark_cyan)

        # Draw the map from our tile list
        for row in range(display_height):
            for column in range(display_width):
                if tile_map[row][column] == 1:
                    game_display.blit(tile_textures[tile_map[row][column]],(column*tile_size,row*tile_size))

        # Draw the robot onto the screen
        game_display.blit(robomaster,(robot_pos[0], robot_pos[1]))

        # Update the screen, this will keep looping at 60 FPS so the robot will move when the robot_pos variable
        # changes.
        pygame.display.update()
        clock.tick(60)


# Run the simulation
simulation_loop()