
import cv2
import numpy as np
import random 

cap = cv2.VideoCapture(0)
lsd = cv2.createLineSegmentDetector(0)

img = cap.read()[1]
hist = []
while True:
	_,img = cap.read() # captura frame da camera
	black = np.zeros_like(img) # cria uma cópia com a mesma dimensão do frame, porém, toda preta.
	black2 = np.invert(black) # Cria uma cópia de Black, invertendo as cores, onde estava preto ficará branco.
	img2 = img.copy() # cria uma cópia do frame, sem alterações.
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # cria imagem a partir do frame, em tons de cinza.

	lines = lsd.detect(gray)[0] # A detecção de linhas deve ser feita em imagem em tons de cinza.
	c1,c2,c3 = random.randint(70,255),random.randint(70,255),random.randint(70,255) # criamos cores aleatórias
	for dline in lines:
		x0, y0, x1, y1 = dline.flatten() # Coordenadas das linhas detectadas
		hist.append([x0,y0,x1,y1]) # cria histórico com linhas detectadas
		cv2.line(black2, (x0, y0), (x1,y1), (0,0,0), 1, cv2.LINE_AA) # plota linhas detectadas na imagem
	if len(hist)>0: # Verifica se o histórico não está vazio
		for item in hist: # Plota todas as linhas do histórico
			cv2.line(img2, (item[0], item[1]), (item[2],item[3]), (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 1, cv2.LINE_AA)
			cv2.line(black, (item[0], item[1]), (item[2],item[3]), (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 1, cv2.LINE_AA)
	hist = hist[-600:] # limita o histórico a 600 linhas, para dar efeito de atraso nas linhas
	final1 = cv2.hconcat([img,black2]) # concatena as imagens
	final2 = cv2.hconcat([black,img2])
	final = cv2.vconcat([final1,final2])
	cv2.imshow("Camera",final) # Exibe a imagem
	k = cv2.waitKey(1) # aguarda tecla ser pressionada
	if k == ord('q') or k == 27:
		exit()
