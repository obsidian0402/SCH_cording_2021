
'''캐스케이드 분류기 : 얼굴 검출
- Viola-Jones 얼굴 검출기
Positive 영상 (얼굴 영상)과 negative 영상(얼굴 아닌 영상)을 훈련하여 빠르고 정화하게 얼굴 영역 검출
- 기존 방법과의 차별점
유사 하르(Harr-like) 특징 사용
Ada Boost에 기반한 강한 분류 성능
캐스케이드(cascade) 방식을 통한 빠른 동작 속도
'''

'''유사 하르(Harr-like)
- 사각형 형태의 필터 집합을 사용
- 흰색 사각형 영역 픽셀 값의 합에서 검정색 사각형 영역 픽셀 값을 뺀 결과 값을 추정
- "눈 사이의 음영"등 인간의 일반적인 특징을 이용하여 찾음.
'''
'''
 캐스케이드 분류기()
일반적인 영상에는 얼굴 1~2개 외에 non-face 영역
non-face 영역 skip 하도록 다단계검사 수행
(1단계(1개) -> 2단계(5개) -> 3단계(20개) )
얼굴과 비슷한 부분은 더 많은 단계를 거쳐서 확정 시킴
'''

import sys
import numpy as np
import cv2

src = cv2.imread('lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

classifier = cv2.CascadeClassifier()
classifier = cv2.CascadeClassifier.load()
