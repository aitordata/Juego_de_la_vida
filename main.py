import numpy as np
import time 
import os

def limpiar_consola(): #Limpia la consola
    os.system('clear')
my_array=np.full((50,50),1)


contador=0
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
import pygame

# Configuración inicial de Pygame
pygame.init()

# Dimensiones de la ventana
ventana_ancho = 800
ventana_alto = 800

# Crear la ventana
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Juego de vida")

# Color de fondo
fondo_color = (255, 255, 255)
filas = len(my_array)
columnas = len(my_array)

# Tamaño de celda
celda_ancho = ventana_ancho // columnas
celda_alto = ventana_alto // filas
ejecutando = True
def renderizar_matriz(my_array):
    for fila in range(filas):
        for columna in range(columnas):
            valor = my_array[fila][columna]
            pygame.draw.rect(ventana, (0, 0, 0), (columna * celda_ancho, fila * celda_alto, celda_ancho, celda_alto))
            texto = pygame.font.Font(None, 36).render(str(valor), True, (255, 255, 255))
            ventana.blit(texto, (columna * celda_ancho + celda_ancho // 2 - texto.get_width() // 2,
                                 fila * celda_alto + celda_alto // 2 - texto.get_height() // 2))

while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    # Borrar la pantalla
    ventana.fill(fondo_color)

    # Dibujar la matriz en la ventana
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
    time.sleep(2)
    print(my_array)
    pygame.display.flip()
                    
