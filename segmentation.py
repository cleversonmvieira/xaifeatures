import cv2
import numpy as np
from skimage import color, util

def segmentation_disc(isolated_nerve, img_eq):
    img_eq = np.float64(img_eq)
    gray = color.rgb2gray(img_eq)
    #gray = util.img_as_uint(gray)
    
    #gray = cv2.cvtColor(img_eq, cv2.COLOR_RGB2GRAY)

    #gray = np.float32(gray)

    #equ = cv2.equalizeHist(gray)

    #median = cv2.medianBlur(gray,15)

    #_, disc = cv2.threshold(gray, 33, 255, cv2.THRESH_BINARY)
    
    return gray