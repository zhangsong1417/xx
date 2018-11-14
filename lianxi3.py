import  numpy as np
import cv2

img = cv2.imread('test1.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0, 0), (300, 300), (255, 255, 255), 15)

cv2.rectangle(img, (20, 20), (200, 200), (0, 255, 0), 5)
cv2.circle(img, (100, 100), 55, (0, 0, 255), -1)

pts = np.array([[0,0], [0, 300], [300, 300], [300, 0]], np.int32)
cv2.polylines(img, [pts], True, (0, 255, 255), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'opencv test!', (0, 150), font, 2, (255, 255, 255), 3, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
