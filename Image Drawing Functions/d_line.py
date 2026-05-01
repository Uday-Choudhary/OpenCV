import cv2
from pathlib import Path

image_path = Path(__file__).parent / "minions.jpg"
image = cv2.imread(str(image_path))

if image is None:
    print('Image not found')
else:
    print("Image loaded")

    (h, w) = image.shape[:2]

    pt1 = (0, 0)
    pt2 = (w+10, h+10   )
    color = (255, 23, 234)  # Blue color in BGR
    thickness = 5

    cv2.line(image, pt1, pt2, color, thickness)

    cv2.imshow('Image with Line', image)
    cv2.imwrite('line-minion.png', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()