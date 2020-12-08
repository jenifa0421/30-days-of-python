import pygame,sys
import random




#GENERAL SETUP
pygame.init()
clock=pygame.time.Clock()

#MAIN WINDOW


global ball_speed_x
global ball_speed_y
global ball
ball_speed_x=7 
ball_speed_y=7
player_speed=0
opponent_speed=7

screen_width=1000
screen_height=500
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("PONG GAME")

ball=pygame.Rect(screen_width/2-15,screen_height/2-15,30,30)
player=pygame.Rect(screen_width-20,screen_height/2-70,10,140)
opponent=pygame.Rect(10,screen_height/2-70,10,140)
bg_color=pygame.Color('grey12')
light_grey=(200,200,200)




while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                player_speed+=7
            if event.key == pygame.K_UP:
                player_speed-=7
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_DOWN:
                player_speed-=7
            if event.key == pygame.K_UP:
                player_speed+=7


    #BALL ANIMATION

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    #PLAYER ANIMATION
    # TO PREVENT PLAYER FROM GOING OUTSIDE OF THE SCREEN

    player.y+=player_speed
    if player.top<=0:
        player.top=0
    if player.bottom>=screen_height:
        player.bottom=screen_height

    # OPPONENT ANIMATION

    if opponent.top<ball.y:
        opponent.top+=opponent_speed
    if opponent.bottom>ball.y:
        opponent.bottom-=opponent_speed


    # TO PREVENT OPPONENT FROM GOING OUTSIDE OF THE SCREEN
    opponent.y += player_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height





    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))


    pygame.display.flip()
    clock.tick(60)

