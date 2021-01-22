import sys
import cv2
'''
#저장을 위한 동영상 파일 열기
cv2.VideoWriter(filename, fourcc, frameSize, isColor=None)->retval
fourcc : 영상파일 코텍,압축방식,색상,픽셀 포맷 등을 정의
fps : 초당 프레임수
frameSize : 프레임 크기 (ex[640,480])
isColor : T = 컬러 F= 그외

cv2.VideoWriter.open(filename, fourcc, fps, frameSize, isColor=None) -> retval(T/F)

#비디오 파일 준비되었는지 확인
cv2.VideoWriter.isOpened() -> retval(T/F)

#프레임 저장하기
cv2.VideoWriter.write(image) -> None  
'''

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D', 'I', 'V', 'X'
delay = round(1000 / fps)

out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

if not out.isOpened():
    print('File open failed!')
    cap.release()
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    #inversed = ~frame
    edge = cv2.Canny(frame,50,150)
    edge_color = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    out.write(frame) #소리저장X

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    cv2.imshow('edge_color', edge_color)
    #cv2.imshow('inversed', inversed)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
