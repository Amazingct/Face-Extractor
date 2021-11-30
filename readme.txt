------- Written by Daniel Ogunlolu --------

INFO:
Date: 30, NOV 2021
Programming Language: Python 3. 7
Main Script: extract-face.Python
Docker Base Image: python3.7

ALGORITHM:
1. Program starts by Downloading the given video from youtube link: https://www.youtube.com/watch?v=JriaiYZZhbY
2. Saves video inside working directory (main) with extension .mp4
3. Run HOG face detection on each frame while displaying video frame simultaneously using CV2, all detections are saved in faces directory
4. Finally, a Clustering process is performed on all faces to filter  unique faces
5. Unique faces are saved in unique_faces directory
6. While Video is playing, Press Q to exit

NOTE:
After building docker file run with the following commands: docker run -v /Users/<path>:/<container path>.
This will mount container directory to <path> on host system so images can easily be viewed if neccessary.

eg docker run -v /User/Desktop/extract-faces: /unique_faces


