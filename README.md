# Facial Recognition Security System for Visually Impaired

## Objective

The primary objective of this project is to develop a facial recognition system designed to enhance the security and independence of visually impaired individuals. This initiative is driven by a commitment to positively impact society by providing a practical solution that addresses the unique challenges faced by those with visual impairments. Our goal is to create a system that helps visually impaired individuals live more securely and confidently, both in their personal and public spaces.

## Overview

The Facial Recognition Security System uses advanced computer vision and machine learning technologies to offer a practical and effective security solution for visually impaired individuals. Developed using Python and OpenCV, the system processes real-time images captured by a front door camera, extracts facial features, and analyzes them to identify individuals.

### Key Features

- **Real-Time Facial Recognition**: The system captures live images of individuals at the door and processes them in real-time.
- **Face Feature Extraction**: Utilizes OpenCV and `face_recognition` libraries to extract and analyze facial features.
- **Known-Person Database**: Compares captured faces with a database of recognized individuals to identify them.
- **Voice Alerts**: Provides voice notifications to inform the visually impaired user about the person at the door.

## Proposed Methodology

1. **Data Capture**: A front door camera continuously captures images of individuals approaching the door.
2. **Image Processing**: The captured images are processed using OpenCV for image manipulation and `numpy` for numerical operations.
3. **Facial Recognition**: The `face_recognition` library is employed to extract facial features and create distinctive signatures for each person.
4. **Face Matching**: The system compares the extracted facial signatures with those stored in the known-person database to identify individuals.
5. **Notification System**: Upon identifying a person, the system uses text-to-speech (TTS) technology to announce the individual's name and alert the visually impaired user.

## Advantages

- **Enhanced Security**: Provides a reliable method for visually impaired individuals to identify people at their door without needing to see them.
- **Increased Independence**: Empowers users to make informed decisions about interacting with visitors, enhancing their sense of security and autonomy.
- **Practical Solution**: Offers a real-time, practical security solution that integrates seamlessly into daily life.
- **Positive Social Impact**: Aims to improve the quality of life for visually impaired individuals by addressing a critical need for accessible security solutions.

## Technology Stack

- **Python**: The programming language used for implementing the system.
- **OpenCV**: A library used for image processing and manipulation.
- **Numpy**: A library for numerical operations.
- **face_recognition**: A library for facial recognition and feature extraction.
- **Text-to-Speech (TTS)**: Used for voice notifications to alert the user.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Run the code**:
   ```bash
   python main.py
   ```

## Contributing

Contributions are welcome to enhance the system's features and performance. Feel free to submit issues or pull requests.
