"""_OpenCV_
Open Source Computer Vision is a library of programming functions
mainly aimed at real-time computer vision.
It is used for image and video processing, object detection, face recognition, and more.
"""

import cv2

# Load an image
img = cv2.imread('./data/mike-benna-kX012NDcCKQ-unsplash.jpg')

### 1. Displaying an image in a window
cv2.imshow('Vancouver Sunset', img)

# Wait for a key press
cv2.waitKey(0)

# Destroy all winodws
cv2.destroyAllWindows()

### 2. Drawing Shapes on an Image
# Draw a line on the image
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

# Draw a rectangle on the image
cv2.rectangle(img, (50, 50), (200, 200), (0, 0, 255), 2)

# Draw a circle on the image
cv2.circle(img, (300, 300), 50, (255, 0, 0), -1)

# Display the image
cv2.imshow('Image', img)

# Wait for a key press
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()

### 3. Face Detection in Real-time Video
# Load the face cascade
face_cascade = cv2.CascadeClassifier('/home/jade/src/python-playground/pyModule/haarcascade_frontalface_default.xml')

# Start the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Video', frame)

    # Exit on ESC
    if cv2.waitKey(1) == 27:
        break

# Release the camera and destroy all windows
cap.release()
cv2.destroyAllWindows()
