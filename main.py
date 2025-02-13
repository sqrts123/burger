import random, pygame

pygame.init()

window_width = 800
window_height = 600
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(" ")

FPS = 60
clock = pygame.time.Clock()

player_start_lives  = 3
player_norm_velocity = 5
player_boost_velocity = 10
start_boost_lv = 100
start_burger_velocity = 3
burger_acceleration = 0.5
buff_dist = 100

score = 0
burger_points = 0
burgers_eaten = 0

player_lives = player_start_lives
player_velocity = player_norm_velocity
boost_lv = start_burger_velocity

orange = (255, 100, 0)
black = (0, 0, 0)
white = (255, 255, 255)

font = pygame.font.Font("WashYourHand.ttf", 32)

def prep_text(text, background_color, locations):
    text_to_return = font.render(text, True, background_color)
    rect = text_to_return.get_rect()

    for location in locations:
        if location == "topleft":
            rect.topleft = locations["topleft"]
        elif location == "centerx":
            rect.centerx = locations["centerx"]
        elif location == "y":
            rect.y = locations["y"]
        elif location == "topright":
            rect.topright = locations["topright"]
        elif location == "center":
            rect.center = locations["center"]
    return text_to_return, rect

prep_text(f"Burger Points: {burger_points}", orange, topleft=(10, 10))
