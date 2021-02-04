import sys
import numpy as np
import cv2

'''
모멘트(moment) : 영상의 형태를 표현하는 일련의 실수 값.
                특정 함수집학과의 상관관계(correlation) 형태로 계산.

Hu의 7개 불변 모멘트
    - 3차 이하의 정규화된 중심 모멘트를 조합하여 만든 7개의 모멘트 값
    - 영상의 <크기,회전,이동,대칭> 변환에 불변. (그외의 변환에는 좋은 결과 기대하기 어려움.)

cv2.matchShapes(contour1, contour2, method, parameter) -> retval
contour : 1,2번째 외곽선 또는 그레이스케일 영상.
method : 비교 방법 지정. cv2.CONTOURS_MATCH_I1 또는 I2, I3
parameter : 사용x (0)
retval : 두 외곽선 또는 그레이스케일 영상 사이의 거리
'''


# 영상 불러오기
obj = cv2.imread('spades.png', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('symbols.png', cv2.IMREAD_GRAYSCALE)

if src is None or obj is None:
    print('Image load failed!')
    sys.exit()

# 객체 영상 외곽선 검출
_, obj_bin = cv2.threshold(obj, 128, 255, cv2.THRESH_BINARY_INV)  #이진화후 사용
obj_contours, _ = cv2.findContours(obj_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
obj_pts = obj_contours[0]

# 입력 영상 분석
_, src_bin = cv2.threshold(src, 128, 255, cv2.THRESH_BINARY_INV)  # 이진화후 사용
contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 결과 영상
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

# 입력 영상의 모든 객체 영역에 대해서
for pts in contours:
    if cv2.contourArea(pts) < 1000: 
        continue  #노이즈제거

    rc = cv2.boundingRect(pts)
    cv2.rectangle(dst, rc, (255, 0, 0), 1)

    # 모양 비교
    dist = cv2.matchShapes(obj_pts, pts, cv2.CONTOURS_MATCH_I3, 0)

    #일치율 표시(작을수록 일치)

    cv2.putText(dst, str(round(dist, 4)), (rc[0], rc[1] - 3),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1, cv2.LINE_AA)
    
    if dist < 0.1:
        cv2.rectangle(dst, rc, (0, 0, 255), 2)

cv2.imshow('obj', obj)
cv2.imshow('dst', dst)
cv2.waitKey(0)
