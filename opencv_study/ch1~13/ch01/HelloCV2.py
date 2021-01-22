import sys
import cv2

print('Hello, OpenCV', cv2.__version__)

img = cv2.imread('cat.bmp',cv2.IMREAD_GRAYSCALE)  

if img is None:   #예외처리코드 반드시 추가!
    print('Image load failed!')
    sys.exit()

cv2.imwrite('cat_gray.png',img) #불러온 영상 png로 저장
cv2.namedWindow('image',cv2.WINDOW_NORMAL) #마우스를 이용해서 창 조절 가능,영상크기가 너무 클때 사용
cv2.imshow('image', img) #namedwindow없이도 출력할 수 있음. 작은사이즈영상이라면 named~ 생략가능 
cv2.waitKey()  #반드시 필요함.(imshow와 waitkey 항상 붙어다녀야함)
cv2.destroyAllWindows()

