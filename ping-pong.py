back = (200 , 255 , 255) 
win_width = 600 
window = display.set_mode ((win_width , win_heigt))  
window.fill(back) 

game = True 
finsh = False 
clock = time.Clock () 
FPS = 60 

#мяч и рокетка 
racket1 = Player('racket.png ' , 30 , 200 , 4 , 50 , 150 ) 
racket2 = Player('racket.png' , 520 ,200 , 4 , 50 , 150 ) 
ball  = GameSprite('tenis_ball.png ' , 200 , 200 , 4 , 50 , 50) 

font.init() 
font = font.sysFont("Areal" , 35 ) 
lose1 = font.SysFont('PLAYER 1 LOSE ' , True , (180 , 0 , 0)
lose2 = font.render('PLAYER 2 LOSE' , True , (180 , 0 , 0 ) l

speed_x -
speed_y - 

while game: 
    for e in event.get() : 
        if e.type == QUIT:
            game = False 
    
if finish != True: 
    window.fill(back) 
    racket1.update_I() 
    racket2.update_R()  

    if sprite.collide_rect(racket) 
    if ball.rect.y > win heigt -50 or ball.rect.y < 0 :
        speed_y *= -1 

    if ball.rect.x > win_width: 
        finish = True
        window.blit(lose2 , (200 , 200)) 
         
    racket1.reset() 
    racket2.reset() 
    ball.reset() 

    display.update() 
    clock.tick(FPS)
 