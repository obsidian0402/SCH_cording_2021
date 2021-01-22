import sys
import cv2

print('Hello, OpenCV', cv2.__version__)

img = cv2.imread('cat.bmp')  # 파일을 불러와 img에 대입

if img is None:  # 영상을 제대로 못불러 왔을때
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image')  # opencv창 만들기
cv2.imshow('image', img)  # 창에 이미지 보여줌
cv2.waitKey()  # 아무키나 누를때까지 계속 보여줌

cv2.destroyAllWindows()
