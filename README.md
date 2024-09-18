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
