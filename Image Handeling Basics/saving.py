import cv2
from pathlib import Path

image_path = Path(__file__).parent / "minions.jpg"
image = cv2.imread(str(image_path))
print(image)


if image is not None:
    success = cv2.imwrite('output_minion.png' , image)

    if success:
        print('Image saved successfully as output-minion.png')
    else:
        print('failed to save an image')
else:
    print('failed to save image')
