import cv2
import numpy as np
import numpy as ppool
import streamlit as st

def segmentation_disc(isolated_nerve, img_eq):

    img_eq = cv2.convertScaleAbs(img_eq)
    orig = isolated_nerve.copy()
    
    norm = ppool.zeros((15,15))
    final = cv2.normalize(img_eq,  norm, 0, 255, cv2.NORM_MINMAX)
    
    median = cv2.medianBlur(final,9)

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

    rect_disc = cv2.rectangle(orig,(x,y),(x+w,y+h),(255,255,255),2)  
    
    return rect_disc


def segmentation_cup(isolated_nerve, img_eq):
    img_eq = cv2.convertScaleAbs(img_eq)
    orig = isolated_nerve.copy()
    
    norm = ppool.zeros((15,15))
    final = cv2.normalize(img_eq,  norm, 0, 255, cv2.NORM_MINMAX)
    median = cv2.medianBlur(final,9)

    lower_cup = np.array([254,254,254])
    upper_cup = np.array([255,255,255])

    #_, disc = cv2.threshold(median, 33, 255, cv2.THRESH_BINARY)
    cup = cv2.inRange(median, lower_cup, upper_cup)

    # Identificação dos contornos
    contours_cup, _ = cv2.findContours(cup, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Encontrar o contorno com a maior área
    cup_contour = max(contours_cup, key=cv2.contourArea)
    
    # Encontrar as coordenadas do retângulo ao redor do contorno encontrado
    x,y,w,h = cv2.boundingRect(cup_contour)

    result_disc = cv2.drawContours(orig, [cup_contour], -1, (255, 255, 255), 2)

    rect_cup = cv2.rectangle(orig,(x,y),(x+w,y+h),(255,255,255),2)  
    
    st.write(len(cup_contour))

    return rect_cup

