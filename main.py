from pygame import *
from random import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.x < 635:
            self.rect.x += self.speed
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.x < 635:
            self.rect.x += self.speed
        if keys_pressed[K_DOWN] and self.rect.x > 5:
            self.rect.x -= self.speed



win_width = 700
win_height = 500
mw = display.set_mode(
    (win_width, win_height)
)
display.set_caption('ping_pong')
background = transform.scale(
    image.load('background.png'),
    (win_width, win_height)
)


clock = time.Clock()
FPS = 60


mixer.init()
mixer.music.load('music.ogg')
mixer.music.play()


player1 = Player('rocket.png', 10, 50, 5, 20, 150)
player2 = Player('rocket.png', 610, 50, 5, 20, 150)


game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    mw.blit(background, (0, 0))
    player1.reset()
    player1.update()
    player2.reset()
    player2.update()
    display.update()
    clock.tick(FPS)