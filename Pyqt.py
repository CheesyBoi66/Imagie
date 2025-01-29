import cv2
import numpy as np
from keyboard import is_pressed

def init():
    cv2.namedWindow("Goofy moe", cv2.WINDOW_NORMAL)
    winImg = np.ones((1080, 1920, 3), dtype=np.uint8) * 255
    cv2.imshow("Goofy moe", winImg)
    

def main():
    init()
    while True:
        cv2.waitKey(1) & 0xFF  # Process OpenCV events

        if is_pressed('w'):
            print("soos")

        if is_pressed('q'):  # Exit if 'q' is pressed
            break  

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
