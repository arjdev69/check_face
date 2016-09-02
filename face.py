#!/usr/bin/env python
import time
import cv2
import sys, getopt
import numpy as np
#import matplotlib.pyplot as plt

i = tam = 0; texto = ""; crop_img = ""; vis = ""; fn = ""
font = cv2.FONT_HERSHEY_SIMPLEX
template = cv2.imread('recote_padrao.png',0)
w, h = template.shape[::-1]

def detect(img, cascade):
  rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
  if len(rects) == 0:
    return []
  rects[:,2:] += rects[:,:2]
  return rects

def draw_rects(img, rects, color, img_gray, name):
  for x1, y1, x2, y2 in rects:
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    tam = len(loc[1]+loc[0])
    if tam > 0:
      name = "bruno"
      cv2.putText(img,'%s'%name,(x1,y1-20), font, 1,(255,255,255),1,cv2.LINE_AA)
      test = cv2.rectangle(img, (x1, y1), (x2, y2), color,2)
    else:
     cv2.putText(img,'Nao Encontrada',(x1,y1-20), font, 1,(255,255,255),1,cv2.LINE_AA)
     test = cv2.rectangle(img, (x1, y1), (x2, y2), color,2)
def takePicture(x, i, top, bottom, left, right):
  timestamp = time.strftime("%S", time.localtime())
  top = 125; bottom = 380; left = 250; right = 450;
  if x == 1:
    fn = '%s/%s.jpg' % ('./img', i)
    crop_img = img[top:bottom, left:right]
    crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('%s'%timestamp,crop_img)
    cv2.imwrite(fn,crop_img)
    print (fn, 'saved')

args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
args = dict(args)
cascade_fn = args.get('--cascade', "../data/haarcascades/haarcascade_frontalface_alt.xml")
nested_fn  = args.get('--nested-cascade', "../data/haarcascades/haarcascade_eye.xml")

cascade = cv2.CascadeClassifier(cascade_fn)
nested = cv2.CascadeClassifier(nested_fn)

cam  = cv2.VideoCapture(0)

while True:
  ret, img = cam.read()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray = cv2.equalizeHist(gray)
  rects = detect(gray, cascade)
  vis = img.copy()
  draw_rects(vis, rects, (0, 1, 0), gray, texto)
  keyboard = cv2.waitKey(1)
  for x1, y1, x2, y2 in rects:
    roi = gray[y1:y2, x1:x2]
    vis_roi = vis[y1:y2, x1:x2]
    subrects = detect(roi.copy(), nested)
    if keyboard == ord(' '):
      i += 1
      x = 1
      texto = raw_input("Digite:")
      takePicture(x, i, x1, y2, x2, y1)
  if keyboard == 27:
      break
  cv2.imshow('facedetect', vis)
    
cv2.destroyAllWindows()
