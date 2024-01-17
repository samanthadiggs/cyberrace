import pygame
from sys import exit
import math
import os
from spritesheet import SpriteSheet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load()
        self.rect



pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("cyberrace")
clock = pygame.time.Clock() #creates a clock object to tract fps
# test_font = pygame.font.Font(None, 50)
# text_surface = test_font.render("Cyberrace", False, "Green")

#define game varuables
scroll = 0

schoolgirl_run_img = pygame.image.load("Assets/schoolgirl-sidescroller-sprite-assets/sprites-run.png")
schoolgirl_run_sprite_sheet = spritesheet.SpriteSheet(schoolgirl_run_img)
schoolgirl_idle_img = pygame.image.load("Assets/schoolgirl-sidescroller-sprite-assets/sprites-idle.png")
schoolgirl_idle_sprite_sheet = spritesheet.SpriteSheet(schoolgirl_idle_img)
schoolgirl_jump_img = pygame.image.load("Assets/schoolgirl-sidescroller-sprite-assets/sprites-jump_up.png")
schoolgirl_jump_sprite_sheet = spritesheet.SpriteSheet(schoolgirl_jump_img)

BLACK = (0,0,0)

#create animation list
animation_list = []
animation_steps = 8
last_update = pygame.time.get_ticks()
animation_cooldown = 75
frame = 0

def player_run():
    global animation_list
    animation_list.clear()
    for x in range(8):
        animation_list.append(schoolgirl_run_sprite_sheet.get_image(x, 48, 48, 3, BLACK))
    print("player running")
def player_idle():
    global animation_list, frame
    animation_list.clear()
    for x in range(4):
        animation_list.append(schoolgirl_idle_sprite_sheet.get_image(x, 48, 48, 3, BLACK))

def player_jump(length):
    global animation_list, frame
    animation_list.clear()
    i = 0 
    while i < length:
        for x in range(4):
            animation_list.append(schoolgirl_jump_sprite_sheet.get_image(x, 48, 48, 3, BLACK))
        i += 1
    print(f"Jump frame is {frame}, and amination list is {animation_list}")


bg_images = []
for i in range(1,4):
    bg_image = pygame.image.load(f"Assets/cyberpunk-street-files/Version 1/PNG/layers/plx-{i}.png").convert_alpha()
    bg_images.append(bg_image)
bg_width = bg_images[0].get_width() 
<<<<<<< HEAD
bg_height= bg_images[0].get_height() 
=======
bg_height= bg_images[0].get_height()
>>>>>>> 74ad1e9d71751800eb81d66e03e618bf712a0f10
print(bg_width)
tiles = math.ceil(800 / bg_width) * 1

player_surface = pygame.image.load('Assets/SimpleCharacter/Girl.gif').convert_alpha()
player_x_pos = 600
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

music = pygame.mixer.Sound("Assets/banana_shake_hus.mp3")
def draw_bg():
    for x in range(5):
        for i in bg_images:
            screen.blit(i, (x * bg_width + scroll, 0))

#intro screen
   # player_stand = player_idle()


music.play()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_jump(3)
                frame = 0
                print("jump")
                player_gravity = -20
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player_run()
                print("key up")
        else:
            player_run()
        
    #screen.blit(test_surface, (0,0))#put one surface on another
    draw_bg()


    #screen.blit(dog_surface,dog_rect)

    #update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0

    #show frame in animation
    print(f"frame is {frame} and animation list is {len(animation_list)}")
    screen.blit(animation_list[frame], (80, 75))
    # scroll background logic
    scroll -= 5
    #reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    #dog_x_pos -= 1

    #if dog_x_pos < -100:
        #dog_x_pos = 800
    #draw all our elements and update everything
        

    pygame.display.update() #updates the display surface
    clock.tick(60) #the while loop should not run more than 60 fps
