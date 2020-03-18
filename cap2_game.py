# This is a game where you have to get to the cherry without being touched by the monsters

import pygame
import random

# Initialise game
pygame.init()

# Constants for screen width and height
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680

# Create screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load images for player, enemy and prize
player = pygame.image.load("C:/Users/Jaco-PC/Dropbox/Gerhardus jacobus Steyn-50451/Introduction to Programming/Task 15/player.jpg")
enemy = pygame.image.load("C:/Users/Jaco-PC/Dropbox/Gerhardus jacobus Steyn-50451/Introduction to Programming/Task 15/monster.jpg")
prize = pygame.image.load("C:/Users/Jaco-PC/Dropbox/Gerhardus jacobus Steyn-50451/Introduction to Programming/Task 15/prize.jpg")

# Get dimentions of images
player_height = player.get_height()
player_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

# Storing the positions of the player, enemies and prize
player_x_position = 0
player_y_position = random.randint(0, SCREEN_HEIGHT - player_height)

enemy1_x_position =  SCREEN_WIDTH - enemy_width
enemy1_y_position =  random.randint(0, SCREEN_HEIGHT - enemy_height)
enemy2_x_position =  SCREEN_WIDTH - enemy_width
enemy2_y_position =  random.randint(0, SCREEN_HEIGHT - enemy_height)
enemy3_x_position =  SCREEN_WIDTH - enemy_width
enemy3_y_position =  random.randint(0, SCREEN_HEIGHT - enemy_height)

prize_x_position = SCREEN_WIDTH / 2
prize_y_position = SCREEN_HEIGHT / 2

# Boolean variables to check which key is pressed
keyUp = False
keyDown = False
keyLeft = False
keyRight = False

# Speed and direction of enemies
enemy1_change_x = 0.3
enemy1_change_y = 0.2
enemy2_change_x = 0.15
enemy2_change_y = 0.3
enemy3_change_x = 0.2
enemy3_change_y = 0.15

# Run until the user asks to quit
running = True

while running:
    
    # Fill background
    screen.fill(0)
    screen.blit(player, (player_x_position, player_y_position))
    screen.blit(enemy, (enemy1_x_position, enemy1_y_position))
    screen.blit(enemy, (enemy2_x_position, enemy2_y_position))
    screen.blit(enemy, (enemy3_x_position, enemy3_y_position))
    screen.blit(prize, (prize_x_position, prize_y_position))

    # Update the screen
    pygame.display.flip()

    # Check if user clicks close button on window
    for event in pygame.event.get():

        # If windows close button is clicked, quit the game
        if event.type == pygame.QUIT:
            running = False 

        # Is a button pressed?
        if event.type == pygame.KEYDOWN:

            # Check which key is pressed
            if event.key == pygame.K_UP: 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True

        # Is the button released?
        if event.type == pygame.KEYUP:

            # Check which key is pressed
            if event.key == pygame.K_UP: 
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False

    # What to do when a certain button is pressed?
    if keyUp == True:
        if player_y_position > 0: # Check that player doesn't move off screen
            player_y_position -= 1
    if keyDown == True:
        if player_y_position < SCREEN_HEIGHT - player_height: # Check that player doesn't move off screen
            player_y_position += 1
    if keyLeft == True:
        if player_x_position > 0: # Check that player doesn't move off screen
            player_x_position -= 1
    if keyRight == True:
        if player_x_position < SCREEN_WIDTH - player_width: # Check that player doesn't move off screen
            player_x_position += 1

    # Assign variable to player size
    player_box = pygame.Rect(player.get_rect())

    # Update player_box to stay around player
    player_box.top = player_y_position
    player_box.left = player_x_position

    # Assign variable to enemy size
    enemy1_box = pygame.Rect(enemy.get_rect())
    enemy2_box = pygame.Rect(enemy.get_rect())
    enemy3_box = pygame.Rect(enemy.get_rect())

    # Update enemy#_box to stay around enemy
    enemy1_box.top = enemy1_y_position
    enemy1_box.left = enemy1_x_position
    enemy2_box.top = enemy2_y_position
    enemy2_box.left = enemy2_x_position
    enemy3_box.top = enemy3_y_position
    enemy3_box.left = enemy3_x_position

    # Assign variable to prize size
    prize_box = pygame.Rect(prize.get_rect())

    # Update prize_box to stay around prize
    prize_box.top = prize_y_position
    prize_box.left = prize_x_position

    # Test collision of enemy and player
    if player_box.colliderect(enemy1_box) or player_box.colliderect(enemy2_box) or player_box.colliderect(enemy3_box):
        print("YOU LOSE!")
        pygame.quit()
        exit(0)

    # Test collision of player and prize
    if player_box.colliderect(prize_box):
        print("YOU WIN!")
        pygame.quit()
        exit(0)

    # Move the enemies around
    enemy1_x_position += enemy1_change_x
    enemy1_y_position += enemy1_change_y
    enemy2_x_position += enemy2_change_x
    enemy2_y_position += enemy2_change_y
    enemy3_x_position += enemy3_change_x
    enemy3_y_position += enemy3_change_y

    # Change enemies' direction when wall is hit
    if enemy1_x_position > (SCREEN_WIDTH - enemy_width) or enemy1_x_position < 0:
        enemy1_change_x = enemy1_change_x * -1
    if enemy1_y_position > (SCREEN_HEIGHT - enemy_height) or enemy1_y_position < 0:
        enemy1_change_y = enemy1_change_y * -1

    if enemy2_x_position > (SCREEN_WIDTH - enemy_width) or enemy2_x_position < 0:
        enemy2_change_x = enemy2_change_x * -1
    if enemy2_y_position > (SCREEN_HEIGHT - enemy_height) or enemy2_y_position < 0:
        enemy2_change_y = enemy2_change_y * -1

    if enemy3_x_position > (SCREEN_WIDTH - enemy_width) or enemy3_x_position < 0:
        enemy3_change_x = enemy3_change_x * -1
    if enemy3_y_position > (SCREEN_HEIGHT - enemy_height) or enemy3_y_position < 0:
        enemy3_change_y = enemy3_change_y * -1

pygame.quit()