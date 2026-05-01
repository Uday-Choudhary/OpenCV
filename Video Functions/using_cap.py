import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # print(ret , frame)
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow('Webcam Feed', frame)
# 0xFF is used to get the last 8 bits of the key pressed, which is necessary for compatibility across different platforms and OpenCV versions. The ord('q') function returns the ASCII value of the character 'q', allowing us to check if the 'q' key was pressed to exit the loop.

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting...")
        break

cap.release()
cv2.destroyAllWindows()