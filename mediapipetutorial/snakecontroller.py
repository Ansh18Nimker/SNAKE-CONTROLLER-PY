import cv2
import mediapipe as mp
import time
import handtracking as htm

pTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()


ACCENT_COLOR = (0, 255, 0)  
TEXT_COLOR = (255, 255, 255)

def draw_overlay(frame, fps):
    h, w = frame.shape[:2]
    
    cv2.rectangle(frame, (0, 0), (w, 60), (30, 30, 30), -1)
    
    cv2.putText(frame, "Snake Controller", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, TEXT_COLOR, 2)
    cv2.putText(frame, f"FPS: {int(fps)}", (w - 150, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, ACCENT_COLOR, 2)
    
    return frame

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame, draw=False)

    if len(lmList) != 0:
        x, y = lmList[8][1], lmList[8][2]
        
        cv2.circle(frame, (x, y), 20, ACCENT_COLOR, 2)
        cv2.circle(frame, (x, y), 8, ACCENT_COLOR, -1)
        
        cv2.putText(frame, "CONTROL", (x - 40, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ACCENT_COLOR, 2)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    frame = draw_overlay(frame, fps)

    cv2.imshow("Snake Controller", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()