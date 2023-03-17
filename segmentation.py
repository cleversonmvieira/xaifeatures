import cv2
import numpy as np

def segmentation_disc(isolated_nerve, img_eq):
    iq = np.float32(img_eq)
    
    orig = isolated_nerve.copy()
    orig_2 = img_eq.copy()
    
    gray = cv2.cvtColor(img_eq, cv2.COLOR_RGB2GRAY)

    equ = cv2.equalizeHist(gray)

    median = cv2.medianBlur(equ,15)
    
    _, disc = cv2.threshold(median, 195, 255, cv2.THRESH_BINARY)
    
    # Identificação dos contornos
    contours_disc, _ = cv2.findContours(disc, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Encontrar o contorno com a maior área
    disc_contour = max(contours_disc, key=cv2.contourArea)
    
    # Encontrar as coordenadas do retângulo ao redor do contorno encontrado
    x,y,w,h = cv2.boundingRect(disc_contour)

    # Desenhar o contorno na imagem original
    #result_disc = cv2.drawContours(orig2, [disc_contour], -1, (255, 255, 255), 2)
    #utils_mod.salvarImagem(path,result_disc,imgName+'_disc_draw',ext,'rectangles')
    #plt.imshow(result_disc)
    #plt.show()
    #result1 = result_disc.copy()
    
    rect_disc = cv2.rectangle(orig_2,(x,y),(x+w,y+h),(0,255,0),2)    
    #print(x,y,w,h)
    
    Xrec = x+w
    xrec = x
    Yrec = y+h
    yrec = y
    #print(Xrec,xrec,Yrec,yrec)

    #plt.imshow(rect_disc)
    #plt.show()

    #utils_mod.salvarImagem(path,rect_disc,imgName+'_disc',ext,'rectangles')

    #return Xrec,xrec,Yrec,yrec 
    return disc, rect_disc