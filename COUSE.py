import cv2
import numpy as np
import copy
import pyautogui as pyauto


#L = 1080
#B = 1920

L1 = 480
B1 = 640

L2 = 2000
B2 = 3000


cap = cv2.VideoCapture(0)
cap.set(1,B1)
cap.set(1,L1)

white = (np.array([250, 250, 250]), np.array([255, 255, 255]))
black = (np.array([0, 0, 0]), np.array([10, 10, 10]))

yellow = ([0,189,150], [77,255,230])
orange = ([0,29,198],[93,117,253])
orange_new = ([0,0,198],[93,70,253])
pink = ([100,7,193],[255,68,254])

# screen = np.ones((480, 640, 3), dtype="uint8") * 255


'''prev_x = 0
prev_y = 0
prev_color = list(np.ones((10, 10, 3), dtype="uint8") * 255)
#print(np.array(prev_color).shape)
'''


def scale(x, y):
    x1 = int((x / L1) * L2)
    y1 = int((y / B1) * B2)
    return x1, y1


def analyze(img):
    if filter(img, orange) and filter(img, pink):
        x, y = filter(img, orange)
        return x,y,1
    elif filter(img, orange):
        x, y = filter(img,orange)
        return x,y,0
    elif filter(img, orange) and filter(img, yellow):
        x, y = filter(img, orange)
        return x, y, 2
    return 0, 0, -1


def filter(img, C):
    lower = np.array(C[0])
    upper = np.array(C[1])
    frame = cv2.inRange(img, lower, upper)

    kernel = np.ones((3, 3), np.uint8)
    frame = cv2.erode(frame, kernel, iterations=1)
    #cv2.imshow("mid", frame)
    M = cv2.moments(frame)
    if M["m00"]:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        return cX, cY
    return None


print("start!")
while 1:
    ret, frame = cap.read()
    # #print(frame.shape)
    frame = frame[:, ::-1]
    frame = frame[100:400]
    #cv2.imshow("orig", frame)
    #x, y, code = analyze(frame)
    x, y , code = analyze(frame)
    #print(x, y)
    x, y = scale(x, y)
    #print("\t\t\t", x, y)
    #print(x, y)

    '''if x >= L2:
        x = L2-1
    if y >= B2:
        y = B2-1'''
    if code == 0:
        pyauto.moveTo(x, y)
    if code == 1:
        pyauto.doubleClick(x, y)
    '''if code == 2:
        pyauto.doubleClick(x, y)'''

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()