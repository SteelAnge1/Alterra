from pygame import *
from random import randint

win_width=500
win_height=500



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
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 20:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 20:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        a = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350, 370, 390, 410, 430, 450, 470, 490]
        x_r = randint(0, len(a)-1)
        self.rect.x = a[x_r]

        if self.rect.y > win_height:
           self.rect.y = 0

back=(200, 255, 255)
window=display.set_mode((win_width, win_height))
window.fill(back)

enemis = sprite.Group()

for i in range(1, 2):
    ene = Enemy('vector.png', 0, 0, 20, 20, 5)
    ene.add(enemis)



display.set_caption('Just Move')

player = Player('round.png', 20, 250, 20, 20, 5)

game=True
finish=False

clock=time.Clock()
FPS=60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        player.update()

        enemis.update()

        enemis.draw(window)

        player.reset()

        if sprite.spritecollide(player, enemis, True, True):
            finish = True
            
    else:
        finish=False
        time.delay(300)

    display.update()
    clock.tick(FPS)