import numpy as np
import time 
import pygame
from functions import celulas_alrrededor,renderizar_matriz
from variables import my_array,negro,ventana


pygame.init()
ventana = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Juego de vida")

ejecutando = True

while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
    ventana.fill(negro)
    for x in range(0,len(my_array)):
      for y in range (0, len(my_array)):
        celulas_vivas_alrrededor=celulas_alrrededor(my_array,x,y)
        if my_array[x][y]==1:
          if (celulas_vivas_alrrededor==2) or (celulas_vivas_alrrededor==3):
            my_array[x][y]=1
          else:
            my_array[x][y]=0
        elif my_array[x][y]==0: 
         if celulas_vivas_alrrededor==3:
            my_array[x][y]=1
    renderizar_matriz(my_array)
    time.sleep(1)
    print(my_array)
    pygame.display.flip()
                    
