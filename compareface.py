import pandas as pd
import numpy as np
import cv2
import face_recognition
import mark_Attendance as mk

class CompareFace:

    def __init__(self):
        # Adding path instead of writing the below code for future update
        self.student_cvs_data = pd.read_csv(r'Student_data.csv', index_col=0)
        self.student_details = self.student_cvs_data.index.values.tolist()
        self.known_encode_data_list = np.array(self.student_cvs_data.values.tolist())

    def compare_face(self):
        video_capture_device_no = 0
        cap = cv2.VideoCapture(video_capture_device_no)

        try:
            while True:
                success, img = cap.read()
                img_second = cv2.resize(img, (0, 0), None, 0.25, 0.25)

                face_current_frame = face_recognition.face_locations(img_second)
                encode_current_frame = face_recognition.face_encodings(img_second)

                for encode_face, face_loc in zip(encode_current_frame, face_current_frame):
                    match = face_recognition.compare_faces(self.known_encode_data_list, encode_face)
                    face_distance = face_recognition.face_distance(self.known_encode_data_list, encode_face)
                    match_index = np.argmin(face_distance)
                    if match[match_index]:
                        name = self.student_details[match_index].upper()
                        mk.mark_attendance(name)
                        y1, x2, y2, x1 = face_loc
                        y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                    else:
                        name = "Unknown Person"
                        print(name)
                        y1, x2, y2, x1 = face_loc
                        y1, x2, y2, x1 = y1 * 2, x2 * 2, y2 * 2, x1 * 2
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv2.imshow("Recognition", img)
                # cv2.waitKey(1)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    cv2.destroyWindow('Recognition')
                    break
        except KeyboardInterrupt as e:
            print("User interrupted")
        else:
            return None
        finally:
            cap.release()