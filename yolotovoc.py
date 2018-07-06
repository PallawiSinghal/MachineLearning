import cv2
image = "enter image path"
im = cv2.imread(image,1)

x = 0.5838427947598254
y = 0.5091984231274639
w = 0.7938864628820961
h = 0.8554533508541393
size = im.shape
image_height = size[0]
image_width = size[1]
Bbox_center_x = x * image_width
print Bbox_center_x
Bbox_center_y = y * image_height
Bbox_width = w * image_width
Bbox_height = h * image_height
xmin = Bbox_center_x - (Bbox_width/2)
ymin = Bbox_center_y - (Bbox_height/2)
xmax = Bbox_center_x + (Bbox_width/2)
ymax = Bbox_center_y + (Bbox_height/2)
tl =(int(xmin),int(ymin))
br =(int(xmax),int(ymax))
print "tl",tl
print"br",br
rectangel = cv2.rectangle(im, tl, br, (0, 0,255), 2)
#
cv2.imshow("image", rectangel)
cv2.waitKey(0)
