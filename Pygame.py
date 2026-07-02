import pygame, random

pygame.init()

screen = pygame.display.set_mode((960,640))
pygame.display.set_caption("Rock Paper Scissors")

bg = pygame.image.load("Game.jpng")

rock_btn = pygame.image.load("Rock button.jpng")
paper_btn = pygame.image.load("Paper button.jpng")
scissor_btn = pygame.image.load("Scissor buttons.jpng")

rock = pygame.image.load("Rock")
paper = pygame.image.load("Paper")
scissors = pygame.image.load("Scissor")

font = pygame.font.Font("Splatch.ttf",70)

player = computer = 0

while True:

    screen.blit(bg,(0,0))