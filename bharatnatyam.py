import streamlit as st
import cv2
import mediapipe as mp

def display_bharatnatyam_page():
    st.title("Bharatnatyam")
    
    # Display introductory video
    st.video("Dance warmup.mp4")  # Replace with your video file
    
    video_style = """
        <style>
        video {
            max-width: 50%; /* Set the maximum width as needed */
            height: auto;    /* Maintain aspect ratio */
        }
        </style>
    """
    st.markdown(video_style, unsafe_allow_html=True)
    
    # Display options
    st.header("Select Module")
    option = st.radio("Choose:", ["Module 1", "Module 2", "Module 3"])
    
    # Store the selected option in session state
    st.session_state.selected_option = option

    # Add a button to navigate to the selected option page
    if st.button("Start Learning"):
        st.session_state.show_option_page = True

    # Show content based on the selected option
    if hasattr(st.session_state, "show_option_page"):
        if st.session_state.selected_option == "Module 1":
            display_option1_page()
        elif st.session_state.selected_option == "Module 2":
            display_option2_page()
        elif st.session_state.selected_option == "Module 3":
            display_option3_page()

def display_option1_page():
    st.title("Module 1")
    st.write("Introduction")
    st.video("Namaskar.mp4")  # Replace with your video file

def display_option2_page():
    st.title("Module 2")
    st.write("Hasta Mudra")
    image_path = "mudra.jpg"  # Replace with the path to your image file
    st.write("Try yourself")
    st.image(image_path,width=250)
    
    # Set up the MediaPipe Hands model
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

    # Set up the camera
    cap = cv2.VideoCapture(0)  # 0 for the default camera, you can use other camera indexes if available

    # Hand sign labels
    hand_signs = {
        0: "mushti",
        1: "chandrakala",
        3: "Pataka",
    }

    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Convert the frame to RGB (MediaPipe requires RGB format)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame and obtain hand landmarks
        results = hands.process(rgb_frame)

        # Visualize the hand landmarks on the frame
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing = mp.solutions.drawing_utils
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Extract hand landmarks
                landmarks = hand_landmarks.landmark

                # Example: Classify hand sign based on landmark positions
                # Modify this part according to your specific hand sign recognition logic
                thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
                index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                middle_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                ring_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
                pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]

                # Calculate distances between finger tips and classify hand sign
                distances = [
                    (thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2,
                    (thumb_tip.x - middle_tip.x) ** 2 + (thumb_tip.y - middle_tip.y) ** 2,
                    (thumb_tip.x - ring_tip.x) ** 2 + (thumb_tip.y - ring_tip.y) ** 2,
                    (thumb_tip.x - pinky_tip.x) ** 2 + (thumb_tip.y - pinky_tip.y) ** 2
                ]
                min_distance_index = distances.index(min(distances))

                # Display the classified hand sign label
                hand_sign_label = hand_signs.get(min_distance_index, "Unknown")
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, f"Hand Sign: {hand_sign_label}", (10, 30), font, 0.7, (0, 255, 0), 2)

        # Display the captured frame
        cv2.imshow('Hand Sign Recognition', frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()
        

def display_option3_page():
    st.title("Module 3")
    st.write("Hand and Leg positions")
    image_path = "Aramandi.jpeg"
    st.image(image_path,width=250)
    image_path = "Murumandi.jpeg"
    st.image(image_path,width=250)
    image_path = "Hand pose.jpeg"
    st.image(image_path,width=250)
