import cv2
from pathlib import Path

image_path = Path(__file__).parent / "minions.jpg"
image = cv2.imread(str(image_path))


if image is None:
    print('Image not found')
else:
    print("Image loaded")

    resize = cv2.resize(image , (300,300))

    cv2.imshow('Original Image' , image)

    cv2.imshow('Resize Image' , resize)
    cv2.imwrite('resize-minion.png' , resize)
    cv2.waitKey()
    cv2.destroyAllWindows()