import cv2
import numpy as np
import random
import time

# Load the Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Start webcam
cap = cv2.VideoCapture(0)  # Change 0 to the appropriate index if multiple webcams are connected

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

# Wait for 5 seconds before capturing
start_time = time.time()
while time.time() - start_time < 5:
    ret, img = cap.read()
    if not ret:
        break

    # Convert the captured frame to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display the grayscale frame
    cv2.imshow('Webcam Capture (Grayscale)', gray_img)
    if cv2.waitKey(1) == ord('q'):
        break

# Release the webcam before using it again
cap.release()

# Check if the image is loaded successfully
if img is None:
    print("Error loading image.")
    exit()

# Perform face detection on the grayscale image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

# Load the images for overlay
santa = cv2.imread('santa.png', -1)
snowman = cv2.imread('snowman.png', -1)
rudolph = cv2.imread('rudolph.png', -1)
wreath = cv2.imread('wreath.png', -1)
tree = cv2.imread('tree.png', -1)

# Initialize variables for frame decoration
red_frame_color = (0, 0, 139)
red_frame_thickness_horizontal = 80

green_frame_color = (0, 100, 0)
green_frame_thickness_vertical = 80

# Create a copy of the original image for overlay
img_with_overlay = img.copy()

# Add red and green frames to the overlay image
img_with_overlay = cv2.rectangle(img_with_overlay, (0, 0), (img.shape[1], red_frame_thickness_horizontal), red_frame_color, -1)
img_with_overlay = cv2.rectangle(img_with_overlay, (0, img.shape[0] - red_frame_thickness_horizontal), (img.shape[1], img.shape[0]), red_frame_color, -1)

img_with_overlay = cv2.rectangle(img_with_overlay, (0, 0), (green_frame_thickness_vertical, img.shape[0]), green_frame_color, -1)
img_with_overlay = cv2.rectangle(img_with_overlay, (img.shape[1] - green_frame_thickness_vertical, 0), (img.shape[1], img.shape[0]), green_frame_color, -1)

# List of stickers
stickers = [santa, snowman, rudolph, wreath, tree]

# Overlay random stickers on detected faces
for (x, y, w, h) in faces:
    face_image = img[y:y+h, x:x+w]

    # Randomly select a sticker
    overlay_image = random.choice(stickers)

    # Resize sticker to fit within the face region
    overlay_width = w
    overlay_height = int(w * (overlay_image.shape[0] / overlay_image.shape[1]))
    overlay_resized = cv2.resize(overlay_image, (overlay_width, overlay_height))

    # Random position for the sticker within the face region
    rand_x = random.randint(0, w - overlay_width)
    rand_y = random.randint(0, h - overlay_height)

    # Overlay image on the face
    for c in range(0, 3):
        face_image[rand_y:rand_y+overlay_height, rand_x:rand_x+overlay_width, c] = \
            face_image[rand_y:rand_y+overlay_height, rand_x:rand_x+overlay_width, c] * (1 - overlay_resized[:, :, 3] / 255.0) + \
            overlay_resized[:, :, c] * (overlay_resized[:, :, 3] / 255.0)

    img_with_overlay[y:y+h, x:x+w] = face_image

# Display and save the result
cv2.imshow('Result Image', img_with_overlay)
cv2.imwrite('result_image.png', img_with_overlay)
cv2.waitKey(0)
cv2.destroyAllWindows()
