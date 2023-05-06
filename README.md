# Autonomous_ground_vehicle
We have developed an autonomous vehicle model using deep learning. Deep learning is used for predicting steering angle. Raspberry pi 4 model B is used for interfacing. Testing video of our proposed vehicle on sample track can be found [here](https://drive.google.com/file/d/1HAA9iVvYc70xF-zYHqx6fOmBDxKFQHcL/view?usp=share_link).
## Getting started with Carla
[Carla](https://carla.org) is an open-source autonomous driving environment that also comes with a Python API to interact with it. Carla helps us to create an environment where we can use a car mounted with a bunch of sensors to emulate real-life self-driving car. Refer the [link](https://carla.readthedocs.io/en/latest/start_quickstart/) for installing and running carla. For dataset collection a camera has been mounted in front of vehicle and its images and corresponding steering and throtle have been collected. The code for same can be found [here]
## Raspberry Pi 4 Model B
Raspberry pi is used for running this models because of its high processing power and smaller size. We have mounted webcam in front of our vehicle. Then by using [opencv](https://opencv.org/) we have captured the image and preprocessed it. Steering angle is then predicted from this images. This angle in passed to servo motor.
A pretrained model for [road segmentation] has been used. The code for steering angle prediction can be found [here]. Further, the code which was used in raspberry pi is mentioned [here].
## Problems Faced
We have faced many problems in this process. Some are mentioned here:
1. Data collected was from simulation. Hence there was gap between simulation data and real world data which affected the accuracy of overall model.
2. Turning radius of map created was higher than steering angle from servo! A silly mistake occured due to lack of focus on track creation.
3. Noise in signal generated for servo, this caused servo to shake.

    
