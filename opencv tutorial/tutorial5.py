import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  width = int(cap.get(3))  #3 is widht
  height = int(cap.get(4))  #4 is height

  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  lower_blue = np.array([40, 120 ,120])
  upper_blue = np.array([130, 255, 255]) #colors from opencv tutorial available on google

  mask = cv2.inRange(hsv, lower_blue, upper_blue) #tells you which part of the image you keep

  result = cv2.bitwise_and(frame, frame, mask=mask) #bitwise_and returns 1 when both the inputs are 1 and 1 only

  cv2.imshow('frame', result)
  cv2.imshow('mask', mask)

  if cv2.waitKey(1) == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()


# BGR_color = np.array([[[255,0,0]]])
# x=cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)
# x[0][]
#convert your own color
