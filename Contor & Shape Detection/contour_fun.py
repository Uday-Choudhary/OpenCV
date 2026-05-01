"""
This code demonstrates how to detect contours in an image using OpenCV. It reads an image, converts it to grayscale, applies a binary threshold to create a binary image, and then finds and draws the contours on the original image. The contours are drawn in green color with a thickness of 3 pixels. Finally, the image with the detected contours is displayed in a window. This technique is useful for various applications such as shape detection, object recognition, and image segmentation.
"""
import cv2
from pathlib import Path

image_path = Path(__file__).parent / "someshapes.jpg"

image = cv2.imread(str(image_path))
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)


_ , thresh = cv2.threshold(gray , 240 , 255 , cv2.THRESH_BINARY)

counters , heierarchy = cv2.findContours(thresh , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image , counters , -1 , (0,255,0) , 3)

for counter in counters:
    approx = cv2.approxPolyDP(counter , 0.01*cv2.arcLength(counter , True) , True)
    corners = len(approx)

    if corners == 3:
        shape_name = 'Triangle'
    elif corners == 4:  
        shape_name = 'Quadrilateral'
    elif corners == 5:
        shape_name = 'Pentagon'
    elif corners > 5:
        shape_name = 'Circle'
    else:
        shape_name = 'Unknown'

    labled_shape = cv2.drawContours(image , [approx] , 0 , (0,255,0) , 3)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    cv2.putText(image , shape_name , (x,y) , cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (255,0,0) , 2)

cv2.imwrite('contours_detected.png' , labled_shaped)

cv2.imshow('Contours Detected' , image)
cv2.waitKey(0)
cv2.destroyAllWindows()