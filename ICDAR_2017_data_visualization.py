#written for gt_img_47.txt and image file img_47.jpg for ICDAR 2017 data
import cv2

image = cv2.imread("your_image_path")
cv2.imshow("Image",image)
cv2.waitKey(0)

tl = (531,224)
tr = (608,224)
br = (608,236)
bl = (531,236)

cv2.circle(image,tl, 8, (0,0,0), -1)#top left
cv2.circle(image,tr, 8, (0,0,0), -1)#top right
cv2.circle(image,bl, 8, (0,0,0), -1)#bottom left
cv2.circle(image,br, 8, (0,0,0), -1)#bottom right

#531,224,608,224,608,236,531,236,Ex-boyfriend

cv2.rectangle(image,tl,br,(0,0,0),2)
cv2.imshow("rec",image)
cv2.waitKey(0)
