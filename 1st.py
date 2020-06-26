import cv2
import numpy as np
'''Showing Images'''
# img = cv2.imread("lena.png")
#
# cv2.imshow("img",img)
# cv2.waitKey(0)
'''Read and show video file'''
# cap = cv2.VideoCapture('test_video.mp4')
#
# while True:
#     success,img = cap.read()
#     cv2.imshow("video",img)
#
#     if cv2.waitKey(1) and 0xFF == ord('q'):
#         break
'''Read and show from webcam'''
# cap = cv2.VideoCapture(0)
# frameWidth = 640
# frameHeight = 480
# while True:
#     success, img = cap.read()
#     img = cv2.resize(img, (frameWidth, frameHeight))
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) and 0xFF == ord('q'):
#          break
'''Important Functions'''
# kernel = np.ones((5,5),np.uint8)
# orig = cv2.imread("lena.png")
# gray = cv2.cvtColor(orig,cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray,(7,7),0)
# canny = cv2.Canny(orig,150,200)
# dilate = cv2.dilate(canny,kernel,iterations=1)
# erode = cv2.erode(dilate,kernel,iterations=1)
# cv2.imshow("Gray",gray)
# cv2.imshow("blur",blur)
# cv2.imshow("canny",canny)
# cv2.imshow("dilated",dilate)
# cv2.imshow("eroded",erode)
# cv2.waitKey(0)
'''Cropping and Resizing'''
# img = cv2.imread("lambo.png")
# print(img.shape)
# imgResize = cv2.resize(img,(700,700))
# print(imgResize.shape)
# cv2.imshow("original",img)
# cv2.imshow("resized",imgResize)
# cv2.waitKey(0)
'''Shapes and Contours'''
# img = np.zeros((512,512,3),np.uint8)
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# cv2.rectangle(img,(100,200),(300,400),(0,0,255),4)
# cv2.circle(img,(img.shape[1]//2,img.shape[0]//2),50,(255,255,0),cv2.FILLED)
# cv2.putText(img,"HELLO",(300,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,0),3)
# cv2.imshow("original",img)
# cv2.waitKey(0)

