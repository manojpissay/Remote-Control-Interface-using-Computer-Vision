import cv2
import numpy as np
import copy
import pyautogui as pyauto
import time


#L = 1080
#B = 1920

L1 = 720
B1 = 1280

L2 = 2000
B2 = 2000


cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)

white = (np.array([250, 250, 250]), np.array([255, 255, 255]))
black = (np.array([0, 0, 0]), np.array([10, 10, 10]))

green = ([0,189,150], [77,255,230])
orange = ([0,29,198],[93,117,253])
pink = ([100,7,193],[255,68,254])
# screen = np.ones((480, 640, 3), dtype="uint8") * 255


prev_x = 0
prev_y = 0
prev_color = list(np.ones((10, 10, 3), dtype="uint8") * 255)
# print(np.array(prev_color).shape)



def scale(x, y, L1, B1, L2, B2):
    x1 = int((x / L1) * L2)
    y1 = int((y / B1) * B2)
    return x1, y1



def default_screen():
    screen = np.ones((L2, B2), np.uint8) * 255
    cv2.putText(screen, "'Ink'y Fingers", (700, 60), cv2.FONT_HERSHEY_COMPLEX, 2, 0, 3)
    cv2.line(screen, (0, 100), (2000, 100), (0, 0, 0), 5)   #horizontal
    #cv2.line(screen, (1100, 0), (1100, 1000), (0, 0, 0), 5)    #vertical
    return screen


def point(screen,x,y):
    #print(x, y)
    global prev_x
    global prev_y
    global prev_color
    cv2.circle(screen, (prev_x, prev_y), 3, (255, 255, 255), 5)
    cv2.circle(screen, (x, y), 5, 0, -1)
    prev_x = x
    prev_y = y
    prev_color = screen[x][y]
    return screen

def write(screen,x,y):
    global prev_x
    global prev_y
    global prev_color
    cv2.line(screen, (prev_x, prev_y), (x, y), (0, 0, 0), 5)
    #prev_x, prev_y = x, y
    prev_color = tuple(black)
    return screen



def analyze(img):
    if filter(img, green):
        x, y = filter(img,green)
        return x,y,2
    if filter(img, orange) and filter(img, pink):
        x, y = filter(img, orange)
        return x,y,1
    elif filter(img, orange):
        x, y = filter(img,orange)
        return x,y,0
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


screen1 = default_screen()
screen2 = screen = np.ones((L2, B2), np.uint8) * 255
while 1:
    ret, frame = cap.read()
    frame = frame[:, ::-1]
    #cv2.imshow("orig", frame)
    x, y, code = analyze(frame)
    x, y = scale(x, y, L1, B1, L2, B2)
    if x >= L2:
        x = L2-1
    if y >= B2:
        y = B2-1

    if code==0:
        point(screen2, x, y)
    elif code==1:
        write(screen1, x, y)
        point(screen2, x, y)
    elif code==2:
        screen1 = default_screen()
        screen2 = np.ones((L2, B2), np.uint8) * 255
    screen = cv2.bitwise_and(screen1, screen2)
    #cv2.imshow("point", screen2)
    #cv2.imshow("write", screen1)
    cv2.imshow("screen", screen)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


cv2.destroyAllWindows()
cap.release()