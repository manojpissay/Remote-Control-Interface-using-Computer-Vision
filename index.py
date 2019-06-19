import cv2
import numpy as np
cap = cv2.VideoCapture(0)

C1 = ([115, 95, 95], [120, 100, 100])
black = ([0, 0, 0], [0, 0, 0])
# green = ([67, 136, 0],[72, 138, 2])
# red = ([0, 0, 240], [100, 100, 255])
red = ([0, 0, 200], [5, 5, 255])
#green = ([0, 150, 0], [110, 255, 90])
#pink = ([90, 50, 240], [120, 75, 255])

green = ([0,189,150], [77,255,230])
orange = ([0,0,198],[93,70,253])
orange_old = ([0,29,198],[93,117,253])
pink = ([100,7,193],[255,68,254])
#yellow = ([150, 150, 0], [255, 255, 200])

L1 = 480
B1 = 640

L2 = 1080
B2 = 1980



def scale(x, y, L1, B1, L2, B2):
    x1 = int((x / L1) * L2)
    y1 = int((y / B1) * B2)
    return x1, y1

def filter(img, C):
    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array(C[0])
    upper = np.array(C[1])
    mask = cv2.inRange(img, lower, upper)
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=0)
    # res = cv2.bitwise_and(img, img, mask=mask)
    # return res
    return mask


cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1980)
while 1:
    my = np.zeros((L2, B2, 3), dtype="uint8")
    #print(my)
    #cap.set(cv2)
    ret, frame = cap.read()
    #print(frame)
    frame = frame[:, ::-1]
    cv2.imshow("orig", frame)
    frame = filter(frame, green)#####################################
    #print(my.shape)
    M = cv2.moments(frame)
    if M["m00"]:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        #my = np.array(my)
        cX, cY = scale(cX, cY, L1, B1, L2, B2)
        cv2.circle(my, (cX, cY), 5, (255, 255, 255), -1)
    cv2.imshow("center", my)
    # print(frame[0, 0])
    cv2.imshow("test", frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break



cv2.destroyAllWindows()
cap.release()