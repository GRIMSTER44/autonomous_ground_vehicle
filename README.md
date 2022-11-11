# autonomous_Car_Model
## Getting started with Carla
Carla is an open-source autonomous driving environment that also comes with a Python API to interact with it. Carla helps us to create an environment where we can use a car mounted with a bunch of sensors to emulate real-life self-driving car
## Setting Carla enviornment
First of all we will have to download Carla's latest version [0.9.13](https://carla.org/2021/11/16/release-0.9.13/). Now firstly we will create a virtual enviornment as this verison of Carla needs python 3.7 version. Virtual enviornment will be created using miniconda. 
```
$ conda create -n autocar python=3.7
```
Now you will need to install serveral libraries such as numpy using pip. But first of all lets install carla
```
$ pip install carla
```
Now to run Carla on Windows, just double click the .exe. If you are using Linux, open a terminal in that directory and do
```
$ ./CarlaUE4.sh
```
Go ahead and navigate from the main Carla directory to the examples: PythonAPI/examples. Here we have many scripts for generating traffic, changing weathers, etc. Lets create traffic with 80 vehicles. Open cmd/terminal
```
$ python generate_traffic -n80
```
This will spawn 80 vehicles in simulator.
To drive the car manually open another cmd/terminal in same foolder i.e PythonAPI/examples and run
```
$ python manual_control.py
```
## Data extraction using Carla
