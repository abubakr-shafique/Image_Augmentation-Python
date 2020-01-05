## This Program is Written by Abubakr Shafique (abubakr.shafique@gmail.com)

from PIL import Image 

def Rotate_Clockwise(Input_Image):

    New_Image = Input_Image.transpose(Image.ROTATE_270)
    
    return New_Image

def Rotate_Counter_Clockwise(Input_Image):

    New_Image = Input_Image.transpose(Image.ROTATE_90)
    
    return New_Image

def Rotate_Upside_Down(Input_Image):

    New_Image = Input_Image.transpose(Image.ROTATE_180)
    
    return New_Image

def main():
    Input_Image = Image.open('Test_Image3.png')

    CW_Rotated_Image = Rotate_Clockwise(Input_Image) 
    CW_Rotated_Image.save('CW_Rotated_Image.png')

    CCW_Rotated_Image = Rotate_Counter_Clockwise(Input_Image) 
    CCW_Rotated_Image.save('CCW_Rotated_Image.png')
    
    UD_Rotated_Image = Rotate_Upside_Down(Input_Image) 
    UD_Rotated_Image.save('UD_Rotated_Image.png')
    
    input('Please Enter to Continue...')


if __name__ == '__main__':
    main()