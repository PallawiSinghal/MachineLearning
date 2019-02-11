import numpy as np
import cv2
from collections import namedtuple

Detection = namedtuple("Detection", ["image_path", "gt", "pred"])
test_images = [Detection("image_2.png", [1033, 375, 1406, 528], [1088, 390, 1458, 600])]

def bb_intersection_over_union(boxA, boxB):
	
	xA = max(boxA[0], boxB[0])
	yA = max(boxA[1], boxB[1])
	xB = min(boxA[2], boxB[2])
	yB = min(boxA[3], boxB[3])
	
	interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)#area of intersection rectangle

	boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)#area of  ground-truth
	boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)#area of both the prediction 


	iou = interArea / float(boxAArea + boxBArea - interArea)#iou

	return iou
if __name__ == '__main__':
	
	for detection in test_images:
		
		image = cv2.imread(detection.image_path)


		cv2.rectangle(image, tuple(detection.gt[:2]), 
			tuple(detection.gt[2:]), (0, 255, 0), 2)

		cv2.rectangle(image, tuple(detection.pred[:2]), 
			tuple(detection.pred[2:]), (0, 0, 255), 2)

		iou = bb_intersection_over_union(detection.gt, detection.pred)

		cv2.putText(image, "IoU: {:.4f}".format(iou), (20, 50),
			cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

		print("{}: {:.4f}".format(detection.image_path, iou))


		cv2.imshow("Image", image)
		cv2.waitKey(0)
