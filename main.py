# filepath: robocar/src/main.py
import cv2
import numpy as np
from lib import direction, camera

def main():
    # Initialize the camera
    cap = cv2.VideoCapture(0)  # Change the index if necessary

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break

        # Process the image to find the error
        error = camera(frame)

        # Calculate motor speeds based on the error
        dutya, dutyb = direction(error)

        # Here you would add code to control the motors using dutya and dutyb
        # For example:
        # set_motor_speeds(dutya, dutyb)

        # Display the processed frame
        cv2.imshow("Robocar", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()