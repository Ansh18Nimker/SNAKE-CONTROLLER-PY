# 🐍 Your Hands, Your Controller! (Hand-Controlled Snake Game)

🎮 Play the classic Snake Game — but **without a keyboard**.  
Move your **index finger** in front of the webcam, and the snake follows.

Built using **OpenCV + MediaPipe + Python + Tkinter** ✅  
Just raise your hand → the snake moves in real time.

---

## 🚀 Demo
🎥 *Gameplay demo coming soon!*

A short clip of the game controlled by hand gestures will be added here.

---

## ✋ What It Does
✅ Tracks your **index finger** using the webcam  
✅ Uses MediaPipe to detect hand landmarks  
✅ Converts finger movement → snake direction  
✅ Food eating & score system  
✅ Press **R** to restart after Game Over  
✅ Live camera window + snake game window

---

## 🧠 Tech Stack
| Library | Purpose |
|---------|----------|
| **Python** | Core logic |
| **OpenCV** | Webcam feed + fingertip detection UI |
| **MediaPipe Hands** | Real-time hand tracking |
| **Tkinter** | Snake game rendering |
| **NumPy** | Frame & coordinate operations |

---

## 📁 Project Structure
your-hands-your-controller/
│
├── handtracking.py # Handles hand detection & fingertip tracking
├── snake.py # Snake game + hand controls + restart logic
└── README.md # This file

yaml
Copy code

---

## ⚙️ How to Run

1️⃣ **Install dependencies**
```bash
pip install opencv-python mediapipe
2️⃣ Run the snake game


python snake.py
✔ Your webcam will open
✔ A separate snake game window will appear
✔ Move your index finger to control the snake

✋ Controls
Action-                 How
Move Snake-         	Move your index finger
Restart Game-      	Press R
Quit Camera Window-	Press Q (or close window)

Movement is intentionally slow and smoothed so tiny finger shakes don’t cause random turns.

🧩 How It Works
MediaPipe detects 21 landmarks on your hand.

We track landmark ID 8 (index fingertip).

Compare current vs. previous fingertip position:

More movement in X → Left/Right

More movement in Y → Up/Down

Only turn when movement is large enough (no jitter).

🎓 What I Learned
Computer vision fundamentals with OpenCV

Real-time gesture tracking using MediaPipe

Integrating CV with classic game logic

Keeping movement smooth (delay + thresholding)

Restarting game state without closing window

✅ Inspiration
This project was inspired by a short Instagram reel by Tuba Captures.
Instead of cloning an existing GitHub repo, I built it step-by-step myself — learning OpenCV and MediaPipe along the way.

👤 About Me
Hi, I’m Ansh Nimker, currently pursuing MCA @ USICT (2025–2027).
I enjoy building fun, visual Python projects that connect programming with real-world interaction — especially Computer Vision & AI.

⭐ If this project looks fun, feel free to fork it or drop a ⭐ on the repo!

