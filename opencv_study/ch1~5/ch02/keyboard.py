import sys
import numpy as np
import cv2

'''
cv2.waitKey(delay=None) -> retval
delay : 밀리초 단위 대기 시간. delay<=0 이면 무한히 기다림. 기본값 0
retval : 눌린 키 값(ASCII code). 눌리지않으면 -1 
특수 키코드 27=ESC, 13=ENTER, 9=TAB
'''
img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)

while True:
    keycode = cv2.waitKey()  
    if keycode == ord('i') or keycode == ord('I'):  # 특정키 입력하면 특수 실행
        img = ~img #논리연산자 '~':반대로 동작
        cv2.imshow('image', img)
    elif keycode == 27:
        break

cv2.destroyAllWindows()
