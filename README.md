# End-to-End Waste Detection Using YOLOv8

[![GitHub](https://img.shields.io/badge/GitHub-Lavishgangwani%2FEnd--to--end--WasteDetection--Using--YoloV8-blue)](https://github.com/Lavishgangwani/End-to-end-WasteDetection-Using-YoloV8)

## Overview
This project is a comprehensive pipeline for waste detection using the YOLOv8 object detection model. It incorporates data annotation through RoboFlow, model training, evaluation, and deployment. The goal is to identify waste in images and videos for environmental applications such as automated recycling and litter management.

## Features
- **Data Annotation**: Use RoboFlow for efficient and structured dataset creation.
- **Object Detection Model**: Leverage YOLOv8 for accurate and fast waste detection.
- **End-to-End Workflow**: Covers dataset preparation, training, evaluation, and deployment.
- **Customizable**: Easily adapt the pipeline for different datasets or object categories.

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Data Preparation](#data-preparation)
4. [Model Training](#model-training)
5. [Evaluation](#evaluation)
6. [Deployment](#deployment)
7. [Results](#results)
8. [Future Work](#future-work)
9. [License](#license)

## Requirements

To run this project, ensure you have the following dependencies installed:

- Python 3.8+
- PyTorch
- YOLOv8 (via [Ultralytics](https://github.com/ultralytics/ultralytics))
- RoboFlow Python SDK
- OpenCV
- Matplotlib
- NumPy
- Pandas

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Lavishgangwani/End-to-end-WasteDetection-Using-YoloV8.git
    cd End-to-end-WasteDetection-Using-YoloV8
    ```

2. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Install YOLOv8 from Ultralytics:

    ```bash
    pip install ultralytics
    ```

## Data Preparation

1. **Data Annotation**:
    - Use [RoboFlow](https://roboflow.com/) for annotating images of waste objects.
    - Export the dataset in YOLO format.

2. **Organize Data**:
    - Place the dataset in the following structure:

      ```
      dataset/
      |-- train/
      |   |-- images/
      |   |-- labels/
      |-- val/
      |   |-- images/
      |   |-- labels/
      ```

3. **Dataset Configuration**:
    - Create a `data.yaml` file specifying paths to the train and validation datasets:

      ```yaml
      path: dataset
      train: train/images
      val: val/images
      nc: <number of classes>
      names: ["class1", "class2", "..."]
      ```

## Model Training

1. **Train the YOLOv8 Model**:
    
    ```bash
    yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640
    ```
    
    - `model=yolov8n.pt`: Use YOLOv8 nano as a base model (replace with `yolov8s.pt`, `yolov8m.pt`, etc., for larger models).
    - `epochs`: Set the number of training epochs.
    - `imgsz`: Define the image size for training.

2. **Monitor Training**:
    - Use the training logs to monitor metrics like precision, recall, and mAP (mean Average Precision).

## Evaluation

1. **Validate the Model**:

    ```bash
    yolo task=detect mode=val model=runs/detect/train/weights/best.pt data=data.yaml
    ```

2. **Performance Metrics**:
    - Precision, Recall, F1 Score, and mAP.
    - Use the YOLOv8 evaluation tools to analyze these metrics.

3. **Visualize Predictions**:

    ```bash
    yolo task=detect mode=predict model=runs/detect/train/weights/best.pt source=val/images
    ```

    - `source`: Path to the validation images.

## Deployment

1. **Inference on Images and Videos**:

    ```bash
    yolo task=detect mode=predict model=runs/detect/train/weights/best.pt source=<path-to-images-or-videos>
    ```

2. **Export Model**:
    - Export the trained model to formats like ONNX, TensorRT, or CoreML for deployment:

      ```bash
      yolo export model=runs/detect/train/weights/best.pt format=onnx
      ```

3. **Web or Edge Deployment**:
    - Integrate the exported model into web or edge devices for real-time detection.

## Results

- **Example Predictions**:
    - Include before-and-after images with bounding boxes for detected objects.

- **Performance**:
    - Example metrics: mAP@0.5 = 92%, Precision = 95%, Recall = 91%.

## Future Work

- Fine-tune the model with more diverse datasets.
- Deploy the model on edge devices like NVIDIA Jetson or Raspberry Pi.
- Develop a web interface for user-friendly detection.
- Experiment with multi-class waste categorization.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to contribute or report issues in the [GitHub repository](https://github.com/Lavishgangwani/End-to-end-WasteDetection-Using-YoloV8).

