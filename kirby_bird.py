import random
from pgzhelper import *
from pgzrun import go

#definindo o tamanho da tela
WIDTH = 640
HEIGHT = 480
TITLE = 'Flappy Kirby'

#terreno
ground = Actor('background')
#dizendo os limites do eixo x e y
ground.x = 320
ground.y = 465

#kirby
kirby = Actor('kirby1')
kirby.x = 75
kirby.y = 100

#desenhar na tela
def draw():
    #bg é o nome da imagem de background, 0,0 são as coordenadas x e y, pra fazer o desenho do começo da tela
    screen.blit('background', (0,0))
    
    #desenhar o terreno 
    ground.draw()
    #desenhar o placar
    screen.draw.text('Score: ', color=(255, 0, 127), midtop=(50, 10),shadow=(0.5 , 0.5),  scolor=(0,0,0), fontsize=30)
    #desenhar o kirby
    kirby.draw()
    
go()