# 🐍 Hand-Controlled Snake Game using Python

🎮 Control the classic **Nokia Snake Game** with your **hand gestures** — no keyboard required!  
This project uses **OpenCV**, **MediaPipe**, and **Pygame** to detect your hand via webcam and move the snake based on your **index finger position** in real time.  

---

## 🚀 Demo
🎥 *Demo video coming soon!*  
Once finalized, this section will include a short gameplay clip showing the snake being controlled through fingertip movement.  

---

## 🧠 Features
- 🖐️ **Real-time hand tracking** using [MediaPipe Hands](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker)
- 🧩 **OpenCV integration** for webcam feed and fingertip detection
- 🐍 **Pygame-based snake logic** with score tracking
- ⚡ Smooth and responsive movement mapped to your finger
- 🎨 Customizable speed, colors, and retro Nokia-style theme

---

## 🧰 Tech Stack
| Library | Purpose |
|----------|----------|
| **Python** | Core programming language |
| **OpenCV** | Camera input & frame processing |
| **MediaPipe** | Hand and fingertip tracking |
| **Pygame** | Game window, snake logic & rendering |
| **NumPy** | Coordinate & array handling |

---

## 📚 What I’m Learning
I’m currently exploring:
- 🧠 **Computer Vision** fundamentals through OpenCV  
- 🖐️ **Gesture and Hand Tracking** using MediaPipe  
- 🎮 **Game development logic** with Pygame  
- 🤖 How to combine AI concepts with real-world applications  

This project helped me *connect my Data Science learning path with hands-on coding* — turning concepts into something visual and interactive!

---

## ⚙️ Installation
1. **Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/hand-controlled-snake.git
   cd hand-controlled-snake
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run the project

bash
Copy code
python main.py
Controls

Move your index finger in front of the webcam to control the snake.

Press Q to quit.

🪄 How It Works
MediaPipe Hands detects 21 keypoints on your hand.

The coordinates of your index fingertip (ID 8) are extracted.

These (x, y) coordinates are mapped to the snake’s head in the Pygame window.

The snake moves according to your hand movement, eats food, and grows — just like the original Snake game!

🧩 File Structure
bash
Copy code
hand-controlled-snake/
│
├── hand_tracking.py      # Handles webcam and fingertip detection
├── snake_game.py         # Core snake logic (keyboard version)
├── main.py               # Combined control (hand + game)
├── requirements.txt      # Dependencies
└── README.md             # Project info (this file)
🎓 What I Learned
Integrating computer vision with game development

Using MediaPipe landmarks for gesture-based control

Managing real-time frame updates efficiently with OpenCV

Combining multiple Python libraries into a single cohesive project

📸 Credits & Inspiration
Inspired by Programming Hero’s Snake Hand Controller

Built while learning Computer Vision & AI concepts 🎯

👨‍💻 About Me
👋 Hi, I’m Ansh Nimker, currently pursuing MCA @ USICT (2025–2027).
I’m learning Data Science, AI, and Computer Vision, and I love building fun, visual projects like this to strengthen my fundamentals.


⭐ If you liked this project, drop a star on the repo — it keeps the motivation alive! ⭐

yaml
Copy code
