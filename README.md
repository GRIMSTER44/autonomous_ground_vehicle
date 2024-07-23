# Autonomous Vehicle Deep Learning Project

## Overview
This project involves developing a deep learning model to predict steering angles for an autonomous vehicle. The model is integrated with a Raspberry Pi 4 Model B for real-time operation and control of the vehicle.
   [here](https://drive.google.com/file/d/1HAA9iVvYc70xF-zYHqx6fOmBDxKFQHcL/view)

## Features
- **Deep Learning Model:** Predicts steering angles from images captured by a front-mounted camera.
- **Real-Time Operation:** Deployed on a Raspberry Pi 4 Model B.
- **Integration:** Connects with hardware components such as a servo motor for steering adjustments.
- **Preprocessing:** Images are resized and normalized for improved model accuracy.
- **Road Segmentation:** Utilizes a pretrained model to assist with identifying drivable areas.

## Getting Started

### Prerequisites
- **Hardware:**
  - Raspberry Pi 4 Model B
  - Front-mounted camera
  - Servo motor

- **Software:**
  - Python
  - TensorFlow
  - OpenCV
  - CARLA simulator (for data collection)

### Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

## Challenges
- **Data Discrepancies:** Bridging the gap between simulation and real-world data to improve accuracy.
- **Track Design:** Ensuring the turning radius in simulations matches the real-world vehicle.
- **Signal Noise:** Addressing noise in the servo motor signal to reduce instability.

## Future Improvements
- **Enhanced Data Collection:** More real-world data for better model performance.
- **Track Accuracy:** Refining simulation tracks to match real-world dynamics.
- **Noise Reduction:** Implementing advanced filtering techniques for smoother control.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- CARLA Simulator
- TensorFlow and Keras
- OpenCV

