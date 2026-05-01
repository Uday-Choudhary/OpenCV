import cv2
from pathlib import Path

image_path = Path(__file__).parent / "minions.jpg"
image = cv2.imread(str(image_path))

if image is None:
    print('Image not found')
else:
    print('Image loaded')
    pt1 = (50, 50)
    pt2 = (200, 200)
    color = (0, 255, 0)  # Green color in BGR
    thickness = 3

    cv2.rectangle(image , pt1 , pt2 , color , thickness)
    cv2.imshow('Image with Rectangle' , image)
    cv2.imwrite('rectangle-minion.png' , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()