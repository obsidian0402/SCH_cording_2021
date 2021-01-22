import sys
import numpy as np
import cv2

'''
영상의 그래디언트
- 함수 f(x,y)를 x축과 y축으로 각각 편미분 하여 벡터 형태로 표현한 것.
- 그래디언트 방향 : 세타=tan^-1(f_x/f_y)
- 그래디언트 크기 : 픽셀 값 차이에 비례
- 그레디언트 방향 : 픽셀 값 가장 급격히 증가하는 방향(밝아지는쪽 방향)
'''
'''
cv2.magnitude(x, y, magnitude=None) -> magnitude
x : 2D 벡터의 x좌표 행렬. 실수형.
y : 2D 벡터의 y좌표 행렬. x와 같은 크기. 실수형.
magnitude : 2D 벡터의 크기 행렬. x와 같은 크기, 같은 타입.

cv2. phase(x,y,angle=None,angleInDegrees=None) -> angle
x: 2D 벡터의 x좌표 행렬. 실수형.
y: 2D 벡터의 y좌표 행렬. x와 같은크기
angle : 2D 벡터의 크기 행렬. x와 같은 크기, 같은타입
angleInDegrees : T=각도단위, F= 라디안 단위
'''

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

mag = cv2.magnitude(dx, dy) #x방향과 y방향 조합해서 보여짐 
mag = np.clip(mag, 0, 255).astype(np.uint8)


edge = np.zeros(src.shape[:2], np.uint8)
edge[mag > 120] = 255  
#_, edge = cv2.threshold(mag, 120, 255, cv2.THRESH_BINARY)

cv2.imshow('src', src)
cv2.imshow('mag', mag)
cv2.imshow('edge', edge) 
cv2.waitKey()

cv2.destroyAllWindows()
