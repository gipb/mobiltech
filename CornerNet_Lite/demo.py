#!/usr/bin/env python

import cv2
from core.detectors import CornerNet_Saccade, CornerNet_Squeeze
from core.vis_utils import draw_bboxes
from core.utils.timer import Timer

#detector = CornerNet_Saccade()
detector = CornerNet_Squeeze()
image    = cv2.imread("./images/samples/person.jpg")

timer = Timer()
timer.tic()
bboxes = detector(image)
timer.toc()
image  = draw_bboxes(image, bboxes)
print(f'Elapsed time : {timer.average_time}')
cv2.imwrite("./images/output/person_out.jpg", image)
