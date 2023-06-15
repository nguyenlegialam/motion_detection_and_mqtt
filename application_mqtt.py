import time
import cv2
from datetime import datetime
from test_http_post import post_http


def camera_motion_detection():
    width, height = 200, 200
    cap = cv2.VideoCapture("rtsp://admin:@172.16.0.4:554/axis-media/media.amp")
    # cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    post_http()
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    out = cv2.VideoWriter(f'E:\Work/videos/camera_id_{datetime.timestamp(datetime.now())}.avi', fourcc, 20.0,
                          (width, height))
    print("start recording")
    t_end = time.time() + 30
    while time.time() < t_end:
        ret, frame1 = cap.read()
        out.write(frame1)
    print("stop recording")
    out.release()
    cap.release()
    cv2.destroyAllWindows()

