import time, math, time, os, cv2 as w
import Pyqt as py
import numpy as np

fps = 60


def winInit():
    global fRate
    fRate = (1000//fps)
    w.namedWindow("Bongo",w.WINDOW_NORMAL)
    bak = np.ones((400,400,3), dtype=np.uint8) * 255
    w.imshow("Bongo", bak)
    
def main():
    
    loop = True
    winInit()

    while(loop==True):
        w.waitKey(fRate)

main()