# XYCams - Anomaly Detection in Camera Footage

A hackathon project implementing real-time anomaly detection and object detection in camera footage using YOLOv5 deep learning model.

## Overview

XYCams is a security surveillance system that leverages YOLOv5 (You Only Look Once v5) for real-time object detection in camera feeds. The system features a login-based authentication system and provides live anomaly detection capabilities for monitoring purposes.

## Features

- **Real-time Object Detection**: Uses YOLOv5 custom model for detecting objects in camera footage
- **Live Video Stream Processing**: Processes video frames from camera/webcam in real-time
- **User Authentication**: Secure login system with MySQL database integration
- **Confidence Scoring**: Displays confidence scores for each detected object
- **FPS Monitoring**: Real-time FPS (frames per second) display for performance tracking
- **GPU Acceleration**: Automatic GPU support detection (CUDA) for faster inference

## Project Structure

```
CyberX/
├── gadhahumai.py                    # Main detection engine (YOLOv5 implementation)
├── login.py                          # GUI login interface
├── login_system.py                   # Database authentication logic
├── bestv5p1.pt                       # Pre-trained YOLOv5 model weights
├── login.spec                        # PyInstaller configuration
├── security-concept-illustration_114360-1528.avif  # UI asset
└── README.md                         # This file
```

## Requirements

- Python 3.7+
- PyTorch
- OpenCV (cv2)
- MySQL Connector
- Tkinter (usually comes with Python)
- YOLOv5

## Installation

1. **Clone/Download the project**
   ```bash
   cd CyberX
   ```

2. **Install required dependencies**
   ```bash
   pip install torch torchvision torchaudio
   pip install opencv-python
   pip install mysql-connector-python
   pip install yolov5
   ```

3. **Set up MySQL Database**
   - Create a database named `xycams`
   - Create a `security` table with columns:
     - `id` (INT, Primary Key)
     - `username` (VARCHAR)
     - `password` (VARCHAR)
   - Update credentials in `login.py` and `login_system.py` if needed

4. **Place the model**
   - Ensure `bestv5p1.pt` (YOLOv5 model weights) is in the project directory

## Usage

1. **Run the Login Interface**
   ```bash
   python login.py
   ```

2. **Authenticate**
   - Enter valid credentials from the MySQL database
   - Upon successful login, the camera feed will activate

3. **View Detection Results**
   - The application opens a window showing:
     - Real-time camera feed
     - Bounding boxes around detected objects
     - Class labels and confidence scores
     - FPS counter

4. **Exit**
   - Press `ESC` key to exit the detection window

## Core Components

### `gadhahumai.py` - MugDetection Class

The main detection engine that handles:
- **Model Loading**: Loads YOLOv5 custom model from PyTorch Hub
- **Frame Processing**: Captures and processes video frames
- **Inference**: Runs object detection on each frame
- **Visualization**: Draws bounding boxes with labels and confidence scores

**Key Methods:**
- `load_model()`: Loads YOLOv5 model
- `get_video_capture()`: Initializes video capture device
- `score_frame()`: Performs inference on a frame
- `plot_boxes()`: Visualizes detection results
- `run()`: Main loop for continuous detection

### `login.py` - User Interface

Tkinter-based GUI for:
- User authentication
- Launching the detection system after login
- Database verification

### `login_system.py` - Database Integration

Handles:
- MySQL database connection
- Credential verification
- User authentication logic

## Configuration

### Model Confidence Threshold
Edit the confidence threshold in `gadhahumai.py` (line ~81):
```python
if scores[i] >= 0.5:  # Adjust this value (0.0-1.0)
```

### Camera Index
Change the camera source in `login.py`:
```python
detector = gd.MugDetection(capture_index=0, model_name='bestv5p1.pt')
# 0 = default camera, 1 = secondary camera, etc.
```

### Frame Resolution
Modify frame size in `gadhahumai.py`:
```python
frame = cv2.resize(frame, (416, 416))  # Change dimensions as needed
```

## Database Setup Example

```sql
CREATE DATABASE xycams;

USE xycams;

CREATE TABLE security (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(100),
  password VARCHAR(100)
);

INSERT INTO security (username, password) VALUES ('admin', 'Pass693');
```

## Hardware Requirements

- **Minimum**: CPU-based inference (slower)
- **Recommended**: NVIDIA GPU with CUDA support (faster)
- **RAM**: 4GB minimum, 8GB recommended
- **Webcam**: Standard USB/built-in camera

## Performance Tips

1. Use GPU for faster inference (CUDA-enabled device)
2. Adjust frame resolution based on your hardware
3. Increase confidence threshold to reduce false positives
4. Monitor FPS counter for bottlenecks

## Limitations

- Current implementation detects objects trained in the custom YOLOv5 model
- Real-time processing depends on hardware capabilities
- Database credentials are hardcoded (not production-ready)

## Troubleshooting

**Issue**: "Cannot connect to database"
- Verify MySQL is running
- Check database credentials in code
- Ensure `xycams` database exists

**Issue**: No camera detected
- Check camera is connected and accessible
- Verify camera permissions
- Try changing `capture_index` value

**Issue**: Low FPS/Slow processing
- Check GPU availability
- Reduce frame resolution
- Lower model complexity
- Close other applications

## Team

This project was created during a hackathon focused on AI-powered security systems and anomaly detection.

## Acknowledgments

- Built with [YOLOv5](https://github.com/ultralytics/yolov5) by Ultralytics
- Uses PyTorch for deep learning
- MySQL for database management
