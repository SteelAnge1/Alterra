from pygame import *

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
    def updater(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_width:
           self.rect.x = randint(0, win_height)
           self.rect.y = randint(0, win_height)

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

back=(200, 255, 255)
window=display.set_mode((win_width, win_height))
window.fill(back)

display.set_caption('Altera')

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

        player.reset()
    else:
        finish=False
        time.delay(300)

    display.update()
    clock.tick(FPS)