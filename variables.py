import numpy as np
import pygame
my_array=np.full((51,51),1)
negro = (255, 255, 255)
filas = len(my_array)
columnas = len(my_array)
celda_ancho = 800 // columnas
celda_alto = 800// filas
ventana = pygame.display.set_mode((800, 800))
