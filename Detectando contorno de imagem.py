import cv2
import numpy as np

#Carregando imagem
image = cv2.imread('homer.png')
cv2.imshow('0 - Original Image', image)
cv2.waitKey(0)

#Criando uma imagem preta com as mesmas dimensões da nossa imagem carregada
blank_image = np.zeros((image.shape[0], image.shape[1], 3))

#Criando uma copia da imagem original
orginal_image = image

#Imagem em escala de cinza
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Encontrando os contornos
edged = cv2.Canny(gray, 50, 200)
cv2.imshow('1 - Canny Edges', edged)
cv2.waitKey(0)

#Encontre contornos e imprima quantos foram encontrados
contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print ("Number of contours found = ", len(contours))

#Desenhe todos os contornos
cv2.drawContours(blank_image, contours, -1, (0,255,0), 3)
cv2.imshow('2 - All Contours over blank image', blank_image)
cv2.waitKey(0)

#Desenhe todos os contornos sobre a imagem original
cv2.drawContours(image, contours, -1, (0,255,0), 3)
cv2.imshow('3 - All Contours', image)
cv2.waitKey(0)

cv2.destroyAllWindows()