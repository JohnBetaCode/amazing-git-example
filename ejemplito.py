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
    cv2.putText(img=img, text='LENA!!$%&/', org=(50, 50),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2.0,
                color=(255, 255, 255), thickness=1, lineType=int(cv2.LINE_AA))

    # ----------------------------------------------------------------------
    # 3 - Draw lena's mouth

    # ----------------------------------------------------------------------
    # 4 - Draw lena's eyes
    cv2.circle(img=img, center=(267, 265), radius=10,
               color=(255, 0, 255), thickness=3)
    cv2.circle(img=img, center=(329, 265),
               radius=10, color=(0, 0, 255), thickness=6)
    # ----------------------------------------------------------------------
    # 5 - Draw lena's face shape
    cv2.ellipse(img=img, center=(290, 287), axes=(70, 100),
                angle=10, startAngle=0, endAngle=360,
                color=(0, 255, 255), thickness=3)
    # ----------------------------------------------------------------------
    # 6 - Draw lena's eyesbrows in two different colors
    cv2.line(img=img, pt1=(293, 262), pt2=(258, 244),
             color=(0, 100, 255), thickness=3)
    cv2.line(img=img, pt1=(320, 259), pt2=(
        353, 246), color=(20, 0, 255), thickness=3)
    # ----------------------------------------------------------------------
    # 7 -Draw lena's nose
    cv2.line(img=img, pt1=(313, 276), pt2=(317, 323), color=(0, 0, 255),
             thickness=3)
    cv2.line(img=img, pt1=(317, 323), pt2=(286, 322), color=(0, 0, 255),
             thickness=3)
    # ----------------------------------------------------------------------
    # 8 - Draw canny lena

    # ----------------------------------------------------------------------
    # 9 - Draw gray lena
<<<<<<< HEAD

=======
    src_gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    img=src_gray
>>>>>>> 0fd069326ab40282d5a373d9bac6526bc414df93
    # ----------------------------------------------------------------------
    # 10 - Draw blurred lena
    img_blur = cv2.blur(src=img, ksize=(3, 3))

    # ----------------------------------------------------------------------
    # 11 - Show and display images
    cv2.imshow("img", img)
    cv2.waitKey(0)


# --------------------------------------------------------------------------
# why this? check -> https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------
