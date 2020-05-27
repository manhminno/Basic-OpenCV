import numpy as np
import cv2
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", help="Img or Video")
    parser.add_argument("--path", help="Link direct")
    opt = parser.parse_args()
    
    if(opt.mode == "Image"):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades  + 'haarcascade_frontalface_default.xml')

        img = cv2.imread(opt.path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        cv2.imshow('img',img)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x, y-60), (x+w, y+h), (255,0,0), 2)
            img2 = img[y-60+2:y+h-2, x+2:x+w-2]
            cv2.imshow("Face", img2)

        cv2.imshow('img',img)
        k = cv2.waitKey() & 0xff
        if k == ord('q'):
            cv2.destroyAllWindows()

    elif(opt.mode == "Video"):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades  + 'haarcascade_frontalface_default.xml')

        cap = cv2.VideoCapture(0)
        while 1:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img, (x, y-60), (x+w, y+h), (255,0,0), 2)
            
                img2 = img[y-60+2:y+h-2, x+2:x+w-2]
                cv2.imshow("Face", img2)
            
            cv2.imshow('img',img)
            k = cv2.waitKey(24) & 0xff
            if k == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    else:
        print("Add parser: --mode (Image/Video) --path (link_Img)")