import sys
import numpy as np
import cv2

'''
<케니 에지 검출>
1단계 : 가우시안 필터링(optional : 잡음 제거 목적)
2단계 : 그래디언트 계산 (주로 소벨 마스크 사용, 4구역(0,45,90,135) 으로 단순화)
3단계 : 비최대 억제(여러개) ,그래디언트 방향에 위치한 두개 픽셀 조사후 국지적 최대 검사(에지는 그레디언트와 수직방향)
4단계 : 히스테리시스 에지 트래킹, 두개의 임계값 사용(강한 에지와 연결 되어 있는 픽셀만 최종에지)


cv2.Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None)-> edges
image : 입력영상
threshold1 : 하단 임계값  #1:2 OR 1:3
threshold2 : 상단 임계값
edges : 에지 영상
apertureSize : 소벨 연산을 위한 커널 크기. 기본값 3
L2gradient : T=L2norm, F=L1norm (기본=F)
'''

src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.Canny(src, 50, 150)
#dst = cv2.Canny(src, 50, 150)  선 구분 더 없어짐.
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
