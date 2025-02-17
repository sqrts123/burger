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
prep_text(f"Score: {score}", orange, topleft=(10, 50))
prep_text("Burger Dog", orange, centerx=window_width // 2, y=10)
prep_text(f"Burgers Eaten: {burgers_eaten}", orange, centerx=window_width // 2,y=50)
prep_text(f"Lives: {player_lives}", orange, topright=(window_width - 10, 10))
prep_text(f"Boost: {boost_lv}", orange, topright=(window_width - 10, 50))
prep_text(f"FINAL SCORE: {score}", orange, center=(window_width // 2, window_height // 2))
prep_text("Press any key to play again", orange, center=(window_width // 2, window_height // 2 + 64))

bark_sound = pygame.mixer.Sound("bark_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
pygame.mixer.music.load("bd_background_music.wav")
player_image_right = pygame.image.load("dog_right.png")
player_image_left = pygame.image.load("dog_left.png")

player_image = player_image_left
player_rect = player_image.get_rect()
player_rect.centerx = window_width // 2
player_rect.bottom = window_height

burger_img = pygame.image.load("burger.png")
burger_rect = burger_image.get_rect()
burger_rect.topleft = (random.randint(0, window_width - 32), - buffer_distance)

pygame.mixer.music.play()
running = True
is_paused = False

def check_quit():
    for event in pygame.event.get():
        if event.type = pygame.QUIT:
            running = False
            break

def move_player():
    global player_image
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x = player_rect.x - player_velocity
        player_image = player_image_left
    if keys[pygame.K_RIGHT] and player.rect.right < window_width:
        player_rect.x = player_rect.x + player_velocity
        player_image = player_image_right
    if keys[pygame.K_UP] and player.rect.top > 100:
        player_rect.y = player_rect.y - player_velocity
    if keys[pygame.K_DOWN] and player.rect.bottom < window_height:
        player_rect.y = player_rect.y + player_velocity
    engage_boost(keys)

def engage_boost(keys):
    if keys[pygame.K_SPACE] and boost_level > 0:
        player_velocity = player_boost_velocity
        boost_level = boost_lv
    else:
        player_velocity = player_norm_velocity

def move_burger():
    


def handle_miss():


def check_collisions():


def update_hud():


def check_game_over():


def display_hud():


def handle_clock():


