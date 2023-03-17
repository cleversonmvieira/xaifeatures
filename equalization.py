import numpy as np
import cv2
import utils_mod
from skimage import io, exposure
import os
from matplotlib import pyplot as plt

def equalization(img):
    img_eq = exposure.equalize_adapthist(img, clip_limit=0.05)

    return img_eq