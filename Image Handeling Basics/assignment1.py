import cv2
from pathlib import Path

image_path = Path(__file__).parent / "minions.jpg"

image = cv2.imread(str(image_path))

if image is not None:
    grey_image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)  
    choice = input('Save or Show: ')
    if choice == 'Show':
        cv2.imshow('minion',grey_image)
        cv2.waitKey()
        cv2.destroyAllWindows()
    elif choice == 'Save':
        cv2.imwrite(input('Enter the filename to save the grey image: ') + '.png', grey_image)
    print('all done')
else:
    print('Error')