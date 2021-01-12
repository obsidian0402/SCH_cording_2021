import sys
import cv2

print('Hello, OpenCV', cv2.__version__)

img = cv2.imread('cat.bmp',cv2.IMREAD_GRAYSCALE)  

if img is None:   
    print('Image load failed!')
    sys.exit()

cv2.imwrite('cat_gray.png',img) 
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
while True:
    if cv2.waitKey() == 27: 
        break               #esc를 누르면 27이 반환되고 27받아서 종료
cv2.destroyAllWindows()

