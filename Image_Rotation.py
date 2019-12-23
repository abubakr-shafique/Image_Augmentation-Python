## This Program is Written by Abubakr Shafique (abubakr.shafique@gmail.com)

import numpy as np
import cv2 as cv 


def Rotate_Clockwise(Image):
    Height, Width, Channels = Image.shape
    
    New_Image = np.zeros(Image.shape, dtype=np.uint8)
    
    for i in range(Height):
        for j in range(Width):
            New_Image[i, j] = Image[Height-j-1, Width-i-1]
            New_Image = New_Image[0:Height, 0:Width]
    return New_Image

def Rotate_Counter_Clockwise(Image):
    Height, Width, Channels = Image.shape
    
    New_Image = np.zeros(Image.shape, dtype=np.uint8)
    
    for i in range(Height):
        for j in range(Width):
            New_Image[i, j] = Image[j-1, i-1]
            New_Image = New_Image[0:Height, 0:Width]
    return New_Image

def Rotate_Upside_Down(Image):
    Height, Width, Channels = Image.shape
    
    New_Image = np.zeros(Image.shape, dtype=np.uint8)
    
    for i in range(Height):
        for j in range(Width):
            New_Image[i, j] = Image[Height-i-1, Width-j-1]
            New_Image = New_Image[0:Height, 0:Width]
    return New_Image

def main():
    Input_Image = cv.imread('Test_Image.png')
    
    Image_CW = Rotate_Clockwise(Input_Image)
    cv.imwrite('Image_CW.png', Image_CW)
    
    Image_CCW = Rotate_Counter_Clockwise(Input_Image)
    cv.imwrite('Image_CCW.png', Image_CCW)
    
    Image_UD = Rotate_Upside_Down(Input_Image)
    cv.imwrite('Image_Upside_Down.png', Image_UD)
    
    input('Please Enter to Continue...')


if __name__ == '__main__':
    main()