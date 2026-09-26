import cv2
import time
import mediapipe as mp
from playsound import playsound
import threading

DOOMSCROLL_TIME = 20  # seconds
ALARM_SOUND = "alarm.mp3"

mp_face = mp.solutions.face_mesh
mp_pose = mp.solutions.pose

face_mesh = mp_face.FaceMesh(min_detection_confidence=0.5)
pose = mp_pose.Pose(min_detection_confidence=0.5)

cap = cv2.VideoCapture(0)

print("Camera permission requested...")
time.sleep(1)
print("Camera ON. Press Q to exit.")

doom_start = None
alarm_on = False

def alarm():
    global alarm_on
    alarm_on = True
    playsound(ALARM_SOUND)
    alarm_on = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face = face_mesh.process(rgb)
    pose_res = pose.process(rgb)

    face_down = False
    phone = False

    if face.multi_face_landmarks:
        for f in face.multi_face_landmarks:
            nose = f.landmark[1]
            chin = f.landmark[152]
            if chin.y - nose.y > 0.08:
                face_down = True

    if pose_res.pose_landmarks:
        lm = pose_res.pose_landmarks.landmark
        nose = lm[mp_pose.PoseLandmark.NOSE]
        lw = lm[mp_pose.PoseLandmark.LEFT_WRIST]
        rw = lm[mp_pose.PoseLandmark.RIGHT_WRIST]

        if lw.y > nose.y + 0.15 or rw.y > nose.y + 0.15:
            phone = True

    if face_down and phone:
        if doom_start is None:
            doom_start = time.time()
        elif time.time() - doom_start > DOOMSCROLL_TIME:
            cv2.putText(frame, "STOP DOOMSCROLLING!",
                        (40, 60), cv2.FONT_HERSHEY_SIMPLEX,
                        1.2, (0, 0, 255), 3)
            if not alarm_on:
                threading.Thread(target=alarm, daemon=True).start()
    else:
        doom_start = None

    cv2.imshow("Anti-Doomscroll System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
