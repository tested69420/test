import pygame
from pygame import mixer
import random
score = 0
high_score = 0
jump_hight = -20
pygame.joystick.init()
j = pygame.joystick.Joystick(0)
time = random.randint(1,2)
mixer.init()
music = pygame.mixer.Sound("audio/music.mp3")
mixer.music.set_volume(.03)
music.play(loops = -1)
speed = 4
pygame.init()
screen = pygame.display.set_mode((900,900))
pygame.display.set_caption('ghost hop')
clock = pygame.time.Clock()
background = pygame.image.load('images/background.png').convert_alpha()
background_1 = pygame.image.load('images/sprite_1.png').convert_alpha()
platform = pygame.Surface((900,100))
test_font = pygame.font.Font('font/Pixeltype.ttf',50)
platform.fill((117, 117, 117))
text = test_font.render(('game over'), False, "red")
score_rect = text.get_rect(center =(450, 450))
enemy = pygame.image.load('images/enemy.png').convert_alpha()
enemy_rect = enemy.get_rect(midbottom = (600,800))
player = pygame.image.load('images/player.png').convert_alpha()
player_rect = player.get_rect(midbottom = (100,800))
start = pygame.image.load('images/start_screen.png')
gravity = 0
screen.blit(start,(0,0))
running = True
game_active = False
while running:
 jump_hight += 1
 if jump_hight >= -30:
     jump_hight = -30
 if jump_hight <= -50:
     jump_hight = -50
 if game_active == False:
     enemy_rect.left = 800
     player_rect.bottom = 800
 gravity += 1
 for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and player_rect.bottom <= 800:
            player_rect.bottom = 800
            jump_hight -= 5
        if event.key == pygame.K_SPACE and player_rect.bottom >= 800:
            gravity = jump_hight
            if game_active == False:
                gravity = 0
                enemy_rect.left = 800
                speed = 4
                gravity = 0
                time = random.randint(1, 2)
                game_active = True
                score = 0
                jump_hight = -30
 if game_active == True:
     if time == 1:
         screen.blit(background, (0, 0))
     if time == 2:
         screen.blit(background_1, (0, 0))
     screen.blit(platform, (0, 800))
     screen.blit(player, player_rect)
     screen.blit(enemy, enemy_rect)
     player_rect.y += gravity
     if player_rect.bottom >= 800:
      player_rect.bottom = 800
     if enemy_rect.bottom >= 800:
      enemy_rect.bottom = 800
      enemy_rect.x -= speed
     if enemy_rect.right <= 0:
         enemy_rect.left = 950
         enemy_rect.y = 700
         score += 1
         speed += (speed/2) - speed+random.randint(1,5)

     #game over
     if enemy_rect.colliderect(player_rect):
             game_active = False
             screen.blit(text, score_rect)
             screen.fill('black')
             screen.blit(text, score_rect)
             print ('your score was',score)
             if score > high_score:
                 high_score = score
             print ('your high score is',high_score)

 pygame.display.flip()
 pygame.display.update()

 clock.tick(60)