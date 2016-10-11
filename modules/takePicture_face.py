from module_face import *

def takePicture(x, i, top, bottom, left, right, img):
  imgs = []
  timestamp = time.strftime("%S", time.localtime())
  top = 125
  bottom = 380
  left = 250
  right = 450
  if x == 1:
    fn = '%s/%s.jpg' % ('./img', i)
    crop_img = img[top:bottom, left:right]
    crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    cv2.imshow(fn, crop_img)
    cv2.imwrite(fn, crop_img)
    print(fn, 'saved')