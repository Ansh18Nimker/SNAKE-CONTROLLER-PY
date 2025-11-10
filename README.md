# 🐍 Your Hands, Your Controller! (Hand-Controlled Snake Game)

Play the classic Snake Game using only your hand gestures — no keyboard needed.  
Move your index finger in front of the webcam and the snake follows in real time.

Built with Python, OpenCV, MediaPipe, and Tkinter.

## 🚀 Demo
https://drive.google.com/drive/folders/1WVk84TmhdRg9MJjuYYQhjM3Vjcff7NSP?usp=sharing


## ✋ What it does
- Tracks your index finger using the webcam
- Converts finger movement into snake direction
- Snake eats food and score increases
- Game Over on collision
- Press R to restart
- Live camera window + game window

## 🧠 Tech Stack
- Python
- OpenCV
- MediaPipe Hands
- Tkinter


## ✅ How to Run
1. Install dependencies
 - pip install opencv-python mediapipe
2. Run the Game


## ✋ Controls
- Move your index finger to move the snake
- Press R to restart after Game Over
- Close camera window to quit

## 🧩 How it works
- MediaPipe detects 21 hand landmarks
- Landmark ID 8 (index fingertip) is tracked
- Movement in X → left/right
- Movement in Y → up/down
- Movement threshold + delay to prevent jitter

## ✅ Inspiration
Inspired by a reel from Tuba Captures.  
Instead of cloning a repo, I built it step by step and learned OpenCV + MediaPipe properly.

## 👤 Author
Ansh Nimker  
MCA @ USICT (2025–2027)

If you like this project, feel free to star the repo. ⭐


