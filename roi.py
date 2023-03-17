import streamlit as st
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
    
    img = img.resize((rW,rH))

    return img
'''
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
    a,l = img.size
    #img = img.crop((h,H,w,W))
    img = img.crop((w,W,h,H))
    st.write(h,H,w,W)
    f = a//2
    a,l = img.size

    img = img.resize((150,150))
    an,ln = img.size
    fnW = l/ln
    fnH = a/an
'''    
    #return int(W*fw),int(w*fw),int(H*fh),int(h*fh),fw,fh,nerve,fnW,fnH,img

    
