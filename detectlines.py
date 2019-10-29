
import cv2
import numpy as np
import random 

cap = cv2.VideoCapture(0)
lsd = cv2.createLineSegmentDetector(0)

img = cap.read()[1]
hist = []
while True:
	_,img = cap.read()
	black = np.zeros_like(img)
	black2 = np.invert(black)
	img2 = img.copy()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	lines = lsd.detect(gray)[0]
	c1,c2,c3 = random.randint(0,255),random.randint(0,255),random.randint(0,255)
	for dline in lines:
		x0, y0, x1, y1 = dline.flatten()
		hist.append([x0,y0,x1,y1])
		cv2.line(black2, (x0, y0), (x1,y1), (0,0,0), 1, cv2.LINE_AA)
		#cv2.line(img, (x0, y0), (x1,y1), (c1,c2,c3), 1, cv2.LINE_AA)
	if len(hist)>0:
		for item in hist:
			cv2.line(img2, (item[0], item[1]), (item[2],item[3]), (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 1, cv2.LINE_AA)
			cv2.line(black, (item[0], item[1]), (item[2],item[3]), (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 1, cv2.LINE_AA)
	hist = hist[-600:]
	final1 = cv2.hconcat([img,black2])
	final2 = cv2.hconcat([black,img2])
	final = cv2.vconcat([final1,final2])
	cv2.imshow("Camera",final)
	k = cv2.waitKey(1)
	if k == ord('q') or k == 27:
		exit()
