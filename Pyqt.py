import cv2
import numpy as np
from keyboard import is_pressed

x,y = 0,0
w,h = 1920,200
global winImg
def init():
    global winImg
    winImg = np.ones((1080, 1920, 3), dtype=np.uint8) * 255
    cv2.imshow("Goofy moe", winImg)
    

def draw_thingies():
    global winImg, x, y, w, h
    cv2.rectangle(winImg,(x,y),(x+w,y+h),(0,100,255), -1)


def main():  
    global x,y
    
    cv2.namedWindow("Goofy moe", cv2.WINDOW_NORMAL)
    

    init()
    
    while True:
        init()
        key = cv2.waitKey(1) & 0xFF  # Process OpenCV events

        if is_pressed('w'):
            y -= 2
            draw_thingies()

            print("w")    


        if is_pressed('s'):
            y += 2
            draw_thingies()
            print("s")

        if is_pressed('q'):  # Exit if 'q' is pressed
            break  

    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()
