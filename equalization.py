from skimage import exposure
import cv2

def equalization(img):
    img_eq = exposure.equalize_adapthist(img, clip_limit=0.05)
    img_eq= cv2.imdecode(img_eq, 1)
    return img_eq