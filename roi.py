import streamlit as st
import cv2
from  PIL import Image
import numpy as np

def isolaNervo(img, rSize):
    
    altura,largura,cores = img.shape 
    
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
    
    img = cv2.resize(img,(rW,rH))
    W,w,H,h,nerve = OpticalLocationCenter2Outside(img,rW,rH)
    W = largura
    w = 0
    H = altura
    h = 0
    nerve = int(altura / 5.4)

    if (w > rW or h > rH):
        w = int(rW//2 - rSize//4)
        W = int(rW//2 + rSize//4)
        h = int(rH//2 - rSize//4)
        H = int(rH//2 + rSize//4)
    a,l,c = img.shape
    img = img[h:H,w:W]
    #st.write(h,H,w,W)
    f = a//2
    a,l,c = img.shape

    img = cv2.resize(img,(150,150))
    an,ln,cn = img.shape
    fnW = l/ln
    fnH = a/an

    return int(W*fw),int(w*fw),int(H*fh),int(h*fh),fw,fh,nerve,fnW,fnH,img
    
def OpticalLocationCenter2Outside(img,rW,rH):
    imgR = img.copy()
    imgblk = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    altura,largura,cores = img.shape
    alturaR,larguraR,coresR = imgR.shape
    md,ml,ld,ll = cv2.minMaxLoc(imgblk)  
    xc = int(largura//2)
    yc = int(altura//2)
    busca = 1
    nbusca = 12
    nerve = int(altura / 5.4)
    fa = altura//nbusca
    fl = largura//nbusca
    x,y,X,Y = (1,1,1,1)

    
    while busca <= nbusca and x>0 and y>0 and X<largura and Y < altura:
        fbuscaA = int(fa*busca)
        fbuscaL = int(fl*busca)
        x = xc - fbuscaL
        X = xc + fbuscaL
        y = yc - fbuscaA
        Y = yc + fbuscaA
        
        imgBusca = img[y:Y,x:X]
        #imgBusca = retinex_mod.exRetinexDirecaoTone(imgBusca)
        imgBusca = utils.histogram_equalization(imgBusca)
        import utils
        imgBusca = utils.medianBlurCustom(imgBusca,9,9)
        imgAux = cv2.cvtColor(imgBusca,cv2.COLOR_BGR2GRAY)
        md,ml,ld,ll = cv2.minMaxLoc(imgAux)
        px = ll[0]
        py = ll[1]
        
        if (np.sum(imgBusca[py][px]) > 700 and np.sum(img[y:Y,x:X][py][px])>300) :
            xf = x + px - nerve
            Xf = x + px + nerve
            yf = y + py - nerve
            Yf = y + py + nerve
            if xf < 0: xf = 0
            if Xf > largura: Xf = largura
            if yf < 0: yf = 0
            if Yf > altura: Yf = altura
            imgBusca = imgR[yf:Yf,xf:Xf]           
            imgAux = imgblk[yf:Yf,xf:Xf]
            md,ml,ld,ll = cv2.minMaxLoc(imgAux)
            px = ll[0]
            py = ll[1]
     
            
            auxX = xf
            auxY = yf
            xf = xf + px - nerve
            yf = yf + py - nerve
            Xf = auxX + px + nerve            
            Yf = auxY + py + nerve            
            if xf < 0: xf = 0
            if Xf > larguraR: Xf = larguraR
            if yf < 0: yf = 0
            if Yf > alturaR: Yf = alturaR            
            return Xf,xf,Yf,yf,nerve
        busca += 1

    return largura,0,altura,0,nerve