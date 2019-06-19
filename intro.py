import numpy as np
import cv2

L1 = 480
B1 = 640
def introScreen():
    #screen = np.ones((L2, B2), np.uint8) * 255
    screen=np.ones((L1,B1),dtype="uint8") * 255
    while 1:
        #cv2.putText(screen, "Project 'Ink'y Fingers", (350, 50), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
        cv2.putText(screen,"Inky Fingers",(100,100),cv2.FONT_HERSHEY_COMPLEX,5,0,0)
        cv2.imshow("ABC",screen)
        k = cv2.waitKey(5)


introScreen()

