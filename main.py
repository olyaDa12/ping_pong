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
        if keys_pressed[K_s] and self.rect.y < 635:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y < 635:
            self.rect.y += self.speed
        if keys_pressed[K_DOWN] and self.rect.y > 5:
            self.rect.y -= self.speed

speed_x = 3
speed_y = 3

class Ball(GameSprite):
    def update(self):
        global finish
        global speed_x
        global speed_y
        if finish != True:
            self.rect.x += speed_x
            self.rect.y += speed_y
        if self.rect.y > win_height-50 or self.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player1, self) or sprite.collide_rect(player2, self):
            speed_x *= -1
        if self.rect.x < 0:
            finish = True
            mw.blit(lose1, (200, 200))
        if self.rect.x > 700:
            finish = True
            mw.blit(lose2, (200, 200))



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

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render(
    'PLAYER 1 LOSE!', True, (180, 0, 0)
)
lose2 = font1.render(
    'PLAYER 2 LOSE!', True, (180, 0, 0)
)


player1 = Player('rocket.png', 10, 50, 5, 20, 150)
player2 = Player('rocket.png', 610, 50, 5, 20, 150)

ball = Ball('ball.png', 0, 250, 4, 65, 65)


game = True
finish = False

while game:
    mw.blit(background, (0, 0))
    player1.reset()
    player1.update1()
    player2.reset()
    player2.update2()
    ball.reset()
    ball.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)