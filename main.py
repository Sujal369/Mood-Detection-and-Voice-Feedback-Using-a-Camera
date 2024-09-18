import cv2
import pyttsx3
from deepface import DeepFace

# Initialize the text-to-speech engine
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to detect mood and speak it
def detect_mood_and_speak(frame):
    try:
        # Use DeepFace to analyze the emotion
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        # Check if result is a list (multiple faces detected)
        if isinstance(result, list):
            result = result[0]  # Take the first result

        dominant_emotion = result['dominant_emotion']

        # Print and speak the dominant emotion
        print(f"You are feeling {dominant_emotion}.")
        speak(f"You are feeling {dominant_emotion}.")
    except Exception as e:
        print(f"Error: {str(e)}")


# Open the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    speak("Error: Could not open the camera.")
else:
    print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Show the video feed
    cv2.imshow('Mood Detector', frame)

    # Detect mood in the current frame
    detect_mood_and_speak(frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
