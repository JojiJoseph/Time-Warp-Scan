import cv2
import numpy as np
import time
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-d","--direction",default="tb", choices=["tb", "bt","lr","rl"])

direction = parser.parse_args().direction

cap = cv2.VideoCapture(2)

ret, ref = cap.read()

h, w, _ = ref.shape

print(h,w)

output = np.zeros((h,w,3), dtype=np.uint8)

end = h if direction in ["tb","bt"] else w
for i in range(0,end,2):
    frame_start_time = time.time()
    ret, frame = cap.read()
    if direction == "tb":
        output[i:i+2] = frame[i:i+2].copy()
        frame[:i+2] = output[:i+2]
        cv2.line(frame, (0,i), (w,i), (255,255,255), 2)
    elif direction == "bt":
        output[h-(i+2):h-i] = frame[h-(i+2):h-i].copy()
        frame[h-(i+2):] = output[h-(i+2):]
        cv2.line(frame, (0,h-i), (w,h-i), (255,255,255), 2)
    elif direction == "lr":
        output[:,i:i+2] = frame[:,i:i+2].copy()
        frame[:,:i+2] = output[:,:i+2]
        cv2.line(frame, (i,0), (i,h), (255,255,255), 2)
    elif direction == "rl":
        output[:,w-(i+2):w-i] = frame[:,w-(i+2):w-i].copy()
        frame[:,w-(i+2):] = output[:,w-(i+2):]
        cv2.line(frame, (w-i,0), (w-i,h), (255,255,255), 2)
    cv2.imshow("Input", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    print("fps:", 1/(time.time()-frame_start_time))

cv2.imwrite("scanned.png", output)

cap.release()