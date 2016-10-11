from module_face import *

font = cv2.FONT_HERSHEY_SIMPLEX

def erro_image(img):
  return cv2.putText(img, 'ERRO NAO EXISTE IMAGEM NO BANCO', 
  (20, 50),font, 1, (0, 0, 255), 1, cv2.LINE_AA)
  #test = cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

def comparision_face(img_gray, i, img_video):
  dir = systems.listdir("./img")
  try:  
    photo = '%s/%s.jpg' % ('./img', 1)
    template = cv2.imread(photo, 0)
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    tam = len(loc[0])
    return tam
  except Exception as excecao:
    erro_image(img_video)

def detect(img, cascade):
  rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(
    30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
  if len(rects) == 0:
    return []
  rects[:, 2:] += rects[:, :2]
  return rects

def draw_rects(img, rects, color, img_gray, name, i):
  for x1, y1, x2, y2 in rects:
    tam = comparision_face(img_gray, i, img)
    print tam
    if tam > 0:
      if name == '':
        name = 'Sem Nome'
      cv2.putText(img, '%s' % name, (x1, y1 - 20),
                  font, 1, (0, 255, 0), 1, cv2.LINE_AA)
      test = cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
    else:
      cv2.putText(img, 'FALTA O CADASTRO', (x1 - 50, y1 - 20),
                  font, 1, (255, 255, 255), 1, cv2.LINE_AA)
      test = cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

asyncore.loop()