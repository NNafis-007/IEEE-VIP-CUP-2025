# RGB Detection & Tracking Documentation

## Instructions on how to run the inference code

### Prerequisites:

- Set up the environment variables and paths in the notebook:
   - `weights_path`: Path to the YOLOv5 model weights (yolov5m_RGB.pt)
   - `images_path`: Path to test images directory
   - `videos_path`: Path to test videos directory
   - `project_path`: Working directory for outputs
   - `device`: GPU device configuration ("0" for single GPU, "0,1" for multi-GPU or "cpu")

### Running the inference:

- **Execute the complete pipeline** by running all cells in the Jupyter notebook `detection-and-tracking-submission.ipynb`

## Brief explanation of the approach

### Detection Approach:
- **Base Model**: YOLOv5m architecture fine-tuned for drone and bird detection
- **Custom Detection Script**: Modified YOLOv5 detect.py with enhanced features:
  - Temporal filtering using IoU-based matching across frames
  - Enclosing box removal to eliminate duplicate detections

### Tracking Approach:
- **Tracker**: ByteTrack algorithm via Supervision library
- **Features**:
  - Detection smoothing using DetectionsSmoother
  - Multi-object tracking with unique track IDs
  - Trajectory visualization with TraceAnnotator
  - FPS monitoring and performance optimization
  - Direction analysis (approaching/receding) based on bounding box area changes over time

### Post-processing:
- **Direction Classification**: Analyzes bounding box area trends across frames using linear regression
- **Performance Benchmarking**: Tests inference on both GPU and CPU to measure FPS
- **Output Format**: Combined CSV with detection results, tracking IDs, confidence scores, and performance metrics

## Hardware Specifications

### GPU Details:
- 2 Nvidia T4 GPUs (16GB x 2)

### CPU & RAM Details:
- Intel Xeon(R) @ 2.2Ghz with 32GB of RAM

## Model Details:
- **Architecture**: YOLOv5m
- **Classes**: Bird (class 0), Drone (class 1)
- **Model File**: yolov5m_RGB.pt
