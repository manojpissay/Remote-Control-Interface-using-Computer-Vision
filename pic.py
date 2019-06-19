import cv2
import numpy as np
cap = cv2.VideoCapture(0)

C1 = ([115, 95, 95], [120, 100, 100])
black = ([0, 0, 0], [0, 0, 0])
red = ([0, 0, 240], [100, 100, 255])
# red_hsv = ([4, 0, 0], [4, 185, 249])
green = ([0, 150, 0], [110, 255, 90])

def filter(img, C):
    #hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array(C[0])
    upper = np.array(C[1])
    mask = cv2.inRange(img, lower, upper)
    #res = cv2.bitwise_and(img, img, mask=mask)
    return mask

ret, frame = cap.read()
#frame = frame[100:400, ::-1]
cv2.imwrite("pic.jpeg", frame)
# print(frame)
# frame = filter(frame, black)
# print(frame[0, 0])
#frame = cv2.imread("pic.jpeg")
#frame1 = filter(frame, green)
#area = cv2.findContours()
#cv2.imshow("test", frame1)
#print("\n\n", frame1[0, 0])
print("next", frame.shape)
#print(str(frame) == str(np.zeros((480, 640, 3))))
print("\n\n", frame[0, 0])


cv2.waitKey(0)
cv2.destroyAllWindows()
#cap.release()