# Autonomous_ground_vehilce
## Getting started with Carla
[Carla](https://carla.org) is an open-source autonomous driving environment that also comes with a Python API to interact with it. Carla helps us to create an environment where we can use a car mounted with a bunch of sensors to emulate real-life self-driving car.
## Setting Carla enviornment
First of all we will have to download Carla's latest version [0.9.13](https://carla.org/2021/11/16/release-0.9.13/). Now, we will need to create a virtual enviornment as this verison of Carla requires python 3.7 version. [Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html) can be used to create virtual enviornment. 
```
$ conda create -n autocar python=3.7
$ conda activate autocar
```
Now you will need to install Carla using pip. Also some more libraries such as numpy are required, which can be installed using pip.
```
$ pip install carla
```
Now to run Carla on Windows, just double click the .exe. If you are using Linux, open a terminal in that directory and do
```
$ ./CarlaUE4.sh
```
Go ahead and navigate from the main Carla directory to the examples: PythonAPI/examples. Here we have many scripts for generating traffic, changing weathers, etc. Lets create traffic with 80 vehicles. Open cmd/terminal and navigate to PythonAPI/examples and run
```
$ python generate_traffic -n80
```
This will spawn 80 vehicles in simulator.
To drive the car manually open another cmd/terminal in same foolder i.e PythonAPI/examples and run
```
$ python manual_control.py
```
## Sensor Data extraction using Carla
For controlling a car and extracting sensor data you need to write some scripts and include them in PythonAPI/examples.
Firstly we will write a code for finding the carla egg file. In order to import carla we need to find it. And also we will import some basic libraries such as random, time, numpy, opencv. This few lines of code is common to all the scripts.

```
import glob
import os
import sys

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla
import random
import time
import numpy as np
import cv2
```

If opencv is not install you can run the follwing command in terminal which has your virtual enviornment running
```
$ pip install opencv-python
```

Now we have a server i.e the world and clients i.e actors such as cars, sensors, pedestrains. We need a list to store actors. Also we need to destory them once we exit because without these our actors will be still on server.

```
actor_list = []
try:


finally:

    print('destroying actors')
    for actor in actor_list:
        actor.destroy()
    print('done.')
```

We have World(server), blueprint, and actors(clients) in Carla. To begin, we'll connect to our server, get the world, and then access the blueprints. 
```
actor_list = []
try:
    client = carla.Client('localhost', 2000)
    client.set_timeout(2.0)

    world = client.get_world()

    blueprint_library = world.get_blueprint_library()
```
Sometimes you may get an error saying "Make sure that your simulator is ready and is connecte to localhost:2000". This can ne rectified by restarting all the Carla windows and terminals/cmd and increase set_timeout.
    
