import cv2

img = cv2.imread('assets/logo.jpeg', 1)

if img is None:
    print("Error loading image.")
else:
    print("Image shape:", img.shape)

    # copy from y=90:110, x=150:170 (both safe)
    tag = img[90:110, 150:170]

    # paste safely at y=150:170, x=180:200
    img[150:170, 180:200] = tag

    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
