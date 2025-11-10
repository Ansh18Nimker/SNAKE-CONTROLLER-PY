import tkinter
import random
import cv2
import time
import handtracking as htm

# Camera + Hand Tracking Setup
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
prev_x = None
prev_y = None

# Smooth control tuning
last_turn_time = time.time()
TURN_DELAY = 0.25          # seconds between allowed turns
MOVE_THRESHOLD = 40        # minimum pixels finger must move

ROWS = 25
COLS = 25
TILE = 25

WINDOW_WIDTH = TILE * COLS
WINDOW_HEIGHT = TILE * ROWS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Tkinter Window Setup
window = tkinter.Tk()
window.title("Snake Game")
window.resizable(False, False)

canvas = tkinter.Canvas(
    window, bg="black",
    width=WINDOW_WIDTH, height=WINDOW_HEIGHT,
    borderwidth=0, highlightthickness=0
)
canvas.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Initialize Game
snake = Tile(5*TILE, 5*TILE)
food = Tile(10*TILE, 10*TILE)
snake_body = []
velocityX = 0
velocityY = 0
gameover = False
score = 0

# Restart function
def reset_game():
    global snake, food, snake_body, velocityX, velocityY, gameover, score
    snake = Tile(5*TILE, 5*TILE)
    food = Tile(10*TILE, 10*TILE)
    snake_body = []
    velocityX = 0
    velocityY = 0
    score = 0
    gameover = False

# Bind R key
window.bind("r", lambda e: reset_game())
window.bind("R", lambda e: reset_game())

# HAND CONTROL WITH CAMERA WINDOW + SMOOTHING
def update_direction_from_finger():
    global velocityX, velocityY, prev_x, prev_y, last_turn_time, gameover

    if gameover:
        return

    success, frame = cap.read()
    if not success:
        return

    frame = cv2.flip(frame, 1)
    frame = detector.findHands(frame, draw=True)
    lmList = detector.findPosition(frame, draw=False)

    # Draw & detect index finger
    if len(lmList) > 8:
        x_f, y_f = lmList[8][1], lmList[8][2]
        cv2.circle(frame, (x_f, y_f), 20, (0, 255, 0), 2)
        cv2.circle(frame, (x_f, y_f), 8, (0, 255, 0), -1)
        cv2.putText(frame, "CONTROL", (x_f - 40, y_f - 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Only update turn if enough time passed
        if prev_x is not None and prev_y is not None:
            dx = x_f - prev_x
            dy = y_f - prev_y

            if time.time() - last_turn_time > TURN_DELAY:

                # Horizontal turn
                if abs(dx) > abs(dy):
                    if dx > MOVE_THRESHOLD and velocityX != -1:
                        velocityX, velocityY = 1, 0
                        last_turn_time = time.time()

                    elif dx < -MOVE_THRESHOLD and velocityX != 1:
                        velocityX, velocityY = -1, 0
                        last_turn_time = time.time()

                # Vertical turn
                else:
                    if dy < -MOVE_THRESHOLD and velocityY != 1:
                        velocityX, velocityY = 0, -1
                        last_turn_time = time.time()

                    elif dy > MOVE_THRESHOLD and velocityY != -1:
                        velocityX, velocityY = 0, 1
                        last_turn_time = time.time()

        prev_x, prev_y = x_f, y_f

    # Always show control window
    cv2.imshow("Snake Controller", frame)
    cv2.waitKey(1)


def move():
    global snake, gameover, food, snake_body, score

    if gameover:
        return

    # Wall collision
    if snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT:
        gameover = True
        return

    # Self collision
    for tile in snake_body:
        if snake.x == tile.x and snake.y == tile.y:
            gameover = True
            return

    snake.x += velocityX * TILE
    snake.y += velocityY * TILE

    # Eating food
    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS - 1) * TILE
        food.y = random.randint(0, ROWS - 1) * TILE
        score += 1

    # Move body
    for i in range(len(snake_body)-1, -1, -1):
        tile = snake_body[i]
        if i == 0:
            tile.x = snake.x - velocityX * TILE
            tile.y = snake.y - velocityY * TILE
        else:
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y


def draw():
    global snake, food, snake_body, gameover, score

    update_direction_from_finger()
    move()
    canvas.delete("all")

    # Draw food
    canvas.create_rectangle(food.x, food.y, food.x+TILE, food.y+TILE, fill="red")

    # Draw snake
    canvas.create_rectangle(snake.x, snake.y, snake.x+TILE, snake.y+TILE, fill="lime green")
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x+TILE, tile.y+TILE, fill="lime green")

    if gameover:
        canvas.create_text(window_width/2, window_height/2 - 20, font="Arial 20", text=f"Game Over : {score}", fill="white")
        canvas.create_text(window_width/2, window_height/2 + 20, font="Arial 12", text="Press R to Restart", fill="yellow")
    else:
        canvas.create_text(30, 20, font="Arial 10", text=f"Score:{score}", fill="white")

    window.after(150, draw)


draw()
window.mainloop()

cap.release()
cv2.destroyAllWindows()
