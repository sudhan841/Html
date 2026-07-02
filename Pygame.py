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
    screen.blit(rock_btn(20,500))
    screen.blit(paper_btn(330,500))
    screen.blit(scissor_btn(640,500))

    score = font.render(f"{player} : {computer}",True,(255,255,255))
    screen.blit(score,(380,20))

    for event in pygame.event.get():

     if event.type == pygame.QUIT:
        pygame.quit()
        quit()

     if event.type == pygame.MOUSEBUTTONDOWN:

        x,y = event.pos

        if x<320:
           p="rock"
           screen.blit(rock,(120,200))
        elif x<630:
           p="paper"
           screen.blit(paper,(120,200))
        else:
           p="scissors"
           screen.blit(scissors,(120,200))

        c = random.choice(["rock","paper","scissors"])

        if c=="rock"