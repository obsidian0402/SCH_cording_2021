import sys
import numpy as np
import cv2

'''
cv2.Sobel(src, ddepth, dx, dy, dst=None, ksize=None, scale=None, borderType=None) -> dst
#대부분 dx=1, dy=0, ksize=3  OR dx=0,dy=1,ksize=3 


src : 입력영상
ddepth : 출력 영상 데이터 타입. -1이면 입력 영상과 같은 데이터 타입 사용.
dx : x 방향 미분차수
dy : y 방향 미분차수
dst : 출력 영상(행렬)
ksize : 커널 크기. 기본값=3
scale : 연산 결과에 추가적으로 곱할 값. 기본값 = 1
delta : 연산 결과에 추가적으로 더할 값. 기본값 = 0
borderType : 가장자리 픽셀 확장 방식. 기본 값 = cv2.BORDER_DEFAULT
'''
src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

'''
kernel = np.array([
    [-1,0,1], 
    [-2,0,2], 
    [-1,0,1]], dtype=np.float32) #3x3 행렬

dx = cv2.filter2D(src, -1, kernel, delta=128)
'''

dx = cv2.Sobel(src, -1, 1, 0, delta=128)
dy = cv2.Sobel(src, -1, 0, 1, delta=128)

cv2.imshow('src', src)
cv2.imshow('dx', dx)
cv2.imshow('dy', dy)
cv2.waitKey()

cv2.destroyAllWindows()
