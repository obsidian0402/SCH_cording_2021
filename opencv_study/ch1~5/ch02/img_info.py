import sys
import cv2


# 영상 불러오기
img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Image load failed!')
    sys.exit()

##영상의 속성 참조

print(type(img1))
print(img1.shape) #흑백일때 (h,w)
print(img2.shape) #컬러일때 (h,w,3)
print(img2.dtype)
print(img2.dtype)
if len(img1.shape)==2:
    print('img1 is a grayscale image')

##영상 데이터 대입

print('type(img1):', type(img1))
print('img1.shape:', img1.shape)
print('img2.shape:', img2.shape)
print('img1.dtype:', img1.dtype)


h,w = img1.shape[:2]  #shape튜플값 2번째까지 불러와서 대입
print('w * h = {} * {}'.format(w,h))
h,w = img2.shape[:2]
print('w * h = {} * {}'.format(w,h))

if len(img1.shape) == 2:
    print('img1 is a grayscale image')
elif len(img1.shape) == 3:
    print('img1 is a truecolor image')

x=20   
y=10
p1=img1[y,x]  #특정위치 값 확인
print(p1)
p2=img2[y,x]
print(p2)

img1[y,x]=0      #특정 위치 픽셀대입
img2[y,x]=(0,0,255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

# 영상의 픽셀 값 참조
'''      #쓰지말것! 느리고 비효율적!, c언어는 괜찮음
for y in range(h):
    for x in range(w):
        img1[y, x] = 255
        img2[y, x] = (0, 0, 255)        
'''

#대체 함수
img1[:,:] = 255
img2[:,:] = (0, 0, 255)


cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

cv2.destroyAllWindows()
