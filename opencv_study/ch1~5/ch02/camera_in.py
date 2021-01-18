import sys
import cv2



'''
# 카메라 열기

cv2.VideoCapture(index(filname), apiPreference=None) -> retval
index : camera_id + domain_offset_id
        시스템 기본 카메라를 기본 방법으로 열려면 index에 0을 전달
        or
        비디오 파일 이름, 정지영상시쿼스,비디오스트림URL 등
apiPreference : 선호하는 카메라(동영상) 처리 방법 지정
retval : cv2.VideoCapture 객체

cv2.VideoCapture.open(index, apiPreference=None) -> retval
retval : T/F

#비디오 캡처 준비 확인/프레임 받아오기
cv2.VideoCapture.isOpened() -> retval(T/F)

cv2.VideoCapture.read(image=None) -> retval(T/F), image
image : 현재 프레임(numpy.ndarray)
'''
cap = cv2.VideoCapture() # 클래스 생성
cap.open(0)
#한줄코드 : cap = cv2.VideoCapture(0)

if not cap.isOpened(): #예외처리
    print("Camera open failed!")
    sys.exit()

# 카메라 프레임 크기 출력
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 카메라 프레임 처리
while True:
    ret, frame = cap.read() #ret 에서는 T/F, frame -> 불리언과 같이 가져오기때문에 두개 지정.

    if not ret: #false면 중단
        break
    
    #윤곽선 영상 만들기
    edge =cv2.Canny(frame, 50, 150)


    #반전
    inversed = ~frame  # 반전

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)
    cv2.imshow('edge', edge)

    if cv2.waitKey(10) == 27: #10초 기다린다. esc(27) 을 누르면 break
        break
'''
cv2.VideoCapture.get(propId) -> retval(실패시 0)
propId : 속성상수(CAP_PROP_TEXT)
TEXT : FRAME_WITDH, FRAME_HEIGT, FPS, FRAME_COUNT 등(OPENCV 문서 참고)

'''
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(w, h)

'''
#카메라, 비디오 장치 속성 값 참조
cv2.VideoCapture.set(propId, value) -> retval(T/F)
propId : 속성 상수
value: 속성값
'''
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(w, h)

cap.release()
cv2.destroyAllWindows()
