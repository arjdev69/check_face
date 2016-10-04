#!/usr/bin/env python
from modules import *


# def takePicture(x, i, top, bottom, left, right, img):
#     imgs = []
#     timestamp = time.strftime("%S", time.localtime())
#     top = 125
#     bottom = 380
#     left = 250
#     right = 450
#     cv2.imshow('aa', img)
#     if x == 1:
#         fn = '%s/%s.jpg' % ('./img', i)
#         crop_img = img[top:bottom, left:right]
#         crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
#         cv2.imshow(fn, crop_img)
#         cv2.imwrite(fn, crop_img)
#         print(fn, 'saved')

args, video_src = getopt.getopt(
    sys.argv[1:], '', ['cascade=', 'nested-cascade='])
args = dict(args)
cascade_fn = args.get(
    '--cascade', "./data/haarcascades/haarcascade_frontalface_alt.xml")
nested_fn = args.get('--nested-cascade',
                     "./data/haarcascades/haarcascade_eye.xml")

cascade = cv2.CascadeClassifier(cascade_fn)
nested = cv2.CascadeClassifier(nested_fn)

cam = cv2.VideoCapture(0)
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    rects = detect(gray, cascade)
    vis = img.copy()
    draw_rects(vis, rects, (0, 1, 0), gray, texto, i)
    keyboard = cv2.waitKey(1)
    for x1, y1, x2, y2 in rects:
        roi = gray[y1:y2, x1:x2]
        vis_roi = vis[y1:y2, x1:x2]
        subrects = detect(roi.copy(), nested)
        if keyboard == ord(' '):
            i = i + 1
            x = 1
            texto = raw_input("Digite:")
            takePicture(x, i, x1, y2, x2, y1, img)
    if keyboard == 27:
        break
    cv2.imshow('facedetect', vis)

cv2.destroyAllWindows()
