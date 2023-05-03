# Autonomous_ground_vehicle
We have developed an autonomous vehicle model using deep learning. Deep learning is used for predicting steering angle. Dataset required for this has been collected using Carla Simulator
## Getting started with Carla
[Carla](https://carla.org) is an open-source autonomous driving environment that also comes with a Python API to interact with it. Carla helps us to create an environment where we can use a car mounted with a bunch of sensors to emulate real-life self-driving car. Refer the [link](https://carla.readthedocs.io/en/latest/start_quickstart/) for installing and running carla. Dataset for steering angle rgb images mounted in front of vehicle and corresponding steering and throtle values.
## Raspberry Pi 4
Raspberry pi is used for running this models. We have mounted webcam in front of our vehicle. Then by using [opencv](https://opencv.org/) we have captured the image and preprocessed it. Steering angle is then predicted from this images. This angle in passed to servo motor.

    
