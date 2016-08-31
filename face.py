#!/usr/bin/env python
import time
import cv2
import sys, getopt
import numpy as np
#import matplotlib.pyplot as plt

crop_img = ""
face = vis = edge = ""
fn = ""
font = cv2.FONT_HERSHEY_SIMPLEX
template = cv2.imread('recote_padrao.png',0)
w, h = template.shape[::-1]
def detect(img, cascade):
  rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
  if len(rects) == 0:
    return []
  rects[:,2:] += rects[:,:2]
  return rects

def draw_rects(img, rects, color, img_gray):
  for x1, y1, x2, y2 in rects:
    it = x1, y1, x2, y2
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    tam = len(loc[0]+loc[1])
    if tam > 0:
      cv2.putText(img,'Face Found',(x1,y1-20), font, 1,(255,255,255),1,cv2.LINE_AA)
      test = cv2.rectangle(img, (x1, y1), (x2, y2), color,2)
      a = y1 + x2
      b = y2 + x1
      edge = cv2.Canny(img, b, a)
      vis[edge != 0] = (255,245,240)

def takePicture():
  timestamp = time.strftime("%d-%m-%Y_%H-%M-%S", time.localtime())
  fn = '%s/%s.jpg' % ('./img', timestamp)
  top = 100 
  bottom = 350
  left = 250
  right = 450
  crop_img = img[top:bottom, left:right]
  cv2.imshow('Recote',crop_img)
  cv2.imwrite('recote_padrao.png',crop_img)
  cv2.imwrite(fn, img)
  img_rgb = cv2.imread(fn)

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
  draw_rects(vis, rects, (0, 1, 0), rects)
  for x1, y1, x2, y2 in rects:
    roi = gray[y1:y2, x1:x2]
    vis_roi = vis[y1:y2, x1:x2]
    subrects = detect(roi.copy(), nested)
    #draw_rects(vis_roi, subrects,(50,119,247))
  cv2.imshow('facedetect', vis)
  keyboard = cv2.waitKey(1)
  if keyboard == 27:
    break
  if keyboard == ord(' '):
    takePicture()
    
cv2.destroyAllWindows()
