import sys
import numpy as np
import cv2
'''
cv2.HouthLines(image, rho, theta, threshold, lines=None, srn=None, stn=None, min_theta=None, max_theta=None)->lines

image : 입력 에지 영상
rho : 축적 배열에서 rho 값의 간격.(1.0->1픽셀 간격)
theta : 축적 배열에서 theta 값의 간격.(np.pi/180 -> 1도 간격)    
    #rho, theta 값 작을수록 축적 배열 커짐 (정교하게 하려면 값 적게 줌.)
threshold : 축적 배열에서 직선을 판단할 임계값
lines : 직선 파라미터(rho,theta) 정보를 담고 있는 numpy.ndarray, shape=(N, 1, 2), dtype = numpy.float32
srn, stn : 멀티 스케일 허프 변환에서 rho 해상도, theta 해상도를 나누는 기본값 = 0(일반 허프 변환)
min_theta, max_theta : 검출할 선분의 최소, 최대 theta 값 
'''

'''
    #확률적 허프 변환에 의한 선분 검출#
cv2.HouthLinesP(image, rho, theta, threshold, lines=None, minLineLength=None, maxLineGap=None) -> lines
image : 입력 에지 영상
lines : 선분의 시작과 끝 좌표(x1,y1,x2,y2) 정보를 담고있는 numpy.ndarray, shape=(N,1,4ㄴ), dtype=numpy.int32
minLineLength : 검출할 선분의 최소 길이
maxLineGap : 직선으로 간주할 최대 에지 점 간격
'''

src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

edges = cv2.Canny(src, 50, 150)

lines = cv2.HoughLinesP(edges, 1, np.pi / 180., 140,
                        minLineLength=50, maxLineGap=5)

dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

if lines is not None:
    for i in range(lines.shape[0]):
        pt1 = (lines[i][0][0], lines[i][0][1])  # 시작점 좌표
        pt2 = (lines[i][0][2], lines[i][0][3])  # 끝점 좌표
        cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
