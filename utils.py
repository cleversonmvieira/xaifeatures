import cv2

def medianBlurCustom(img,x,r):
    for i in range(0,r):
        img = cv2.medianBlur(img,x)
    return img


def histogram_equalization(img):
    
    rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #rgb_img = cv2.imread(image_path)

    # convert from RGB color-space to YCrCb
    ycrcb_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2YCrCb)

    # equalize the histogram of the Y channel
    ycrcb_img[:, :, 0] = cv2.equalizeHist(ycrcb_img[:, :, 0])

    # convert back to RGB color-space from YCrCb
    equalized_img = cv2.cvtColor(ycrcb_img, cv2.COLOR_YCrCb2BGR)

    #cv2.imshow('equalized_img', equalized_img)
    return equalized_img