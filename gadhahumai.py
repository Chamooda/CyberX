import torch
import numpy as np
import cv2
from time import time


class MugDetection:
    """
    Class implements YOLOv5 model to make inferences on a YouTube video using OpenCV2.
    """

    def __init__(self, capture_index, model_name):
        """
        Initializes the class with YouTube URL and output file.
        :param capture_index: The index of the video capture device (e.g., 0 for the default camera).
        :param model_name: The name or path of the YOLOv5 model to be used.
        """
        self.capture_index = capture_index
        self.model = self.load_model(model_name)
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("Using Device:", self.device)

    def get_video_capture(self):
        """
        Creates a new video streaming object to extract video frame by frame for prediction.
        :return: OpenCV2 video capture object with the lowest quality frame available.
        """
        return cv2.VideoCapture(self.capture_index)

    def load_model(self, model_name):
        """
        Loads the YOLOv5 model from PyTorch Hub.
        :param model_name: The name or path of the YOLOv5 model.
        :return: The loaded PyTorch model.
        """
        if model_name:
            model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_name, force_reload=True)
        else:
            model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        return model

    def score_frame(self, frame):
        """
        Takes a single frame as input and scores the frame using the YOLOv5 model.
        :param frame: The input frame in numpy/list/tuple format.
        :return: The labels, coordinates, and confidence scores of objects detected by the model in the frame.
        """
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
        labels, cord, scores = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1], results.xyxyn[0][:, 4]
        return labels, cord, scores

    def class_to_label(self, x):
        """
        Converts a numeric label to the corresponding string label.
        :param x: The numeric label.
        :return: The corresponding string label.
        """
        return self.classes[int(x)]

    def plot_boxes(self, results, frame):
        """
        Takes a frame and its results as input and plots the bounding boxes, labels, and confidence scores onto the frame.
        :param results: The labels, coordinates, and confidence scores predicted by the model on the given frame.
        :param frame: The frame which has been scored.
        :return: The frame with bounding boxes, labels, and confidence scores plotted on it.
        """
        labels, cord, scores = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if scores[i] >= 0.5:  # Draw bounding box only if confidence score is >= 0.75
                x1, y1, x2, y2 = int(row[0] * x_shape), int(row[1] * y_shape), int(row[2] * x_shape), int(row[3] * y_shape)
                bgr = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                label = self.class_to_label(labels[i])
                score = scores[i]
                text = f"{label}: {score:.2f}"
                cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)

        return frame

    def run(self):
        """
        This function is called when the class is executed. It runs the loop to read the video frame by frame
        and displays the output with bounding boxes, labels, and confidence scores.
        :return: None
        """
        cap = self.get_video_capture()
        assert cap.isOpened()

        while True:
            ret, frame = cap.read()
            assert ret

            frame = cv2.resize(frame, (416, 416))

            start_time = time()
            results = self.score_frame(frame)
            frame = self.plot_boxes(results, frame)

            end_time = time()
            fps = 1 / np.round(end_time - start_time, 2)
            cv2.putText(frame, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

            cv2.imshow('YOLOv5 Detection', frame)

            if cv2.waitKey(5) & 0xFF == 27:
                cv2.destroyAllWindows()
                break

        cap.release()


# Create a new object and run the detection.
#detector = MugDetection(capture_index=0, model_name='bestv5p1.pt')
#detector.run()

