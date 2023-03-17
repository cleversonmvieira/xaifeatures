import cv2
from  PIL import Image

def isolaNervo(img, rSize):
    
    altura,largura = img.size 
    
    if altura < largura :        
        rH = rSize
        rW = int(rSize*largura/altura)
        fw = largura/rW
        fh = altura/rH
    else:        
        rW = rSize
        rH = int(rSize*altura/largura)
        fw = largura/rW
        fh = altura/rH
    
    img = cv2.resize(img,(rW,rH),interpolation=cv2.INTER_CUBIC)
    return img
