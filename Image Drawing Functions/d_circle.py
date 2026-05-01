import cv2
from pathlib import Path

image_path = Path(__file__).parent / "minions.jpg"
image = cv2.imread(str(image_path))

if image is None:
    print('Image not found')
else:
    print('Image loaded')
    center = (340, 255)
    radius = 76 
    color = (255, 0, 0)  # Blue color in BGR
    thickness = 3

    cv2.circle(image , center , radius , color , thickness)

    cv2.imshow('Image with Circle' , image)
    cv2.imwrite('circle-minion.png' , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
