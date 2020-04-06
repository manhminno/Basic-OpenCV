import numpy as np 
import cv2


def mouse_event(event, x, y, f, img):
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_event.x0 = x
        mouse_event.y0 = y
        mouse_event.draw = True
    if event == cv2.EVENT_LBUTTONUP:
        mouse_event.x1 = x
        mouse_event.y1 = y
        mouse_event.draw = False
        miny = min(mouse_event.y0, mouse_event.y1)
        maxy = max(mouse_event.y0, mouse_event.y1)
        minx = min(mouse_event.x0, mouse_event.x1)
        maxx = max(mouse_event.x0, mouse_event.x1)
        mouse_event.img = img[miny : maxy, minx : maxx]
    if event == cv2.EVENT_MOUSEMOVE:
        mouse_event.x1 = x
        mouse_event.y1 = y

mouse_event.img = None
mouse_event.x0 = 0
mouse_event.y0 = 0
mouse_event.x = 0
mouse_event.y = 0
mouse_event.x1 = 0
mouse_event.x1 = 0
mouse_event.draw = False

cap = cv2.VideoCapture('image/tracking.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
wait = 1000/fps

play = True
while True:
    if play:
        ret, img = cap.read()
    if ret == False:
        break
    
    img_clone = img.copy()

    #xu ly mouse
    cv2.setMouseCallback('Video', mouse_event, img)
    if mouse_event.draw:
        cv2.rectangle(img_clone, (mouse_event.x0, mouse_event.y0), (mouse_event.x1, mouse_event.y1), (0, 0, 255), 2)

    #show anh lay ra:
    if mouse_event.img is not None:
        res = cv2.matchTemplate(img, mouse_event.img, cv2.TM_CCOEFF_NORMED)
        cv2.imshow('Res', res)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if max_val > 0.5:
            h, w, d = mouse_event.img.shape
            cv2.rectangle(img_clone, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 0, 255), 2)
            cv2.putText(img_clone, '%.2f'%max_val, max_loc, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Video', img_clone)
    key = cv2.waitKey(int(wait))
    if key == ord('q'):
        break
    elif key == ord(' '):
        play = not play

cv2.destroyAllWindows()


