# Mood-Detection-and-Voice-Feedback-Using-a-Camera
This project detects the user's mood in real-time using a camera, processes the user's facial expression to identify the emotion, and then speaks out loud the detected mood. The system leverages Python libraries like OpenCV for capturing video, DeepFace for facial emotion recognition, and pyttsx3 for converting text to speech. 
Features:
Real-time facial emotion detection via a camera.
Verbal feedback with a natural voice.
Supports multiple emotions (happy, sad, angry, surprised, etc.).
Simple and user-friendly interface with a live video feed.
Exits smoothly on pressing 'q'.
Technologies Used:
Python
OpenCV: For capturing the video from the webcam.
DeepFace: For detecting emotions from the user's face.
pyttsx3: For converting the detected emotion into speech.
Prerequisites:
Ensure the following libraries are installed:

bash
Copy code
pip install opencv-python
pip install pyttsx3
pip install deepface
Additionally, make sure you have a working camera connected to your system.

How to Run:
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/mood-detection-voice-feedback.git
Navigate to the project folder:

bash
Copy code
cd mood-detection-voice-feedback
Run the Python script:

bash
Copy code
python mood_detector.py
To quit the program, press the 'q' key.

Project Structure:
bash
Copy code
├── mood_detector.py  # Main Python script
├── README.md         # Project documentation
└── requirements.txt  # List of dependencies

Usage:
Run the script and allow camera access.
The camera will capture your face and analyze your facial expressions.
The dominant emotion (mood) will be detected and spoken aloud.
Press 'q' to exit.
Dependencies:
Python 3.x
OpenCV
pyttsx3
DeepFace
Troubleshooting:
Camera not working: Ensure that the camera is properly connected and accessible. You can try running a simple OpenCV script to check the camera.

python
Copy code
import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if ret:
    print("Camera is working")
cap.release()
DeepFace error: If DeepFace doesn't detect the face or returns an error, make sure you have a clear image of the face in the camera's frame and the model is working properly.

License:
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing:
Contributions are welcome! Please feel free to submit a Pull Request if you have any suggestions or improvements.

Author:
Sujal Lothe
