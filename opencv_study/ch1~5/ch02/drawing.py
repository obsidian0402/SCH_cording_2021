import numpy as np
import cv2

'''
#직선그리기
cv2.line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None) -> img
img : 그림 그릴 영상
pt1, pt2  : 직선의 시작과 끝
color : 선 색상, 밝기. bgr 튜플 or 정수
thickness : 선 두께. 기본값=1
linetype : 선타입. cv2.LINE_8, cv2.LINE_AA
shift : 좌표 값의 축소 비율. 기본값=0
'''
img = np.full((400, 400, 3), 255, np.uint8)

cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5)
cv2.line(img, (50, 60), (150, 160), (0, 0, 128))

'''
#사각형그리기
cv2.rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None) -> img
cv2.rectangle(img, rec, color, thickness=None, lineType=None, shift=None) -> img
rec : 사각형 위치 정보.(x,y,w,h) 튜플 x,y= 시작점 w,h=가로,세로
thickness : 선두께, 음수(-1) 지정하면 내부 채움
'''

cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1)

'''
#원그리기
cv2.circle(img, center, radius, color, thickness=None, lineType=None, shift=None) -> img
center : 중심좌표 (x,y)
radius : 반지름

'''

cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA)
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)

'''
#다각형그리기
cv2.polylines(img, pts, isClosed, color, thickness=None, lineType=None, shift=None)->img
pts : 다각형 외곽점들의 좌표 배열. numpy.ndarray 리스트로 감싸서 입력.
isClosed : 폐곡선 여부 , T/F

'''
pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]])
cv2.polylines(img, [pts], True, (255, 0, 255), 2)
#pts = 리스트 형태[pts] 로 감싸서 입력해야함.


'''
문자열출력
cv2.putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=Noen) -> img
text : 출력할 문자열
org : 영상에서 문자열을 출력할 위치의 좌측 하단 좌표
fontFace : 폰트종류. cv2.FONT_HERSHEY_ 로 시작하는 상수 중 선택
fontScale : 폰트 크기 확대/축소 비율
bottomLeftOrigin : True면 영사의 좌측 하단을 원점으로 간주.
'''



text = 'Hello? OpenCV ' + cv2.__version__
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
            (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()

