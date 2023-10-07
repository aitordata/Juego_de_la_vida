import numpy as np
import time 
import os
import pygame
from variables import columnas,filas,celda_alto,celda_ancho,ventana

def limpiar_consola(): #Limpia la consola
    os.system('clear')


def celulas_alrrededor(my_array,x,y): #Devuelve cuantas células de alrrededor estan vivas 
    if x==0: 
        if y==0:
            resultados_alrrededor=[my_array[x][y+1],my_array[x+1][y],my_array[x+1][y+1]]
            return np.sum(resultados_alrrededor)  
        elif y==len(my_array)-1:
            resultados_alrrededor=[my_array[x][y-1],my_array[x+1][y-1],my_array[x+1][y]]
            return np.sum(resultados_alrrededor)
        else:
            resultados_alrrededor=[my_array[x][y-1],my_array[x+1][y-1],my_array[x+1][y],my_array[x+1][y+1],my_array[x][y+1]]
            return np.sum(resultados_alrrededor) 
    elif x>0 and x<(len(my_array)-1):
        if y==0:
            resultados_alrrededor=[my_array[x-1][y],my_array[x-1][y+1],my_array[x][y+1],my_array[x+1][y+1],my_array[x+1][y]]
            return np.sum(resultados_alrrededor )
        elif y==len(my_array)-1:
            resultados_alrrededor=[my_array[x-1][y],my_array[x-1][y-1],my_array[x][y-1],my_array[x+1][y-1],my_array[x+1][y]]
            return np.sum(resultados_alrrededor)
        else:
            resultados_alrrededor=[my_array[x-1][y], my_array[x-1][y+1],my_array[x][y+1],my_array[x+1][y-1],my_array[x+1][y+1],my_array[x+1][y],my_array[x][y-1],my_array[x-1][y-1]]
            return np.sum(resultados_alrrededor) 
    elif x==len(my_array)-1:
        if y==0:
            resultados_alrrededor=[my_array[x-1][y],my_array[x-1][y+1],my_array[x][y+1]]
            return np.sum(resultados_alrrededor)
        elif y==len(my_array)-1:
            resultados_alrrededor=[my_array[x-1][y],my_array[x-1][y-1],my_array[x][y-1]]
            return np.sum(resultados_alrrededor) 
        else:
            resultados_alrrededor=[my_array[x][y-1],my_array[x-1][y-1],my_array[x-1][y],my_array[x-1][y+1],my_array[x][y+1]]
            return np.sum(resultados_alrrededor) 

def renderizar_matriz(my_array): #función realizada con chat gpt 
    for fila in range(filas):
        for columna in range(columnas):
            valor = my_array[fila][columna]
            pygame.draw.rect(ventana, (0, 0, 0), (columna * celda_ancho, fila * celda_alto, celda_ancho, celda_alto))
            texto = pygame.font.Font(None, 36).render(str(valor), True, (255, 255, 255))
            ventana.blit(texto, (columna * celda_ancho + celda_ancho // 2 - texto.get_width() // 2,
                                 fila * celda_alto + celda_alto // 2 - texto.get_height() // 2))