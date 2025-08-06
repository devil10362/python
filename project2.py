import face_recognition
import cv2

# Load the known images (knows) and their names
image_of_person_a = face_recognition.load_image_file("person_a.jpg")
image_of_person_b = face_recognition.load_image_file("person_b.jpg")

known_faces = [
    face_recognition.face_encodings(image_of_person_a)[0],
    face_recognition.face_encodings(image_of_person_b)[0]
]

known_names = ["person_a", "person_b"]

# Initialize the video capture object
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the image from BGR to RGB
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face matches any of the known faces
        matches = face_recognition.compare_faces(known_faces, face_encoding)

        # If it matches, then assign the name of the person
        name = "Unknown"
        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]

        # Draw a rectangle around the face and display the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the open window
video_capture.release()
cv2.destroyAllWindows()