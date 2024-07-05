Face Recognition Algorithm
This project implements a face recognition algorithm using YOLOv8 for face detection and OpenCV for video processing. The code reads a video file, detects faces in each frame using the YOLO model, and displays the video with bounding boxes around detected faces.

Table of Contents




Installation



Usage




Requirements





Contributing






Installation




Clone the repository:


Copy code
git clone https://github.com/your-username/face-recognition-algo.git
cd face-recognition-algo
Install dependencies:
Make sure you have Python installed. Then, install the required Python packages:


Copy code
pip install -r requirements.txt
Download the YOLOv8 face detection model:
Place the yolov8n-face.pt file in the project directory. You can download the model from the YOLOv8 repository.



Usage
Place your video file in the project directory and rename it to test.mp4, or modify the video_path variable in the script to point to your video file.

Run the script:


Copy code


python face_recognition.py



Control the script:

The video will be displayed with bounding boxes around detected faces.
Press q to exit the video display.
Requirements
Python 3.x
OpenCV
cvzone
ultralytics
You can install the dependencies using the following command:
Copy code
pip install opencv-python cvzone ultralytics




Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any changes or improvements.

Fork the Project



Create your Feature Branch (git checkout -b feature/AmazingFeature)



Commit your Changes (git commit -m 'Add some AmazingFeature')




Push to the Branch (git push origin feature/AmazingFeature)



Open a Pull Request



Author

Manpreet kour
