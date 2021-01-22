import sys
import cv2


'''
ROI : 영상에서 특정 연상을 수행하고자하는 임의의 영역
마스크 연산 : 특정함수 (copyTo, calcHist, bitwise_or, matchTemplate 등) 에 ROI연산 지원, 마스크 영상을 인자로 함께 전달함.
마스크 영상 : cv2.CV_8UC1 타입(그레이스케일 영상)
마스크 영상의 픽셀 값이 0이 아닌 위치에서만 연산 수행.
-> 보통 마스크 영상으로는 0 or 255로 구성된 이진영상 사용
'''
'''
cv2.copyTo(src, mask, dst=None) -> dst
src : 입력영상
mask : 마스크 영상. cv2.CV_8U (numpy.uint8)
        0이 아닌 픽셀에 대해서만 복사 연산 수행
dst : 출력 영상.
    src와 크기&타입 같은 dst 이면 dst를 새로 생성X
    다르다면 dst 새로생성&연산 후 반환
'''
# 마스크 영상을 이용한 영상 합성
src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE) #마스크를 자동으로 생성할수도 있음!
dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)


if src is None or mask is None or dst is None: #예외처리
    print('Image load failed!')
    sys.exit() 

#cv2.copyTo(src, mask, dst)  # src,mask 서로 타입이 같아야함  #src의 mask만 따와서 dst 출력

dst[mask > 0] = src[mask > 0]  #불리언 인덱싱
#mask>0 인 값을 다 찾음 -> 참조형태로 복사 (dst값도 다 바뀜)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()

# 알파 채널을 마스크 영상으로 이용
src = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)
logo = cv2.imread('opencv-logo-white.png', cv2.IMREAD_UNCHANGED)

if src is None or logo is None: #예외처리
    print('Image load failed!')
    sys.exit()

mask = logo[:, :, 3]    # mask는 알파 채널로 만든 마스크 영상
logo = logo[:, :, :-1]  # logo는 b, g, r 3채널로 구성된 컬러 영상
h, w = mask.shape[:2]
crop = src[10:10+h, 10:10+w]  # logo, mask와 같은 크기의 부분 영상 추출

cv2.copyTo(logo, mask, crop)
#crop[mask > 0] = logo[mask > 0]

cv2.imshow('src', src)
cv2.imshow('logo', logo)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()
