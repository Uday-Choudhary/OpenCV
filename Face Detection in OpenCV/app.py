import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

"""detectMultiScale is a method of the CascadeClassifier class in OpenCV that detects objects (in this case, faces) in an image. It takes several parameters, including the input image (gray), scaleFactor, and minNeighbors. The method returns a list of rectangles (x, y, w, h) that represent the detected faces in the image. Each rectangle corresponds to a detected face, where (x, y) is the top-left corner of the rectangle, and (w, h) are the width and height of the rectangle, respectively. The scaleFactor parameter specifies how much the image size is reduced at each image scale, while the minNeighbors parameter specifies how many neighbors each candidate rectangle should have to retain it. A higher minNeighbors value results in fewer detections but with higher quality. The detected faces can then be drawn on the original frame using cv2.rectangle or other drawing functions."""
while True:
    ret , frame = cap.read()

    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray , scaleFactor=1.1 , minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame , (x, y) , (x+w, y+h) , (255, 0, 0) , 2)    
    cv2.imshow('Face Detection' , frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting...")
        break
cap.release()
cv2.destroyAllWindows()