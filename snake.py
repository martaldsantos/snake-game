import pygame
import sys
import random
import numpy as np
from keras import models, layers

#Esta implementaçao tem o problema de poder spwanar uma mça no corpo da snake
#Mudar isso

class Snake():
    def __init__(self, repre):
        self.length = 2
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = up
        self.color = (17, 24, 47)
        self.score = 0
        self.brain = None
        
        
        model = self.make_model()
        model.set_weights(repre)

        self.brain = model

    def make_model(self):
            model = models.Sequential()
            model.add(layers.InputLayer(input_shape=(13,)))
            model.add(layers.Dense(13, activation='relu'))
            model.add(layers.Dense(3, activation='softmax'))
            model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['acc'])
            return model

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point
    
    def lost(self):
        cur = self.get_head_position()
        x,y = self.direction
        new = (((cur[0]+(x*gridsize))%screen_width), (cur[1]+(y*gridsize))%screen_height)

        if cur[0] == 0 or cur[1] == 0 or cur[0] == 440 or cur[1] == 440:
            self.reset()

        elif len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            pass

    def move(self):
        cur = self.get_head_position()
        x,y = self.direction
        new = (((cur[0]+(x*gridsize))%screen_width), (cur[1]+(y*gridsize))%screen_height)

        if cur[0] == 0 or cur[1] == 0 or cur[0] == 440 or cur[1] == 440:
            self.reset()

        elif len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        # self.length = 2
        # self.positions = [((screen_width/2), (screen_height/2))]
        # self.direction = random.choice([up, down, left, right])
        # self.score = 0
        pygame.quit()
        #sys.exit()

    def draw(self,surface):
        for p in self.positions:
            if p == self.get_head_position():
                r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
                pygame.draw.rect(surface, (255,255, 255), r)
                pygame.draw.rect(surface, (255,255, 255), r, 1)
            else:
                r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
                pygame.draw.rect(surface, self.color, r)
                pygame.draw.rect(surface, (93,216, 228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.K_UP:
                pygame.quit()
                sys.exit()

    def get_positions(self):
        return self.positions

    def make_move(self, data, model):
        global last_pos #Alterar pq n é o valor global q queremos, se calhar é

        move = np.argmax(model.predict(np.reshape(data, (1,13))))

        if move == 0: #Forward
            self.turn(last_pos)
            self.move()

        if move == 1: #Left
            if last_pos==up:
                self.turn(left)
                last_pos=left
                self.move()
            elif last_pos==right:
                self.turn(up)
                last_pos=up
                self.move()
            elif last_pos==left:
                self.turn(down)
                last_pos=down
                self.move()
            else:
                self.turn(right)
                last_pos=right
                self.move()
            
        if move == 2: #Right
            if last_pos==up:
                self.turn(right)
                last_pos=right
                self.move()
            elif last_pos==right:
                self.turn(down)
                last_pos=down
                self.move()
            elif last_pos==left:
                self.turn(up)
                last_pos=up
                self.move()
            else:
                self.turn(left)
                last_pos=left
                self.move()

class Food():
    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(1, grid_width-2)*gridsize, random.randint(1, grid_height-2)*gridsize)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if x==0 or x==11 or y==0 or y==11:
                r = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface,(0,0,0), r)
            elif (x+y)%2 == 0:
                r = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface,(93,216,228), r)
            else:
                rr = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface, (84,194,205), rr)

def snake_eyes(snake, food):
    #Placeholder for the final matrix
    space = np.zeros((3,3))

    snake_pos = snake.get_positions()

    head_pos = snake_pos[0]

    food_pos = food.position 

    #Actual values of the squares of the final matrix
    game_board = [[(head_pos[0]-40,head_pos[1]-40),(head_pos[0],head_pos[1]-40),(head_pos[0]+40,head_pos[1]-40)],
                [(head_pos[0]-40,head_pos[1]),head_pos,(head_pos[0]+40,head_pos[1])],
                [(head_pos[0]-40,head_pos[1]+40),(head_pos[0],head_pos[1]+40),(head_pos[0]+40,head_pos[1]+40)]]

    #Values of the border of the game
    border = [(0.0, 0.0),
            (40.0, 0.0),
            (80.0, 0.0),
            (120.0, 0.0),
            (160.0, 0.0),
            (200.0, 0.0),
            (240.0, 0.0),
            (280.0, 0.0),
            (320.0, 0.0),
            (360.0, 0.0),
            (400.0, 0.0),
            (440.0, 0.0),
            (440.0, 40.0),
            (440.0, 80.0),
            (440.0, 120.0),
            (440.0, 160.0),
            (440.0, 200.0),
            (440.0, 240.0),
            (440.0, 280.0),
            (440.0, 320.0),
            (440.0, 360.0),
            (440.0, 400.0),
            (440.0, 440.0),
            (400.0, 440.0),
            (360.0, 440.0),
            (320.0, 40.0),
            (280.0, 440.0),
            (240.0, 440.0),
            (200.0, 440.0),
            (160.0, 440.0),
            (120.0, 440.0),
            (80.0, 440.0),
            (40.0, 440.0),
            (0.0, 440.0),
            (0.0, 400.0),
            (0.0, 360.0),
            (0.0, 320.0),
            (0.0, 280.0),
            (0.0, 240.0),
            (0.0, 200.0),
            (0.0, 160.0),
            (0.0, 120.0),
            (0.0, 80.0),
            (0.0, 40.0)] #Colocar isto noutro file

    for i in range(3): #Iterates through every value of the matrix, replaces with  if there is food and -1 if it is a border square or a snake square
        for j in range(3):
            if game_board[i][j]==food_pos:
                space[i][j]=1
            for k in snake_pos:
                if game_board[i][j]==k:
                    space[i][j]=-1
            for k in border:
                if game_board[i][j]==k:
                    space[i][j]=-1
          

    return space.flatten()

def make_data(vision, last_pos):
    movement = np.zeros(4)
    if last_pos == (0,-1):
        movement[0] = 1
    if last_pos == (0,1):
        movement[1] = 1
    if last_pos == (-1,0):
        movement[2] = 1
    else:
        movement[3] = 1
    return np.concatenate((vision, movement))





screen_width = 480
screen_height = 480

gridsize = 40
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)

last_pos = left

def main(repre):
    fit = 0
     
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake(repre)
    food = Food()

    myfont = pygame.font.SysFont("monospace",16)

    snake.turn(left)
    snake.move()
    movesWithoutApple=0
    scoreplusone = 1 #Just to stop after 50 moves, find better solution later
    
    while (True):
        #clock.tick(0.5)
        snake.handle_keys()
        drawGrid(surface)
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(snake.score), 1, (255,255,255))
        fit = snake.score
        screen.blit(text, (5,10))
        snake.lost()
        data = make_data(snake_eyes(snake,food), last_pos)
        snake.make_move(data, snake.brain)
        try:
            pygame.display.update()
        except:
            return fit
        if snake.score < scoreplusone:
            movesWithoutApple+=1
        else:
            movesWithoutApple = 0
            scoreplusone +=1
        if movesWithoutApple>50:
            return fit
            pygame.quit()