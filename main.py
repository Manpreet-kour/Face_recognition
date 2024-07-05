import cv2
import cvzone
from ultralytics import YOLO
import time

# Path to the video file
video_path = 'test.mp4'
cap = cv2.VideoCapture(video_path)

# Get the original frame rate of the video
fps = cap.get(cv2.CAP_PROP_FPS)
frame_duration = 1 / fps

# Load YOLO face detection model
facemodel = YOLO('yolov8n-face.pt')

while cap.isOpened():
    start_time = time.time()

    rt, video = cap.read()
    if not rt:
        break  # Break the loop if there are no more frames

    # Resize the video frame
    video = cv2.resize(video, (640, 360))

    # Perform face detection
    faceresult = facemodel.predict(video, conf=0.40)
    for info in faceresult:
        parameters = info.boxes
        for box in parameters:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            h, w = y2 - y1, x2 - x1
            cvzone.cornerRect(video, [x1, y1, w, h], l=9, rt=3)

    # Display the frame
    cv2.imshow('frame', video)

    # Calculate the time taken to process the frame
    elapsed_time = time.time() - start_time
    # Calculate the time to wait to match the original frame rate
    wait_time = max(1, int((frame_duration - elapsed_time) * 1000))

    if cv2.waitKey(wait_time) & 0xFF == ord('q'):
        break  # Exit the loop when 'q' is pressed

cap.release()
cv2.destroyAllWindows()

