import cv2
import numpy as np
from keyboard import is_pressed

x,y = 0,0
w,h = 1920,200

def init():
    winImg = np.ones((1080, 1920, 3), dtype=np.uint8) * 255
    cv2.rectangle(winImg,(x,y),(x+w,y+h),(0,100,255), -1)
    cv2.imshow("Goofy moe", winImg)
    



def main():  
    global x,y
    
    cv2.namedWindow("Goofy moe", cv2.WINDOW_NORMAL)
    

    init()
    
    while True:
        key = cv2.waitKey(1) & 0xFF  # Process OpenCV events

        if is_pressed('w'):
            y -= 2
            init()
            print("w")    


        if is_pressed('s'):
            y += 2
            init()
            print("s")

        if is_pressed('q'):  # Exit if 'q' is pressed
            break  

    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()
