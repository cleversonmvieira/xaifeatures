from skimage import exposure
import numpy as np

def equalization(img):
    img_eq = exposure.equalize_adapthist(img, clip_limit=0.05)
    img_eq = np.array(img_eq)
    return img_eq