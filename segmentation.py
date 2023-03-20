import cv2
import numpy as np

def segmentation_disc(isolated_nerve, img_eq):
    img_eq_int = np.float32(img_eq)
    orig = isolated_nerve.copy()
    orig_2 = img_eq_int.copy()
    
    gray = cv2.cvtColor(img_eq_int, cv2.COLOR_BGR2GRAY)
    _, disc = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    return disc