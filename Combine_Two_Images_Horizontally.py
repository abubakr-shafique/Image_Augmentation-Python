## This Program is Written by Abubakr Shafique (abubakr.shafique@gmail.com)

import numpy as np
import cv2 as cv 

def Combine_Images_Horizontally(Image1, Image2):
    Height1 = Image1.shape[0]
    Width1 = Image1.shape[1]
    Channels1 = Image1.shape[2]
    
    Height2 = Image2.shape[0]
    Width2 = Image2.shape[1]
    Channels2 = Image2.shape[2]
    
    N = 10 #Spacing Between two combined Image
    
    New_Width = Width1 + Width2 + N
    
    if(Height1 > Height2):
        New_Height = Height1
    else:
        New_Height = Height2
    
    New_Image = np.zeros((New_Height, New_Width, Channels1), np.uint8)
    
    for x in range(0, Height1):
        for y in range(0, Width1):
            for c in range(Channels1):
                New_Image[x, y, c] = Image1[x, y, c]
    
    for x in range(0, Height2):
        for y in range(0, Width2):
            for c in range(Channels2):
                New_Image[x, (y + Width1 + N), c] = Image2[x, y, c]
    
    return New_Image        

def main():
    Image1 = cv.imread("Test_Image1.png")
    Image2 = cv.imread("Test_Image3.png")
    
    New_Combined_Image = Combine_Images_Horizontally(Image1, Image2)
    
    cv.imwrite("Horizontally_Combined_Image.png", New_Combined_Image)
    input("Please Enter to Continue...")


if __name__ == '__main__':
    main()