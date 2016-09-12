import cv2
import numpy as np
#from matplotlib import pyplot as plt

cam  = cv2.VideoCapture(0)
img = cam.read()

ret, img_rgb  = img
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('1.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
print len(zip(*loc[::-1]))

for pt in zip(*loc[::-1]):
  font = cv2.FONT_HERSHEY_SIMPLEX
  cv2.putText(img_rgb,'Bruno',(10,400), font, 1,(255,255,255),1,cv2.LINE_AA)	
  cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
cv2.imshow('Face',img_rgb)
cv2.imwrite('./img/res.png',img_rgb)























# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('./img/res.png',0)
# img2 = img.copy()
# template = cv2.imread('recote_padrao.png',0)
# w, h = template.shape[::-1]

# # All the 6 methods for comparison in a list
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#             'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# for meth in methods:
#     img = img2.copy()
#     method = eval(meth)

#     # Apply template Matching
#     res = cv2.matchTemplate(img,template,method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

#     # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#     if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#         top_left = min_loc
#     else:
#         top_left = max_loc
#     bottom_right = (top_left[0] + w, top_left[1] + h)

#     cv2.rectangle(img,top_left, bottom_right, 255, 2)

#     plt.subplot(121),plt.imshow(res,cmap = 'gray')
#     plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#     plt.subplot(122),plt.imshow(img,cmap = 'gray')
#     plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#     plt.suptitle(meth)

#     plt.show()

# # 






























#28-08-2016_15-01-35
# import cv2
# img = cv2.imread("./img/res.png")
# crop_img = img[200:400, 100:300] # Crop from x, y, w, h -> 100, 200, 300, 400
# # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
# cv2.imshow("cropped", crop_img)
# cv2.imwrite("recote.png",crop_img)
# cv2.waitKey(0)
# import cv2
# import numpy as np

# # mouse callback function
# def draw_circle(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.rectangle(img, (300, 150), (30, 0), (0,255,0),3)
#         #cv2.circle(img,(x,y),50,(255,0,0),-1)

# # Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_circle)

# while(1):
#     cv2.imshow('image',img)
#     if cv2.waitKey(20) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()
# import cv2
# import numpy as np

# drawing = False # true if mouse is pressed
# mode = True # if True, draw rectangle. Press 'm' to toggle to curve
# ix,iy = -1,-1

# # mouse callback function
# def draw_circle(event,x,y,flags,param):
#     global ix,iy,drawing,mode

#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix,iy = x,y

#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing == True:
#             if mode == True:
#                 cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
#             else:
#                 cv2.circle(img,(x,y),5,(0,0,255),-1)

#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         if mode == True:
#             cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
#         else:
#             cv2.circle(img,(x,y),5,(0,0,255),-1)
# img = np.zeros((512,512,3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_circle)

# while(1):
#     cv2.imshow('image',img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == ord('m'):
#         mode = not mode
#     elif k == 27:
#         break

# cv2.destroyAllWindows()
# import cv2
# import numpy as np
# #from matplotlib import pyplot as plt

# img_rgb = cv2.imread('./img/29-08-2016_09-02-20.jpg')
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# template = cv2.imread('./img/29-08-2016_09-02-18.jpg',0)
# w, h = template.shape[::-1]

# res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# threshold = 0.8
# loc = np.where( res >= threshold)
# print len(loc[0])
# for pt in zip(*loc[::-1]):
#   cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)

# cv2.imwrite('./img/res.png',img_rgb)

# #28-08-2016_15-01-35