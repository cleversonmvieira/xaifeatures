import streamlit as st
import cv2
import utils_mod
import retinex_mod
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
    img = cv2.resize(img,(rW,rH),interpolation=cv2.INTER_CUBIC)           
    
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
    f = a//2
    a,l,c = img.shape

    img = cv2.resize(img,(150,150),interpolation=cv2.INTER_CUBIC)
    an,ln,cn = img.shape
    fnW = l/ln
    fnH = a/an
    
    return int(W*fw),int(w*fw),int(H*fh),int(h*fh),fw,fh,nerve,fnW,fnH,img
