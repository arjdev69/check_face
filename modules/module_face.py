import time
import cv2
import sys
import getopt
import numpy as np
from detect_face import *
from takePicture_face import *

i = tam = 0
texto = ""
crop_img = ""
vis = ""
fn = ""
font = cv2.FONT_HERSHEY_SIMPLEX
