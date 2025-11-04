# RGB Payload Identification Documentation

## Instructions on how to run the inference code

### Prerequisites:

- Set up the environment variables and paths in the notebook:
   - `model_path`: Path to the trained YOLOv12m model weights (yolov12trainingpayloadRGB.pt)
   - `image_dir`: Path to test images directory containing payload images

### Running the inference:

- **Direct execution**: Run all cells in the Jupyter notebook `yolov12inference-payloadsubmission.ipynb`

## Brief explanation of the approach

### Model Architecture:
- **Base Model**: YOLOv12m (Ultralytics implementation)
- **Task**: Binary classification for payload identification
- **Classes**: 
  - Class 0: "Harmful" payload
  - Class 1: "Normal" payload

### Inference Pipeline:
1. **Model Loading**: Loads pre-trained YOLOv12m weights from the specified path
2. **Batch Processing**: Processes images in batches of 16 for efficiency
3. **Image Resolution**: Fixed input size of 640x640 pixels
4. **Device Utilization**: GPU acceleration with fallback capability

### Detection and Classification:
- **Confidence Scoring**: Uses model confidence scores for harmful payload probability
- **Bounding Box Format**: Normalized coordinates (xywhn format) converted to min/max bounds
- **Output Format**: Structured CSV with standardized submission format

### Post-processing:
- **Label Mapping**: Binary classification to "Harmful"/"Normal" labels
- **Standardized Output**: CSV format compatible with submission requirements

### Performance Optimizations:
- GPU acceleration for faster inference
- Batch processing to reduce overhead
- Streaming results to minimize memory usage
- Efficient coordinate transformations

## Hardware Specifications

### GPU Details:
- 2 Nvidia T4 GPUs (16GB x 2)

### CPU & RAM Details:
- Intel Xeon(R) @ 2.2Ghz with 32GB of RAM

## Model Details:
- **Architecture**: YOLOv12m
- **Task**: Payload Classification (Binary)
- **Classes**: Harmful (0), Normal (1)
- **Input Resolution**: 640x640
- **Batch Size**: 16
- **Model File**: yolov12trainingpayloadRGB.pt
- **Framework**: Ultralytics YOLO