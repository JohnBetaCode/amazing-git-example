# --------------------------------------------------------------------------
# IMport yur dependencis herer
# import this
# import numpy
import cv2
import os

# --------------------------------------------------------------------------
# Put yur funtions righ here

def main():

    # Some amazing code

    # ----------------------------------------------------------------------
    # 1 - Read lena image
    path = os.path.dirname(os.path.abspath(__file__))
    img = cv2.imread(os.path.join(path, "lena.jpg"))

    # ----------------------------------------------------------------------
    # 2 - Print Lena over the image
    cv2.putText(img=img, text='Lena', org=(50, 50),
    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale= 2.0,
    color=(255, 255, 255), thickness=1, lineType=int(cv2.LINE_AA)) 

    # ----------------------------------------------------------------------
    # 3 - Draw lena's mouth 
    
    # ----------------------------------------------------------------------
    # 4 - Draw lena's eyes
    
    # ----------------------------------------------------------------------
    # 5 - Draw lena's face shape
    cv2.ellipse(img=img, center=(290, 287), axes=(70, 100), 
           angle=10, startAngle=0, endAngle=360, 
           color=(0, 255, 255), thickness=3) 
    # ----------------------------------------------------------------------
    # 6 - Draw lena's eyesbrows
    
    # ----------------------------------------------------------------------
    # 7 -Draw lena's nose
    
    # ----------------------------------------------------------------------
    # 8 - Draw canny lena
    
    # ----------------------------------------------------------------------
    # 9 - Draw gray lena
    
    # ----------------------------------------------------------------------
    # 10 - Draw blurred lena 
    
    # ----------------------------------------------------------------------
    # 11 - Show and display images
    cv2.imshow("img", img)
    cv2.waitKey(0)

# --------------------------------------------------------------------------
# why this? check -> https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------
