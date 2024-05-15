from pygame import *

r.png = racket1:
r.png = racket2:

#игровая сцена
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        # Вызываем конструктор класса (Sprite):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (whight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <win_height -80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y <win_height -80:
            self.rect.y += self.speed

racket1 = Player(r.png, 30, 200, 4, 50, 150)
racket2 = Player(r.png, 520, 200, 4, 50, 150)
ball = GameSprite(g.png, 200, 200, 4, 50, 50)

font.init()
font = font.Font(None,35)
lose1 = font.render('потребитель1 не вывез', True,(100,0,0))
lose2 = font.render('потребитель2 не вывез', True,(100,0,0))

speed_x = 3
speed_y = 3


while game:
    for e in event.get():
        if e.tipe == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y


        if sprite.collide_rect(racket1,ball) or sprite.collide_rect (rocket2, ball):
            speed_x *= -1
            speed_y *=  1

        if ball.rect.y > win_height-50 or ball.rect.y <0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))    
            game_over = True


        
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200,200))
            game_over = True



        racket1.reset()
        racket1.reset()
        ball.reset()
            
        

    display.update()
    clock.tick(FPS)
