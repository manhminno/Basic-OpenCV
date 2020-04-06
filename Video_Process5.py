import cv2
import numpy as np


def Mouse_event(event, x, y, f, img):
    if event == cv2.EVENT_LBUTTONDOWN:
        Mouse_event.x0 = x
        Mouse_event.y0 = y
        Mouse_event.draw = True    
    
    if event == cv2.EVENT_LBUTTONUP:
        Mouse_event.x1 = x
        Mouse_event.y1 = y
        Mouse_event.draw = False
        miny = min(Mouse_event.y0,Mouse_event.y1)
        maxy = max(Mouse_event.y0, Mouse_event.y1)
        minx = min(Mouse_event.x0, Mouse_event.x1)
        maxx = max(Mouse_event.x0, Mouse_event.x1)
        Mouse_event.img = img[miny:maxy,minx:maxx]
    
    if event == cv2.EVENT_MOUSEMOVE:
        Mouse_event.x = x
        Mouse_event.y = y            

Mouse_event.img = None
Mouse_event.x0 =0
Mouse_event.y0 =0
Mouse_event.x1 =0
Mouse_event.y1 =0
Mouse_event.x =0
Mouse_event.y =0
Mouse_event.draw = False


def selPic(winname,img):
    cv2.setMouseCallback(winname, Mouse_event, img)
    if Mouse_event.draw:
        img = cv2.rectangle(img, (Mouse_event.x0,Mouse_event.y0),(Mouse_event.x,Mouse_event.y),(0,0,255),2)
    if Mouse_event.img is not None:
        cv2.imshow("IMG", Mouse_event.img)


cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    img2 = img.copy()
    
    #chon vat the:
    selPic('Webcam', img)

    #xu ly bam theo
    if Mouse_event.img is not None:
        result = cv2.cvtColor(Mouse_event.img, cv2.COLOR_BGR2HSV)
        h = np.mean(result[:, :, 0])
        s = np.mean(result[:, :, 1])
        v = np.mean(result[:, :, 2])
        
        #tao nguong
        lower = np.array([h - 30, s - 30, v - 30])
        upper = np.array([h + 30, s + 30, v + 30])
        
        #tao mask
        mask = cv2.inRange(cv2.cvtColor(img, cv2.COLOR_BGR2HSV), lower, upper)
        
        #ve vien khi so sanh voi mau
        res = cv2.matchTemplate(img, Mouse_event.img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val > 0.4:
            h2, w, d = Mouse_event.img.shape
            cv2.rectangle(img, max_loc, (max_loc[0] + w, max_loc[1] + h2), (0, 0, 255), 2)
            cv2.putText(img, str('%.2f'%(max_val*100)) + '%', max_loc, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Result', mask)

    cv2.imshow('Webcam', img)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows