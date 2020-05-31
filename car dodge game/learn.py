import pygame
import random
import os,math

pygame.init()

width=600
height=600
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)



gamewindow=pygame.display.set_mode((width,height))
pygame.display.set_caption("car dodge by Abhishek mishra")
bgimg=pygame.image.load("welcome.jpg")
bgimg=pygame.transform.scale(bgimg,(width,height)).convert_alpha()
bgimg1=pygame.image.load("cartrack.jpg")
bgimg1=pygame.transform.scale(bgimg1,(width,height)).convert_alpha()
block_img = pygame.image.load('apni.png')
block_img=pygame.transform.scale(block_img,(70,70)).convert_alpha()
block_img2 = pygame.image.load('enemy.png')
block_img2=pygame.transform.scale(block_img2,(70,70)).convert_alpha()
 
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,45)

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

def welcome():
    exit_game=False
    while not exit_game:
        gamewindow.fill(white)
        gamewindow.blit(bgimg,(0,0))
        text_screen("Welcome in car dodge game",(black),110,20)
        text_screen("press spacebar to play",(black),110,555)
        
        
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                    

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        #pygame.mixer.music.load('')
                        #pygame.mixer.music.play()
                        gameloop()
        
        
        pygame.display.update()
        clock.tick(60)

def collision(x,y,obs_x,obs_y):
    distance=math.sqrt((x - obs_x)**2 + (y - obs_y)**2)
    if distance<60:
        return True
    else:
        return False

def gameloop():
    exit_game=False
    game_over=False
    x,y=420,510
    obs_x=random.randint(0,width-200)
    obs_y=10
    score=0
    vel=10
    fps=60

    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")
    with open("highscore.txt" , "r") as f:
        highscore=f.read() 
    while not exit_game:

        if game_over:
            
            with open("highscore.txt" , "w") as f:
                f.write(str(highscore))
            gamewindow.fill(black)
            gamewindow.blit(bgimg,(0,0))
            text_screen("game over, press enter to play again ",red,20,220)
            text_screen("score :"+str(score) ,red,200,250)
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                    

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
        
        else:
    
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT and  x<=width-100:
                        x +=100
                    if event.key==pygame.K_LEFT and x >= 100 :
                        x -=100

            obs_y+=vel
            
            if obs_y>600:
                obs_x=random.randint(0,width-200)
                obs_y=10
                score+=10
                vel+=0.5
                if score >int(highscore):
                        highscore=score

            
            gamewindow.fill(white)
            gamewindow.blit(bgimg1,(0,0))
            gamewindow.blit(block_img2,(obs_x,obs_y))
            #pygame.draw.rect(gamewindow,black,[obs_x,obs_y,60,60])
            
            gamewindow.blit(block_img,(x,y))
            text_screen("score : "+ str(score) + "  highscore: "+str(highscore) , red ,5,5)

            if collision(x,y,obs_x,obs_y):
                game_over=True
        


        pygame.display.update()
        clock.tick(fps)
                    
    pygame.quit()
    quit()
               

welcome()
gameloop()
