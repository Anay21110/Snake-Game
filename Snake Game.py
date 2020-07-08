#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pygame
import time
import random


# In[3]:


pygame.init()
Clock = pygame.time.Clock()
#Declare the colors using RGB code
orange_color = (255,123,7)
black_color = (0,0,0)
red_color = (213,58,80)
green_color = (0,255,0)
blue_color = (50,153,213)



#Displays windows width and height

display_width = 600
display_height = 400
dis = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake Game')
snake_block = 10
snake_speed = 15


snake_list = []



#Defines the snake structure and position





def snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,orange_color,[x[0],x[1],snake_block,snake_block])
        

def snakegame():
    game_over = False
    game_end = False
    
    #coordinates of the snake
    x1= display_width / 2
    y1= display_height / 2
    # when the snake moves
    x1_change = 0
    y1_change = 0
    
    #defines the length of the snake
    snake_length = []
    Length_of_snake = 1
    
    #the coordinates of the food element
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0)* 10.0
    foody = round(random.randrange(0, display_height - snake_block ) / 10.0) * 10.0
    
    
    
    
    
    
    while not game_over :
        
        while game_end == True:
            #display the score
            
            score = Length_of_snake -1 
            score_font = pygame.font.SysFont("comicsansms" , 35)
            value = score_font.render("Your Score: " + str(score) , True , green_color)
            dis.blit(value,[display_width / 3,display_height / 5])
            pygame.display.update()
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_end = False #game has been ended
                    
        
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                    
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                    
                    
                elif event.key == pygame.K_UP:
                    x1_change = -snake_block
                    y1_change = 0
                    
                elif event.key == pygame.K_DOWN:
                    x1_change = snake_block
                    y1_change = 0
                    
                    
        if x1 >= display_width or x1<0 or y1>= display_height or y1<0: 
            game_end = True
        #updated coordinates with changed positions
        x1 += x1_change
        y1 += y1_change 
        dis.fill(black_color)
        pygame.draw.rect(dis,green_color,[foodx,foody,snake_block,snake_block])
        snake.Head = []
        snake.Head.append(x1)
        snake.Head.append(y1)
        snake_list.append(snake.Head)
        
        
        #when the length of the snake exceeds ,delete the snake_list which will end the game
        if len(snake_list)> Length_of_snake:
            del snake_list[0]
            
        
        #when the snake hits itself,game ends
        for x in snake_list [:-1]:
            if x == snake.Head():
                game_end = True
        snake(snake_block,snake_list)
        
        
                    
                
                
        pygame.display.update()
        
        
        #when the snake hits the food, the length of snake should be incremented by 1
        if x1 == foodx and  y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0)* 10.0
            foody = round(random.randrange(0, display_height - snake_block ) / 10.0) * 10.0
            Length_of_snake +=1
            
            
        Clock.tick(snake_speed)
    
            
        
        
    pygame.quit()
    quit()
        
snakegame()
        
        
        
 


# In[ ]:




