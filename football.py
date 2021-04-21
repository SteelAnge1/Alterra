from pygame import *

win_width=600
win_height=500

i_w_1 = 0
i_w_2 = 0

color = (0, 255, 0)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed ):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class  Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 30:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 30:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 30:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 30:
            self.rect.x += self.speed
        
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 30:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 30:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 30:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 30:
            self.rect.x += self.speed

class goal(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, x, y, width, height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height

        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((win_width, win_height))
color1 = (34, 133, 245)

background = transform.scale(image.load("fon.jpg"), (win_width,win_height))

p1 = Player('round.png', win_width/2, 30, 30, 30, 5)

p2 = Player('round.png', win_width/2, win_height - 30, 30, 30, 5)

ball=GameSprite('ball.png', 200, 200, 30, 30, 70)

display.set_caption('ping-pong')

w1 = goal(0, 0, 0, (win_width/2)-100 , 0, 200, 10)

w2 = goal(0, 0, 0, (win_width/2)-100, win_height-10, 200, 10)

font.init()
font = font.SysFont('Arial', 35)

win1 = font.render('FIRST WIN!', True, (204, 186, 51))
win2 = font.render('SECOND WIN!', True, (204, 186, 51))

speed_x=3
speed_y=3

game=True
finish=False

clock=time.Clock()
FPS=60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        p1.update1()
        p2.update2()

        text_win1 = font.render(str(i_w_1), 1, color)
        window.blit(text_win1, (10, 230))

        text_win2 = font.render(str(i_w_2), 1, color)
        window.blit(text_win2, (10, 270))

        if ball.rect.x > win_width-50 or ball.rect.x < 0 or sprite.collide_rect(p1, ball) or sprite.collide_rect(p2, ball):
            speed_x*=-1
            
        if ball.rect.y > win_height-50 or ball.rect.y < 0 or sprite.collide_rect(p1, ball) or sprite.collide_rect(p2, ball):
            speed_y *=-1

        if sprite.collide_rect(ball, w1):
            finish = True
            i_w_2+=1
            window.blit(win1, (300,250))

        if sprite.collide_rect(ball, w2):
            finish = True
            i_w_1+=1
            window.blit(win2, (300,250))

        ball.reset()
        p1.reset()
        p2.reset()
        w1.reset()
        w2.reset()
    else:
        finish=False
        time.delay(1000)
        ball = GameSprite('ball.png', 200, 200, 30, 30, 70)

    display.update()
    clock.tick(FPS)