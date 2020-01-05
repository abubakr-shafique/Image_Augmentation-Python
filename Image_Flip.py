## This Program is Written by Abubakr Shafique (abubakr.shafique@gmail.com)

import numpy as np
import cv2 as cv

def main():
    Input_Image = cv.imread('Test_Image.png')
    
    Flip_Vertical = cv.flip(Input_Image, 0) #0 means Vertical Flip
    cv.imwrite('Flip_Vertical.png', Flip_Vertical)
    
    Flip_Horizontal = cv.flip(Input_Image, 1) #1 means Horizontal Flip
    cv.imwrite('Flip_Horizontal.png', Flip_Horizontal)
    
    Flip_Vertical_Horizontal = cv.flip(Input_Image, -1) #-1 means Flip both Vertical and Horizontal
    cv.imwrite('Flip_Vertical_Horizontal.png', Flip_Vertical_Horizontal)
    
    input('Press Enter to Continue...')

if __name__ == '__main__':
    main()