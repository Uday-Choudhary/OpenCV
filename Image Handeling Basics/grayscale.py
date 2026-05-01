import cv2
from pathlib import Path

image_path = Path(__file__).parent / "minions.jpg"
image = cv2.imread(str(image_path))
print(image)


if image is not None:
    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    print(gray)
    cv2.imshow('Gray Minion', gray)
    cv2.waitKey()   
    cv2.destroyAllWindows()
else:
    print('Image not loaded')