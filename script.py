import cv2
import numpy as np

cap = cv2.VideoCapture('./input.mp4')

font = cv2.FONT_HERSHEY_SIMPLEX 
fontColor = (255, 255, 255)
fontThickness = 2

def on_click(event, x, y, p1, p2):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x)
        print(y)
        print(p1)
        print(p2)


roi = None
while(cap.isOpened()):
    rect, current_frame = cap.read()
    if roi is None:
        roi = cv2.selectROI("roi pane", current_frame, False)
        cv2.imshow("image", current_frame)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', on_click)
        print(roi)

    cropped_frame = current_frame[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
    skewed_frame = current_frame

    cv2.putText(current_frame, 'input stream', (200, 90), font, fontThickness, fontColor, 5)
    cv2.imshow("Current frame", current_frame)
    cv2.imshow("cropped frame", cropped_frame)

    rows,cols,ch = cropped_frame.shape
    pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(current_frame, M,(1920,1080))
    cv2.imshow("warped frame", dst)
    cv2.waitKey(1)
