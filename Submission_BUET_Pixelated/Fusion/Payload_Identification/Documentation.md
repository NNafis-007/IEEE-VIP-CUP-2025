# RGB-IR Fusion Payload Identification Documentation

## Instructions on how to run the inference code

### Prerequisites:

- Set up the environment variables and paths in the notebook:
   - `weights_path`: Path to the fusion model weights (yolov12m_fusion_payload.pt)
   - `images_path`: Path to test images directory
   - `device`: GPU configuration ("0,1" for multi-GPU, "0" for single GPU, "cpu" for CPU)
   - `output_dir`: Directory to save inference results
   - `submission_filename`: Output CSV filename

### Running the inference:

- **Direct execution**: Run all cells in the Jupyter notebook `yolov12m_inference-payload.ipynb`

## Brief explanation of the approach

### Model Architecture:
- **Base Model**: YOLOv12m fine tuned with RGB-IR fusion 
- **Task**: Binary payload classification (Harmful vs Normal)
- **Model File**: yolov12m_fusion_payload.pt

### Fusion Approach:
- **Multi-modal Integration**: Replaced Blue channel of RGB with IR channel 

### Inference Pipeline:
1. **Environment Setup**: Initialize YOLOv5 environment and dependencies
2. **Model Loading**: Load pre-trained fusion model weights
3. **Batch Processing**: Process images using YOLOv5 detect.py script
4. **Result Parsing**: Extract detection results from output text files
5. **Format Conversion**: Convert YOLO format to submission-required format

### Detection Parameters:
- **Input Resolution**: 640x640 pixels
- **Confidence Threshold**: 0.1 (low threshold for maximum recall)
- **Multi-GPU Support**: Configurable device settings for optimal performance
- **Output Format**: YOLO text format with confidence scores

### Post-processing Pipeline:
- **Label Parsing**: Read detection results from text files
- **Coordinate Conversion**: Transform from center-width-height to min-max format
- **Classification Logic**:
  - Class 0: "Harmful" payload (prob_harmful = confidence score)
  - Class 1: "Normal" payload (prob_harmful = 0.0)

### Key Features:
- **Fusion Model Integration**: Leverages multi-modal learning for enhanced performance
- **Low Confidence Threshold**: Ensures high recall for critical payload detection
- **Multi-GPU Acceleration**: Supports distributed inference for faster processing
- **Robust Error Handling**: Fallback mechanisms for different output formats
- **Standardized Output**: Compatible submission format generation

## Hardware Specifications

### GPU Details:
- 2 Nvidia T4 GPUs (16GB x 2)

### CPU & RAM Details:
- Intel Xeon(R) @ 2.2Ghz with 32GB of RAM