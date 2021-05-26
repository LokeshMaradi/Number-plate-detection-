import cv2
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,150)
iPlate=cv2.CascadeClassifier('Resources\haarcascades\haarcascade_russian_plate_number.xml')
minArea=500
count=0
while True:
    success,img=cap.read()
    imgG=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    plates=iPlate.detectMultiScale(imgG,1.1,4,)
    for (x,y,w,h) in plates:
        area=w*h
        if area>minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
            cv2.putText(img,'Number Plate',(x,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)
            imgCrop=img[y:y+h,x:x+w]
            cv2.imshow('op1',imgCrop)
    cv2.imshow('op2',img)
    if cv2.waitKey(1) & 0xFF==ord('s'):
        cv2.imwrite("Resources\scanned\_"+str(count)+".jpg",imgCrop)
        cv2.rectangle(img,(0,200),(640,400),(0,255,0),cv2.FILLED)
        cv2.putText(img,'Saved',(50,250),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),5)
        cv2.imshow('op2',img)
        cv2.waitKey(500)
        count+=1



