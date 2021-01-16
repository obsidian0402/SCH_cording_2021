import numpy as np
import cv2

'''
#shape : 각 차원 크기. (h,w)or(h,w,3)
#dtype : 원소의 데이터 타입. 일반적 영상 -> numpy.unit8
#arr : 생성된 영상(numpy.ndarray)

numpy.empty(shape,dtype=float,... )  임의의값으로 초기화된 배열 생성
numpy.zero(shape,dtype=float,... ) 0으로 초기화된 배열 생성
numpy.ones(shape, dypte=none,...) 1로 초기화된 배열 생성
numpy.full(shape, fill_value, dtype=none,...) fill_value로 초기화된 배열 생성(특정한 숫자값 지정하여 생성) (BGR 순서!) 단순 숫자 넣으면 같은 숫자로 통일
'''

# 새 영상 생성하기

img1 = np.empty((240, 320), dtype=np.uint8)   # grayscale image
img2 = np.zeros((240, 320, 3), dtype=np.uint8)  # color image
img3 = np.ones((240, 320), dtype=np.uint8) * 255  # dark gray
img4 = np.full((240, 320, 3), (0, 255, 255), dtype=np.uint8)  # yellow  (BGR 순서!)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()

# 영상 복사
img1 = cv2.imread('HappyFish.jpg')

img2 = img1  #2는 1과 같은 코드 공유
img3 = img1.copy() #복사본 아예 생성 (이후 img1 수정하든 상관x)
img1[:, :] = (0, 255, 255)  
#img1.fill(255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()

# 부분 영상 추출
img1 = cv2.imread('HappyFish.jpg')

img2 = img1[40:120, 30:150]  # numpy.ndarray의 슬라이싱
img3 = img1[40:120, 30:150].copy()

#img1[:,:]=(0,255,255)  #이후 img1을 바꾸면 img2도 바뀜
#img2.fill(0) #영상 특정 부분 처리 할때 사용 (잘라내서 다른것으로 채움.)
cv2.circle(img2, (50,50), 20, (0,0,255), 2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()
