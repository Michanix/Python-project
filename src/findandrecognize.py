import face_recognition
import cv2
import numpy as np

# source: 
# https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py

'''The code from source link was modified for my needs.
    If you want to see how works the original code, check the source link.'''


def find_and_recognize(path='images/face.jpg'):
    video_capture = cv2.VideoCapture(0)

    user_face = face_recognition.load_image_file(path)
    user_face_encoding = face_recognition.face_encodings(
        user_face, num_jitters=30)[0]

    known_faces_encodings = [
        user_face_encoding
    ]

    face_encodings = []
    process_this_frame = True
    state = False  # state of the match. If True match is found

    while state != True:

        _, frame = video_capture.read()

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(
                rgb_small_frame, number_of_times_to_upsample=2, model="cnn")
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)

            for face_encoding in face_encodings:

                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(
                    known_faces_encodings, face_encoding, tolerance=0.6)

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(
                    known_faces_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    state = True
                else:
                    state = False

            break
        process_this_frame = not process_this_frame

    # Release handle to the webcam

    video_capture.release()

    return state


if __name__ == '__main__':
    find_and_recognize()
