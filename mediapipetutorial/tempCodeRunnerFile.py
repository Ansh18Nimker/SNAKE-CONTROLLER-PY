import cv2
import mediapipe as mp
import time
import handtracking as htm
import numpy as np

pTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

# Subtle colors
ACCENT_COLOR = (100, 200, 100)  # Soft green
TEXT_COLOR = (255, 255, 255)    # White
DARK_BG = (30, 30, 30)          # Dark gray

def draw_overlay(frame, fps):
    h, w = frame.shape[:2]
    
    # Simple top bar
    cv2.rectangle(frame, (0, 0), (w, 60), DARK_BG, -1)
    
    # Title
    cv2.putText(frame, "Snake Controller", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, TEXT_COLOR, 2)
    
    # FPS counter
    fps_text = f"FPS: {int(fps)}"
    cv2.putText(frame, fps_text, (w - 150, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, ACCENT_COLOR, 2)
    
    return frame

def draw_hand_points(frame, lmList):
    # Draw connections
    connections = [
        (0, 1), (1, 2), (2, 3), (3, 4),
        (0, 5), (5, 6), (6, 7), (7, 8),
        (0, 9), (9, 10), (10, 11), (11, 12),
        (0, 13), (13, 14), (14, 15), (15, 16),
        (0, 17), (17, 18), (18, 19), (19, 20),
        (5, 9), (9, 13), (13, 17)
    ]
    
    for connection in connections:
        if connection[0] < len(lmList) and connection[1] < len(lmList):
            x1, y1 = lmList[connection[0]][1], lmList[connection[0]][2]
            x2, y2 = lmList[connection[1]][1], lmList[connection[1]][2]
            cv2.line(frame, (x1, y1), (x2, y2), ACCENT_COLOR, 2)
    
    # Draw landmarks
    for lm in lmList:
        x, y = lm[1], lm[2]
        cv2.circle(frame, (x, y), 5, ACCENT_COLOR, -1)
    
    return frame

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    
    frame = detector.findHands(frame, draw=False)
    lmList = detector.findPosition(frame, draw=False)

    if len(lmList) != 0:
        frame = draw_hand_points(frame, lmList)
        
        # Small marker on index finger
        if len(lmList) > 8:
            x, y = lmList[8][1], lmList[8][2]
            cv2.circle(frame, (x, y), 12, (0, 255, 0), 2)

    # Calculate FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    frame = draw_overlay(frame, fps)

    cv2.imshow("Snake Controller", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()