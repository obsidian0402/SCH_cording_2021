import matplotlib.pyplot as plt
import cv2


# 컬러 영상 출력
imgBGR = cv2.imread('cat.bmp')  #imread 는 BGR 순서
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB) #RGB순서로 바꿔줌

plt.axis('off') #x,y축표시 off
plt.imshow(imgRGB)
plt.show()

# 그레이스케일 영상 출력
imgGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()
