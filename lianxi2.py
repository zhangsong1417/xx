"""
获取摄像头视频，并做灰度显示
电脑没有摄像头，执行程序出错（原因不明，调试中---）
"""
import  numpy as np
import cv2

cap = cv2.VideoCapture(1)
fource = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fource, 20.0, (640,480))
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.weite(frame)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()


