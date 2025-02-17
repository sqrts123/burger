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
burger_rect.topleft = (random.randint(0, window_width - 32), - buff_dist)

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
    burger_rect.y = burger_rect.y + burger_velocity
    burger_points = int(burger_velocity * (window_height - burger_rect.y + 100))

def handle_miss():
    if burger_rect.y > window_height:
        player_lives = player_lives - 1
        pygame.mixer.music.load("miss_sound.wav")
        burger_rect.topleft = (random.randint(0, window_width - 32), -buff_dist)
        burger_velocity = start_burger_velocity
        player_rect.centerx = window_width // 2
def check_collisions():
    if player_rect.colliderect(burger_rect):
        score = score + burger_points
        burgers_eaten = burgers_eaten + 1
        pygame.mixer.music.load("bark_sound.wav")
        burger_rect.topleft = (random.randint(0, window_width - 32), -buff_dist)
        burger_velocity = burger_velocity + burger_acceleration
        boost_lv = boost_lv + 25
        if boost_lv > start_boost_lv:
            boost_lv = start_boost_lv

def update_hud():
    points_text = font.render("Burger Points: " + str(burger_points), True, orange)
    score_text = font.render("Score: " + str(score), True, orange)
    eaten_text = font.render("Burgers Eaten: " + str(burgers_eaten), True, orange)
    lives_text = font.render("Lives: " + str(player_lives), True, orange)
    boost_text = font.render("Boost: " + str(boost_lv), True, orange)

def check_game_over():
    global game_over_text, is_paused, score, burgers_eaten, player_lives, boost_lv, burger_velocity, running
    if player_lives == 0:
        game_over_text = font.render(f"FINAL SCORE: {score}", True, orange)
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    burgers_eaten = 0
                    player_lives = player_start_lives
                    boost_lv = start_boost_lv
                    burger_velocity = start_burger_velocity
                    pygame.mixer.music.play()
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

def display_hud():
    display_surface.fill(black)
    display_surface.blit(points_text, points_rect)
    pygame.draw.line(display_surface, white, (0, 100), window_width, 100), 3)
    display_surface.blit(player_image, player_rect)
    display_surface.blit(burger_image, burger_rect)

def handle_clock():
    pygame.display.update()
    clock.tick(FPS)

while running:
    check_quit()
    move_player()
    move_burger()
    handle_miss()
    check_collisions()
    update_hud()
    check_game_over()
    display_hud()
    handle_clock()

pygame.quit()


