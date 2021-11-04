import cv2
import numpy as np
import time

cap = cv2.VideoCapture(2)

ret, ref = cap.read()

h, w, _ = ref.shape

print(h,w)

output = np.zeros((h,w,3), dtype=np.uint8)

for i in range(0,h,2):
    frame_start_time = time.time()
    ret, frame = cap.read()
    output[i:i+2] = frame[i:i+2].copy()
    frame[:i+2] = output[:i+2]
    cv2.line(frame, (0,i), (w,i), (255,255,255), 2)
    cv2.imshow("Input", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    print(1/(time.time()-frame_start_time))

cv2.imwrite("scanned.png", output)

cap.release()