from skimage import exposure

def equalization(img):
    img_eq = exposure.equalize_adapthist(img, clip_limit=0.05)

    return img_eq