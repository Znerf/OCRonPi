import numpy as np
import cv2
import mapper


img = cv2.imread("ery1.jpg")
 
img=cv2.resize(img,(700,700))
_, threshold = cv2.threshold(img, 155, 255, cv2.THRESH_BINARY)
 
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
mean_c = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 12)
gaus = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 12)
# ret, otsu = cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# im=img.copy()
# for i in xrange(400):
# 	for j in xrange(700):
# 		im[i][j]=(gaus[i][j]+otsu[i][j])/2

# img_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
 
# mean_c = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 12)
# gaus = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 12)
 
# mean_c1 = cv2.adaptiveThreshold(gaus, 100, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 12)
# gaus1 = cv2.adaptiveThreshold(img_gray1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 12)

# cv2.imshow("Img", img)
# cv2.imshow("Binary threshold", threshold)
# cv2.imshow("Mean C", mean_c)
cv2.imshow("Gaussian", gaus)
cv2.imwrite('01.png',gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''code 1'''



# Load an color image in grayscale
# img = cv2.imread('img')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# thresh = cv2.GaussianBlur(img,(5,5),0)
# edges = cv2.Canny(img,100,200)
# cv2.imshow("Original.jpg", edges)

# ret, thresh= cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)


# denoised = cv2.fastNlMeansDenoising(thresh, 11, 31, 9) # you may experiment with the constants here
image=cv2.imread("try.jpg")   #read in the image
image=cv2.resize(image,(1300,800)) #resizing because opencv does not work well with bigger images
orig=image.copy()

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)  #RGB To Gray Scale
# cv2.imshow("Title",gray)


blurred=cv2.GaussianBlur(gray,(5,5),0)  #(5,5) is the kernel size and 0 is sigma that determines the amount of blur
# cv2.imshow("Blur",blurred)

edged=cv2.Canny(blurred,30,50)  #30 MinThreshold and 50 is the MaxThreshold
cv2.imshow("Canny",edged)


image,contours,hierarchy=cv2.findContours(edged,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  #retrieve the contours as a list, with simple apprximation model

contours=sorted(contours,key=cv2.contourArea,reverse=True)
img = np.zeros( (1300,800) ) # create a single channel 200x200 pixel black image 
for i in xrange(1300):
	for j in xrange(800):
		img[i][j]=255
for c in contours:

	cv2.fillPoly(img, pts =[np.asarray(c)], color=(0,0,0))
# 	cv2.imshow(" ", img)
#     p=cv2.arcLength(c,True)
#     approx=cv2.approxPolyDP(c,0.02*p,True)

#     if len(approx)==4:
#         target=approx
#         break
# approx=mapper.mapp(target) #find endpoints of the sheet
# img = cv2.bitwise_not(img)
# pts=np.float32([[0,0],[800,0],[800,800],[0,800]])  #map to 800*800 target window

# op=cv2.getPerspectiveTransform(approx,pts)  #get the top or bird eye view effect
# dst=cv2.warpPerspective(orig,op,(800,800))


cv2.imshow("Scanned",img)


cv2.imwrite('01.png',gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()