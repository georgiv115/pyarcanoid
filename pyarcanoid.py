import pygame
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((500,500))
window.fill((0,255,255))
black = (0,0,0)
class Area():
    def init(self, x=0, y=0, width=10, height=10, color = None ):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = 'yellow'
    def color(self, new_color):
        self.fill_color = new_color 
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)
    def collidirect(self,rect):
        return self.rect.colliderect(rect)
    
class Picture(Area):
    def init(self, filename, x=0, y=0, width=10, height=10):
        Area.init(self, x=x, y=y, width=width, height=height, color=None)
        self.image1 = pygame.image.load(filename)
    def draw(self):
        #self.fill()
        window.blit(self.image1,(self.rect.x,self.rect.y))

class Label(Area):
    def set_text(self,text,size=350,color=black):
        self.image =  pygame.font.SysFont('verdana',size).render(text,True,color)
    def draw(self,shift_x,shift_y):
        self.fill()
        window.blit(self.image,(self.rect.x+ shift_x,self.rect.y+ shift_y))
monsters = list()
count = 9
start_x = 25
start_y = 50
x = 50
y = 50
for i in range(3):
    x = start_x + i*30
    for j in range(count):
        monster = Picture('enemy.png',x,y,50,50)
        x+= 55
        monsters.append(monster)
    x = 50    
    count -= 1   
    y+= 50
    
   

platform = Picture('platform.png',200,450,50,50)
platform.draw()

ball = Picture('ball.png',225,300,50,50)
ball.draw()

x1 = 0
y1 = 100
move_right = False
move_left = False
speed_y = 3
speed_x = 3

game_over = False
while not game_over:
    platform.fill()
    ball.fill()
    for i in monsters:
        i.draw()
        if i.collidirect(ball.rect):
            monsters.remove(i)
            i.fill()
            speed_y *= -1
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False
    if move_right:
        platform.rect.x += 4
    if move_left:
        platform.rect.x -= 4
    if ball.rect.y > (platform.rect.y + 20):
            time_text = Label(150, 300, 50, 350,black)
            time_text.set_text('YOU LOSE', 60, (255,0,0)) 
            time_text.draw(10,10)
            game_over = True
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.colliderect(platform.rect):
        speed_y *= -1
    if ball.rect.x >= 450:
        speed_x *= -1
    if ball.rect.x <= 10:
        speed_x *= -1
    if ball.rect.y <= 0:
        speed_y *= -1
    if len(monsters) == 0:
        time_text = Label(150, 300, 50, 350,black)
        time_text.set_text('YOU WIN', 60, (255,0,0))
        time_text.draw(10,10)
        game_over = True
        
    platform.draw()
    ball.draw()
    pygame.display.update()
    clock.tick(40)