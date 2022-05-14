#importing packages for the game to run
import pygame
import os
import time
import random

#random comment
#window setup
WIDTH, HEIGHT = 400, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

#Adding in the images as variables 
#enemy ships and their location
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "gameu_ship_red.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "gameu_ship_green.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "gameu_ship_blue.png"))

#player Ship yay!
PLAYER_SHIP = pygame.image.load(os.path.join("assets", "gameu_ship_player.png"))

PLAYER_LASER = pygame.image.load(os.path.join("assets", "gameu_laser_white.png"))

#Background

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "gameu_background2.png")), (WIDTH, HEIGHT))

#This class will be used for both enemy and player ships
class Ship:
  def __init__(self, start_x, start_y):
    self.x = start_x
    self.y = start_y
    self.ship_img = None

  def draw(self, window):
    window.blit(self.ship_img,(self.x, self.y))

#Initializing the Player
class Player(Ship):
  def __init__(self, x, y):
    super().__init__(x,y)
    self.ship_img = PLAYER_SHIP

#Initializing laser
class Laser():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.collision = None
    self.move_away = False

#drawing the laser
    def draw(self, window):
      self.collision = pygame.Rect(self.x + 15, self.y + 5, 4, 20)
      pygame.draw.rect(window, (255,255,255), self.collision)
      window.blit(PLAYER_LASER (self.x, self.y))

     #BYE!!!!! Stopped here 05/09/2022
      
      

