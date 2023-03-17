import streamlit as st
import cv2
from  PIL import Image
import numpy as np

def isolaNervo(img, rSize):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    altura,largura,cores = img.shape 


    img[100 : 500,  100 : 500]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (15, 15), 0)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

    start_point = (maxLoc[0]-rSize, maxLoc[1]-rSize)
    end_point = (maxLoc[0]+rSize, maxLoc[1]+rSize)

    isolated_nerve = cv2.rectangle(img, start_point, end_point, (0,0,0), 15)

    return gray, minVal, maxVal, minLoc, maxLoc, isolated_nerve

    
'''
    cv2.rectangle(img, start_point, end_point, (0,0,0), 15)
    isolated_nerve = img[maxLoc[1]-rSize : maxLoc[1]+rSize,  maxLoc[0]-rSize : maxLoc[0]+rSize ]
'''
    