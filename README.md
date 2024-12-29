# HANDFULL
# HandFull: A Python Library for Hand Gesture Recognition

![contribution](https://img.shields.io/badge/contributions-welcome-blue)
![python](https://img.shields.io/badge/Python-3.9_or_later-green)
![opencv](https://img.shields.io/badge/OpenCV-4.5_or_later-green)

Welcome to HandFull, a Python-based library for hand gesture recognition! This README provides a detailed overview of the project, including its features, usage, architecture, development process, references, and enhancements.

## (1) 程式的功能 Features

HandFull offers the following features:

- **Real-time Gesture Recognition**: Detect and classify hand gestures from video streams.
- **Multi-hand Support**: Recognizes gestures from both hands simultaneously.
- **Custom Gesture Training**: Train models to recognize user-defined gestures.
- **Visualization Tools**: Displays bounding boxes and labels for detected gestures.
- **Export/Import Models**: Save and load trained models for reuse.
- **Voice output results**: Improve the interactive experience by outputting the recognized voice results through voice.

## (2) 使用方式 Usage

Follow these steps to use HandFull:

### 1. Set Up Your Environment

Install HandFull and its dependencies with the following commands:

```bash
# Create a virtual environment
python -m venv handfull-env

# Activate the environment
# On Windows:
source handfull-env\Scripts\activate
# On macOS/Linux:
source handfull-env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Gesture Recognition

Use the example code below to recognize gestures in real time:

```python
from hand_full import HandFull

# Initialize HandFull
recognizer = HandFull()

# Start video capture and recognition
recognizer.start_recognition()
```

### 3. Train Custom Gestures

Train your own gestures with the following script:

```python
from hand_full import HandFull

# Initialize HandFull
recognizer = HandFull()

# Collect training data
recognizer.collect_training_data("gesture_name")

# Train the model
recognizer.train_model()

# Save the trained model
recognizer.save_model("custom_model.h5")
```

## (3) 程式的架構 Program Architecture

The project is organized as follows:

```
HandFull/
├── hand_full/
└── README.md          # Documentation
```

- **Core Components**:
  - `hand_detector.py`: Processes video streams and detects gestures.
  - `model_trainer.py`: Handles training and saving custom gesture models.
  - `visualization.py`: Provides tools for debugging and displaying results.

## (4) 開發過程 Development Process

The development of HandFull followed these steps:

1. **Research and Planning**: Analyzed requirements for real-time gesture recognition.
2. **Implementation**: Built modules for detection, training, and visualization.
3. **Testing**: Verified performance with various gestures and scenarios.
4. **Enhancements**: Improved accuracy and added support for custom models.

## (5) 參考資料來源 References

1. [OpenCV](https://opencv.org/) - Used for image processing and feature detection.
2. [MediaPipe](https://mediapipe.dev/) - Framework for hand-tracking models.
3. ChatGPT - Assisted with integration of the above two sets of code.

## (6) 程式修改或增強的內容 Enhancements and Contributions

### Reference Features Integrated:
1. Added multi-hand recognition inspired by MediaPipe's tracking capabilities.
2. Provided visualization tools for easier debugging and model evaluation.

### Unique Contributions:
1. Developed customizable training pipelines for user-defined gestures.
2. Calculate the number represented by the gesture.
3. In addition to the numbers 1-99, add the ok gesture and output the ok voice.
4. Changed one-handed detection in reference material to two-handed detection.
5. Enabled export/import functionality for saving and reusing models.
6. Enhanced real-time performance with optimized algorithms.
7. Use the speech export function to export numbers or custom speech in Chinese, it can be changed with different languages ​​and tones.

We encourage further modifications and welcome community contributions to improve HandFull!

