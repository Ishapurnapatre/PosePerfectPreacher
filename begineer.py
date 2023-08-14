import streamlit as st
import cv2
import math
import mediapipe as mp

def display_begineer_page():
    st.title("Beginner Level Yoga with Live Camera")

    # Display options
    st.header("Select an Option")
    option = st.radio("Choose:", ["Vrukshasana", "Cat pose", "Child pose", "Ushtrasana", "Phalakasana"])
    
    # Store the selected difficulty level in session state
    st.session_state.selected_option = option
    
    # Add a button to navigate to the selected difficulty page
    if st.button("Start", key="1"):
        st.session_state.show_option_page = True
    
    # Show content based on the selected difficulty
    if hasattr(st.session_state, "show_option_page") and st.session_state.show_option_page:
        if st.session_state.selected_option == "Vrukshasana":
            display_option1()
        elif st.session_state.selected_option == "Cat pose":
            display_option2()
        elif st.session_state.selected_option == "Child pose":
            display_option3()
        elif st.session_state.selected_option == "Ushtrasana":
            display_option4()
        elif st.session_state.selected_option == "Phalakasana":
            display_option5()



def display_option1():
    
    # Initialize MediaPipe Pose model
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

    # Set up the camera
    cap = cv2.VideoCapture(0) 
      
    # Create a resizable window
    cv2.namedWindow('Resizable Webcam Feed', cv2.WINDOW_NORMAL)

    # Function to calculate angle between three points
    def calculate_angle(a, b, c):
        angle = math.degrees(math.atan2(c.y - b.y, c.x - b.x) - math.atan2(a.y - b.y, a.x - b.x))
        angle = angle % 360  # Ensure the angle is within [0, 360] degrees
        return angle
    
    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Convert the frame to RGB (MediaPipe requires RGB format)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame and obtain the pose landmarks
        results_pose = pose.process(rgb_frame)

        # Visualize the pose landmarks on the frame
        if results_pose.pose_landmarks:
            mp_drawing = mp.solutions.drawing_utils
            mp_drawing.draw_landmarks(frame, results_pose.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Extract landmarks for right arm
            right_shoulder = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
            right_elbow = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW]
            right_wrist = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]            
            right_hip = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]
            right_knee = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE]
            right_ankle = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]
            # Extract landmarks for left arm
            left_shoulder = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
            left_elbow = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW]
            left_wrist = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
            left_hip = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
            left_knee = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE]
            left_ankle = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE]
            
            angle_right_hand = calculate_angle(right_shoulder, right_elbow, right_wrist)
            angle_left_hand = calculate_angle(left_shoulder, left_elbow, left_wrist)
            angle_right_leg = calculate_angle(right_hip, right_knee, right_ankle)
            angle_left_leg = calculate_angle(left_hip, left_knee, left_ankle)        
            
            # Display the calculated angles on the frame
            font = cv2.FONT_HERSHEY_SIMPLEX
            if 190 <= angle_right_hand <= 210:
                cv2.putText(frame, "Right Arm: Perfect", (10, 30), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Right Arm: Improvement Needed", (10, 30), font, 0.5, (0, 0, 255), 1)

            if 150 <= angle_left_hand <= 170:
                cv2.putText(frame, "Left Arm: Perfect", (380, 30), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Left Arm: Improvement Needed", (380, 30), font, 0.5, (0, 0, 255), 1)
                
            if 350 <= angle_right_leg <= 290:
                cv2.putText(frame, "Right Leg: Perfect", (10, 450), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Right Leg: Improvement Needed", (10, 450), font, 0.5, (0, 0, 255), 1)

            if 170 <= angle_left_leg <= 180:
                cv2.putText(frame, "Left Leg: Perfect", (380, 450), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Left Leg: Improvement Needed", (380, 450), font, 0.5, (0, 0, 255), 1)

        # Display the captured frame
        cv2.imshow('Pose and Hand Landmarks', frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()
    
    
def display_option2():    
    # Initialize MediaPipe Pose model
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

    # Set up the camera
    cap = cv2.VideoCapture(0) 
      
    # Create a resizable window
    cv2.namedWindow('Resizable Webcam Feed', cv2.WINDOW_NORMAL)

    # Function to calculate angle between three points
    def calculate_angle(a, b, c):
        angle = math.degrees(math.atan2(c.y - b.y, c.x - b.x) - math.atan2(a.y - b.y, a.x - b.x))
        angle = angle % 360  # Ensure the angle is within [0, 360] degrees
        return angle
    
    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Convert the frame to RGB (MediaPipe requires RGB format)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame and obtain the pose landmarks
        results_pose = pose.process(rgb_frame)

        # Visualize the pose landmarks on the frame
        if results_pose.pose_landmarks:
            mp_drawing = mp.solutions.drawing_utils
            mp_drawing.draw_landmarks(frame, results_pose.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Extract landmarks for right arm
            right_shoulder = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
            right_elbow = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW]
            right_wrist = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]
            right_pinky = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_PINKY]
            right_index = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX]
            right_thumb = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_THUMB]
            right_hip = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]
            right_knee = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE]
            right_ankle = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]
            right_heel = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HEEL]
            right_foot_index = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX]
            
            # Extract landmarks for left arm
            left_shoulder = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
            left_elbow = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW]
            left_wrist = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
            left_pinky = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_PINKY]
            left_index= results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_INDEX]
            left_thumb = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_THUMB]
            left_hip = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
            left_knee = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE]
            left_ankle = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE]
            left_heel = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HEEL]
            left_foot_index = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX]
            
            angle_right_hand = calculate_angle(right_shoulder, right_elbow, right_wrist)
            angle_left_hand = calculate_angle(left_shoulder, left_elbow, left_wrist)
            angle_right_leg = calculate_angle(right_hip, right_knee, right_ankle)
            angle_left_leg = calculate_angle(left_hip, left_knee, left_ankle)        
            
            # Display the calculated angles on the frame
            font = cv2.FONT_HERSHEY_SIMPLEX
            if 190 <= angle_right_hand <= 210:
                cv2.putText(frame, "Right Arm: Perfect", (10, 30), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Right Arm: Improvement Needed", (10, 30), font, 0.5, (0, 0, 255), 1)

            if 150 <= angle_left_hand <= 170:
                cv2.putText(frame, "Left Arm: Perfect", (380, 30), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Left Arm: Improvement Needed", (380, 30), font, 0.5, (0, 0, 255), 1)
                
            if 360 <= angle_right_leg <= 310:
                cv2.putText(frame, "Right Leg: Perfect", (10, 450), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Right Leg: Improvement Needed", (10, 450), font, 0.5, (0, 0, 255), 1)

            if 170 <= angle_left_leg <= 180:
                cv2.putText(frame, "Left Leg: Perfect", (380, 450), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Left Leg: Improvement Needed", (380, 450), font, 0.5, (0, 0, 255), 1)

        # Display the captured frame
        cv2.imshow('Pose and Hand Landmarks', frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()
    
    
def display_option3():
    
    # Initialize MediaPipe Pose model
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

    # Set up the camera
    cap = cv2.VideoCapture(0) 
      
    # Create a resizable window
    cv2.namedWindow('Resizable Webcam Feed', cv2.WINDOW_NORMAL)

    # Function to calculate angle between three points
    def calculate_angle(a, b, c):
        angle = math.degrees(math.atan2(c.y - b.y, c.x - b.x) - math.atan2(a.y - b.y, a.x - b.x))
        angle = angle % 360  # Ensure the angle is within [0, 360] degrees
        return angle
    
    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Convert the frame to RGB (MediaPipe requires RGB format)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame and obtain the pose landmarks
        results_pose = pose.process(rgb_frame)

        # Visualize the pose landmarks on the frame
        if results_pose.pose_landmarks:
            mp_drawing = mp.solutions.drawing_utils
            mp_drawing.draw_landmarks(frame, results_pose.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Extract landmarks for right arm
            right_shoulder = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
            right_elbow = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW]
            right_wrist = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]
            right_pinky = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_PINKY]
            right_index = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX]
            right_thumb = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_THUMB]
            right_hip = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]
            right_knee = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE]
            right_ankle = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]
            right_heel = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HEEL]
            right_foot_index = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX]
            
            # Extract landmarks for left arm
            left_shoulder = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
            left_elbow = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW]
            left_wrist = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
            left_pinky = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_PINKY]
            left_index= results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_INDEX]
            left_thumb = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_THUMB]
            left_hip = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
            left_knee = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE]
            left_ankle = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE]
            left_heel = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HEEL]
            left_foot_index = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX]
            
            angle_right_hand = calculate_angle(right_shoulder, right_elbow, right_wrist)
            angle_left_hand = calculate_angle(left_shoulder, left_elbow, left_wrist)
            angle_right_leg = calculate_angle(right_hip, right_knee, right_ankle)
            angle_left_leg = calculate_angle(left_hip, left_knee, left_ankle)        
            
            # Display the calculated angles on the frame
            font = cv2.FONT_HERSHEY_SIMPLEX
            if 190 <= angle_right_hand <= 210:
                cv2.putText(frame, "Right Arm: Perfect", (10, 30), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Right Arm: Improvement Needed", (10, 30), font, 0.5, (0, 0, 255), 1)

            if 150 <= angle_left_hand <= 170:
                cv2.putText(frame, "Left Arm: Perfect", (380, 30), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Left Arm: Improvement Needed", (380, 30), font, 0.5, (0, 0, 255), 1)
                
            if 360 <= angle_right_leg <= 310:
                cv2.putText(frame, "Right Leg: Perfect", (10, 450), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Right Leg: Improvement Needed", (10, 450), font, 0.5, (0, 0, 255), 1)

            if 170 <= angle_left_leg <= 180:
                cv2.putText(frame, "Left Leg: Perfect", (380, 450), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Left Leg: Improvement Needed", (380, 450), font, 0.5, (0, 0, 255), 1)

        # Display the captured frame
        cv2.imshow('Pose and Hand Landmarks', frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()
    
    
def display_option4():
    
    # Initialize MediaPipe Pose model
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

    # Set up the camera
    cap = cv2.VideoCapture(0) 
      
    # Create a resizable window
    cv2.namedWindow('Resizable Webcam Feed', cv2.WINDOW_NORMAL)

    # Function to calculate angle between three points
    def calculate_angle(a, b, c):
        angle = math.degrees(math.atan2(c.y - b.y, c.x - b.x) - math.atan2(a.y - b.y, a.x - b.x))
        angle = angle % 360  # Ensure the angle is within [0, 360] degrees
        return angle
    
    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Convert the frame to RGB (MediaPipe requires RGB format)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame and obtain the pose landmarks
        results_pose = pose.process(rgb_frame)

        # Visualize the pose landmarks on the frame
        if results_pose.pose_landmarks:
            mp_drawing = mp.solutions.drawing_utils
            mp_drawing.draw_landmarks(frame, results_pose.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Extract landmarks for right arm
            right_shoulder = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
            right_elbow = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW]
            right_wrist = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]
            right_hip = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]
            right_knee = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE]
            right_ankle = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]
            
            # Extract landmarks for left arm
            left_shoulder = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
            left_elbow = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW]
            left_wrist = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
            left_hip = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
            left_knee = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE]
            left_ankle = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE]
            
            angle_right_hand = calculate_angle(right_shoulder, right_elbow, right_wrist)
            angle_left_hand = calculate_angle(left_shoulder, left_elbow, left_wrist)
            angle_right_leg = calculate_angle(right_hip, right_knee, right_ankle)
            angle_left_leg = calculate_angle(left_hip, left_knee, left_ankle)        
            
            # Display the calculated angles on the frame
            font = cv2.FONT_HERSHEY_SIMPLEX
            if 160 <= angle_right_hand <= 180:
                cv2.putText(frame, "Right Arm: Perfect", (10, 30), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Right Arm: Improvement Needed", (10, 30), font, 0.5, (0, 0, 255), 1)

            if 180 <= angle_left_hand <= 200:
                cv2.putText(frame, "Left Arm: Perfect", (380, 30), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Left Arm: Improvement Needed", (380, 30), font, 0.5, (0, 0, 255), 1)
                
            if 80 <= angle_right_leg <= 110:
                cv2.putText(frame, "Right Leg: Perfect", (10, 450), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Right Leg: Improvement Needed", (10, 450), font, 0.5, (0, 0, 255), 1)

            if 280 <= angle_left_leg <= 250:
                cv2.putText(frame, "Left Leg: Perfect", (380, 450), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Left Leg: Improvement Needed", (380, 450), font, 0.5, (0, 0, 255), 1)

        # Display the captured frame
        cv2.imshow('Pose and Hand Landmarks', frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()
    
    
def display_option5():
    
    # Initialize MediaPipe Pose model
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

    # Set up the camera
    cap = cv2.VideoCapture(0) 
      
    # Create a resizable window
    cv2.namedWindow('Resizable Webcam Feed', cv2.WINDOW_NORMAL)

    # Function to calculate angle between three points
    def calculate_angle(a, b, c):
        angle = math.degrees(math.atan2(c.y - b.y, c.x - b.x) - math.atan2(a.y - b.y, a.x - b.x))
        angle = angle % 360  # Ensure the angle is within [0, 360] degrees
        return angle
    
    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Convert the frame to RGB (MediaPipe requires RGB format)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame and obtain the pose landmarks
        results_pose = pose.process(rgb_frame)

        # Visualize the pose landmarks on the frame
        if results_pose.pose_landmarks:
            mp_drawing = mp.solutions.drawing_utils
            mp_drawing.draw_landmarks(frame, results_pose.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Extract landmarks for right arm
            right_shoulder = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
            right_elbow = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW]
            right_wrist = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]
            right_pinky = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_PINKY]
            right_index = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX]
            right_thumb = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_THUMB]
            right_hip = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]
            right_knee = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE]
            right_ankle = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]
            right_heel = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HEEL]
            right_foot_index = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX]
            
            # Extract landmarks for left arm
            left_shoulder = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
            left_elbow = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW]
            left_wrist = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
            left_pinky = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_PINKY]
            left_index= results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_INDEX]
            left_thumb = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_THUMB]
            left_hip = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
            left_knee = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE]
            left_ankle = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE]
            left_heel = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HEEL]
            left_foot_index = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX]
            
            angle_right_hand = calculate_angle(right_shoulder, right_elbow, right_wrist)
            angle_left_hand = calculate_angle(left_shoulder, left_elbow, left_wrist)
            angle_right_leg = calculate_angle(right_hip, right_knee, right_ankle)
            angle_left_leg = calculate_angle(left_hip, left_knee, left_ankle)        
            
            # Display the calculated angles on the frame
            font = cv2.FONT_HERSHEY_SIMPLEX
            if 190 <= angle_right_hand <= 210:
                cv2.putText(frame, "Right Arm: Perfect", (10, 30), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Right Arm: Improvement Needed", (10, 30), font, 0.5, (0, 0, 255), 1)

            if 150 <= angle_left_hand <= 170:
                cv2.putText(frame, "Left Arm: Perfect", (380, 30), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Left Arm: Improvement Needed", (380, 30), font, 0.5, (0, 0, 255), 1)
                
            if 360 <= angle_right_leg <= 310:
                cv2.putText(frame, "Right Leg: Perfect", (10, 450), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Right Leg: Improvement Needed", (10, 450), font, 0.5, (0, 0, 255), 1)

            if 170 <= angle_left_leg <= 180:
                cv2.putText(frame, "Left Leg: Perfect", (380, 450), font, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "Left Leg: Improvement Needed", (380, 450), font, 0.5, (0, 0, 255), 1)

        # Display the captured frame
        cv2.imshow('Pose and Hand Landmarks', frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()