from module_face import *

font = cv2.FONT_HERSHEY_SIMPLEX


def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(
        30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
      return []
    rects[:, 2:] += rects[:, :2]
    return rects


def draw_rects(img, rects, color, img_gray, name, i):
  for x1, y1, x2, y2 in rects:
    fotos = '%s/%s.jpg' % ('./img', 1)
    template = cv2.imread(fotos, 0)
    template = template[125:380, 250:450]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    tam = len(loc[0])
    if tam > 0:
      cv2.putText(img, '%s' % name, (x1, y1 - 20),
                  font, 1, (0, 255, 0), 1, cv2.LINE_AA)
      test = cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
    else:
      cv2.putText(img, 'Nao Encontrada', (x1, y1 - 20),
                  font, 1, (255, 255, 255), 1, cv2.LINE_AA)
      test = cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
