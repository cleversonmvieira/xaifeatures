import cv2
import numpy as np
import numpy as ppool
import streamlit as st

def segmentation_disc(isolated_nerve, img_eq):

    img_eq = cv2.convertScaleAbs(img_eq)
    orig = isolated_nerve.copy()
    
    norm = ppool.zeros((15,15))
    final = cv2.normalize(img_eq,  norm, 0, 255, cv2.NORM_MINMAX)
    
    median = cv2.medianBlur(final,21)

    lower_disc = np.array([255,229,0])
    upper_disc = np.array([255,255,36])

    #_, disc = cv2.threshold(median, 33, 255, cv2.THRESH_BINARY)
    disc = cv2.inRange(median, lower_disc, upper_disc)

    # Identificação dos contornos
    contours_disc, _ = cv2.findContours(disc, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Encontrar o contorno com a maior área
    disc_contour = max(contours_disc, key=cv2.contourArea)
    
    # Encontrar as coordenadas do retângulo ao redor do contorno encontrado
    x,y,w,h = cv2.boundingRect(disc_contour)

    Xrec_disc = x+w
    xrec_disc = x
    Yrec_disc = y+h
    yrec_disc = y

    rect_disc = cv2.rectangle(orig,(x,y),(x+w,y+h),(0,0,0),2)  
    
    return rect_disc,Xrec_disc,xrec_disc,Yrec_disc,yrec_disc


def segmentation_cup(isolated_nerve, img_eq):
    img_eq = cv2.convertScaleAbs(img_eq)
    orig = isolated_nerve.copy()
    
    norm = ppool.zeros((15,15))
    final = cv2.normalize(img_eq,  norm, 0, 255, cv2.NORM_MINMAX)
    median = cv2.medianBlur(final,5)

    lower_cup = np.array([255,255,254])
    upper_cup = np.array([255,255,255])

    #_, disc = cv2.threshold(median, 33, 255, cv2.THRESH_BINARY)
    cup = cv2.inRange(median, lower_cup, upper_cup)

    # Identificação dos contornos
    contours_cup, _ = cv2.findContours(cup, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Encontrar o contorno com a maior área
    cup_contour = max(contours_cup, key=cv2.contourArea)
    
    # Encontrar as coordenadas do retângulo ao redor do contorno encontrado
    x,y,w,h = cv2.boundingRect(cup_contour)

    Xrec_cup = x+w
    xrec_cup = x
    Yrec_cup = y+h
    yrec_cup = y

    #result_cup = cv2.drawContours(orig, [cup_contour], -1, (255, 255, 255), 2)

    rect_cup = cv2.rectangle(orig,(x,y),(x+w,y+h),(0,0,0),2)  

    return rect_cup, Xrec_cup,xrec_cup,Yrec_cup,yrec_cup

