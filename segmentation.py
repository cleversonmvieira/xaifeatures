import cv2
import numpy as np
import numpy as ppool
from skimage import color, util

def segmentation_disc(isolated_nerve, img_eq):
    img_eq = cv2.convertScaleAbs(img_eq)
    #gray = color.rgb2gray(img_eq)
    #gray = util.img_as_uint(gray)
    
    norm = ppool.zeros((15,15))
    final = cv2.normalize(img_eq,  norm, 0, 255, cv2.NORM_MINMAX)
    
    gray = cv2.cvtColor(img_eq, cv2.COLOR_RGB2GRAY)

    #gray = np.float64(gray)

    equ = gray

    #equ = cv2.equalizeHist(gray)

    median = cv2.medianBlur(final,15)


    lower_disc = np.array([255,229,0])
    upper_disc = np.array([255,255,36])

    lower_cup = np.array([255,255,255])
    upper_cup = np.array([255,255,255])

    #_, disc = cv2.threshold(median, 33, 255, cv2.THRESH_BINARY)

    disc = cv2.inRange(median, lower_disc, upper_disc)

    cup = cv2.inRange(median, lower_cup, upper_cup)
    
    return median, disc, cup