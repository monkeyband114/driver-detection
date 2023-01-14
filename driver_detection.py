import cv2 


car_detect = cv2.CascadeClassifier('cardetect.xml')

human = cv2.CascadeClassifier('fullbody.xml')

video = cv2.VideoCapture('vidtest.mp4')

while True:
   seucess_true, frame = video.read()
   
   grey_man = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
   train_cars = car_detect.detectMultiScale(grey_man)
   
   train_full = human.detectMultiScale(grey_man)
   
   for (x, y, w, h) in train_cars:
       cv2.rectangle(frame, (x+2, y+2), (x+w, y+h), (0, 225,0), 2)
       cv2.rectangle(frame, (x, y), (x+w, y+h), (225, 225,0), 2)
       
   for (x, y, w, h) in train_full:
       cv2.rectangle(frame, (x, y), (x+w, y+h), (225, 0, 150), 2)
       
   cv2.imshow('i be dead', frame)
   end = cv2.waitKey(1)
    
    
   if end == 81 or end == 113:
        break

video.release()