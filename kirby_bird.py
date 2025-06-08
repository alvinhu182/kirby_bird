import random
from pgzhelper import *
from pgzrun import go

#definindo o tamanho da tela
TITLE = 'Flappy Kirby'
WIDTH = 640
HEIGHT = 480


#terreno
ground = Actor('teste')
#dizendo os limites do eixo x e y
ground.x = 320
ground.y = 465

#kirby
kirby = Actor('kirby')
kirby.x = 75
kirby.y = 100
#as imagens que vão ficar no loop
kirby.images =['kirby','kirby2','kirby3']
#quantos frames por segundo
kirby.fps = 6

# gravity = velocidade que o kirby cai
# speed =velocidade que o kirby move pra cima e pra baixo
gravity = 0.1
kirby.speed = 1
kirby.alive = True

#game over
gameover = Actor('game_over')
gameover.x = 320
gameover.y = 200
gameover.scale = 3

def on_mouse_down():
    #se o kirby estiver vivo, ele vai pular, 6.5 pixel
    if kirby.alive:
        kirby.speed = -6.5
        sounds.jump.play()
    else:
        kirby.alive = True


#update é onde acontece as animações, mudanças de frames
def update():
#     #animação do kirby
    kirby.animate()
    #atualização do movimento do kirby pra baixo mais a velocidade

    # kirby.y = kirby.y + kirby.speed esse codigo é a mesma coisa do de baixo
    kirby.y += kirby.speed
    # kirby.speed = kirby.speed + gravity  mesmo exemplo
    kirby.speed += gravity

    #acaba o jogo se o kirby cair no chão
    if kirby.y > HEIGHT - 40 or kirby.y < 0:
        kirby.alive = False
        sounds.death.play()

#desenhar na tela
def draw():
    #bg é o nome da imagem de background, 0,0 são as coordenadas x e y, pra fazer o desenho do começo da tela
    screen.blit('teste', (0,0))
    
    if kirby.alive :
        #desenhar o terreno
        ground.draw()
        #desenhar o placar
        screen.draw.text('Score: ', color=(255, 0, 127), midtop=(50, 10),shadow=(0.5 , 0.5),  scolor=(0,0,0), fontsize=30)
        #desenhar o kirby
        kirby.draw()
    #qnd o kirby morre
    else:
        
        gameover.draw()
        #posiciona ele no eixo x a 75px e eixo y a 100px
        kirby.x = 75
        kirby.y = 100
        #para o movimento do kirby qnd morre
        gravity = 0
        speed = 0
        screen.draw.text('Score: ', color=(255, 0, 127), midtop=(50, 10),shadow=(0.5 , 0.5),  scolor=(0,0,0), fontsize=30)
        screen.draw.text('click here to play again: ', color=(255, 0, 127), center=(320, 300),shadow=(0.5 , 0.5),  scolor=(0,0,0), fontsize=30)
       
        


go()
