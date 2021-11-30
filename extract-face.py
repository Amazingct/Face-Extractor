# -----------------------------------DOWNLOAD VIDEO------------------------------------------------- #

from pytube import YouTube
import os

def downloadYouTube(videourl, path):
    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

print("\n \nContainer Started")
print(" >>> Downloading Video from youtube link: https://www.youtube.com/watch?v=JriaiYZZhbY")
downloadYouTube('https://www.youtube.com/watch?v=JriaiYZZhbY','.')
print(" >>> Download done ")

for file in os.listdir():
    if file.endswith("mp4"):
        video = file

print(" >>> Video name: {}".format(video))


# -----------------------------------FACE DETECTION------------------------------------------------- #

import cv2
import dlib
from imutils import face_utils

frame_skip = 4
face_detect = dlib.get_frontal_face_detector()
frame_no = 0
video_capture = cv2.VideoCapture(video)

def detect_face(frame):
    frame_original = frame
    global frame_no

    if frame_no%frame_skip == 0:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #Detect
        rects = face_detect(gray, 1)

        detect = 1
        for (i, rect) in enumerate(rects):
            detect = 2
            (x, y, w, h) = face_utils.rect_to_bb(rect)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # save face
            cv2.imwrite("faces/frame-{}-face-{}.jpg".format(str(frame_no), str(i)),frame_original[y:y+h, x:x+w])


    #return frame with detection
    return frame, detect

print(" >>> Using HOG to detect Faces in all frames (this will take a while)..........")

while True:
    # Capture frame
    ret, frame = video_capture.read()
    

    if ret == 0:
        break

    # Display the frame with detection
    try:
        show, detect= detect_face(frame)
        cv2.imshow('Video', show)
    except Exception as e:
        #print(" >>> can not display video due to this error: {}".format(e))
        pass
    frame_no = frame_no + 1

    # Quit video by typing Q
    if cv2.waitKey(detect) & 0xFF == ord('q'):
        break

print(" >>> Reach end of Video or Can't receive frame")
print(" >>> Done, existing video window  and saving detected face")

video_capture.release()
cv2.destroyAllWindows()

print(" >>> Detected faces saved to faces Directory.")



# -----------------------------------FACE CLUSTTERING------------------------------------------------- #
def cluster():
    no = 10
    return no

face_no = cluster()

print(" >>> Performing Face Clustering to detect unique faces in faces saved in faces directory")
print(" >>> Done, Total number of unique face is {}".format(face_no))
print(" >>> Unique Faces saved to Unique-face directory")
print(" >>> Prigram Ended... exiting ...")