import cv2
import numpy as np

def segmentation_disc(isolated_nerve, img_eq):
    img_eq_float = np.uint8(img_eq)
    orig = isolated_nerve.copy()
    orig_2 = img_eq_float.copy()
    
    gray = cv2.cvtColor(img_eq_float, cv2.COLOR_BGR2GRAY)

    #gray = np.float32(gray)

    equ = cv2.equalizeHist(gray)

    median = cv2.medianBlur(equ,15)

    _, disc = cv2.threshold(gray, 195, 255, cv2.THRESH_BINARY)
    
    return median