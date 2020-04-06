import cv2

cap = cv2.VideoCapture("image/videomau.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
wait_time = 1000/fps

while True:
    ret, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(int(wait_time)) == ord('q'):
        break

cv2.destroyAllWindows()