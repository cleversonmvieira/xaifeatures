import cv2
import numpy as np

def segmentation_disc(isolated_nerve, img_eq):
    img_eq_int = np.float32(img_eq)
    orig = isolated_nerve.copy()
    orig_2 = img_eq_int.copy()
    
    gray = cv2.cvtColor(img_eq_int, cv2.COLOR_BGR2GRAY)

    equ = cv2.equalizeHist(gray)

    median = cv2.medianBlur(equ,15)

    _, disc = cv2.threshold(gray, 195, 255, cv2.THRESH_BINARY)
    
    return disc