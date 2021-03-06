from imageai.Detection import VideoObjectDetection
import os
from cv2 import cv2

execution_path = os.getcwd()


camera = cv2.VideoCapture(0)

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(
    execution_path, "models/yolo.h5"))
detector.loadModel()


video_path = detector.detectObjectsFromVideo(
    camera_input=camera,
    output_file_path=os.path.join(execution_path, "camera_detected_video"),
    frames_per_second=10, log_progress=True, minimum_percentage_probability=40)

# print(video_path)
