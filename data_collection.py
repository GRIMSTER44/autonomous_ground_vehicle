import carla
import os
import random
from datetime import datetime
import time
import numpy as np
import sys
import csv 


curr_time = round(time.time()*1000)

print(curr_time)

def save_to_csv(idx, steering_angle, throttle, turn):
    with open('/home/deep/auto_vehicle/CARLA_0.9.11/outputs/controls.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([idx, steering_angle, throttle, turn])

def main():
    client = carla.Client('localhost', 2000)
    client.set_timeout(2.0)
    world = client.get_world()


    actor_list = []
    sensor_list = []
    controllers = []

    i = 0
    
    try:

        original_settings = world.get_settings()
        settings = world.get_settings()

        # We set CARLA syncronous mode
        settings.fixed_delta_seconds = 0.05
        settings.synchronous_mode = True
        world.apply_settings(settings)


        world = client.load_world('Town02') # you can also retrive another world by specifically defining 1, 4, 2
        blueprint_library = world.get_blueprint_library()
        # Set weather for your world
        weather = carla.WeatherParameters(cloudiness=0.0,
                                          sun_altitude_angle=70,
                                          precipitation=10.0,
                                          fog_density=0.0)
        world.set_weather(weather)

        # create the ego vehicle
        ego_vehicle_bp = blueprint_library.find('vehicle.tesla.model3')
        # black color
        ego_vehicle_bp.set_attribute('color', '0, 0, 0')
        # get a random valid occupation in the world
        transform = random.choice(world.get_map().get_spawn_points())
        # spawn the vehilce
        ego_vehicle = world.spawn_actor(ego_vehicle_bp, transform)
        # set the vehicle autopilot mode
        ego_vehicle.set_autopilot(True)

        
        # control = carla.VehicleControl(throttle=0.2)
        # ego_vehicle.apply_control(control)

        # collect all actors to destroy when we quit the script
        actor_list.append(ego_vehicle)

        list_actor = world.get_actors()
        for actor_ in list_actor:
            if isinstance(actor_, carla.TrafficLight):
                # for any light, first set the light state, then set time. for yellow it is 
                # carla.TrafficLightState.Yellow and Red it is carla.TrafficLightState.Red
                actor_.set_state(carla.TrafficLightState.Green) 
                actor_.set_green_time(1000.0)

        # add a camera
        camera_bp = blueprint_library.find('sensor.camera.rgb')
        segment_bp = blueprint_library.find('sensor.camera.semantic_segmentation')
        
        camera_bp.set_attribute('image_size_x', '256')
        camera_bp.set_attribute('image_size_y', '256')
        camera_bp.set_attribute('fov', '110')

        segment_bp.set_attribute('image_size_x', '256')
        segment_bp.set_attribute('image_size_y', '256')
        segment_bp.set_attribute('fov', '110')

        # camera relative position related to the vehicle

        # front side
        camera_transform_f = carla.Transform(carla.Location(x=2.5, z=1.0))

        # left side
        # camera_transform_l = carla.Transform(carla.Location(x=0, z=1.8, y=-0.3), carla.Rotation(0, -100, 0))

        # # right side
        # camera_transform_r = carla.Transform(carla.Location(x=0, z=1.8, y=0.3), carla.Rotation(0, 100, 0))

        # # back side
        # camera_transform_b = carla.Transform(carla.Location(x=-2.0, z=1.5), carla.Rotation(0, 180, 0))

        # #bev
        # camera_transform_bev = carla.Transform(carla.Location(x=0, y=0, z=15), carla.Rotation(pitch=-90))


        camera_f = world.spawn_actor(camera_bp, camera_transform_f, attach_to=ego_vehicle)
        # camera_l = world.spawn_actor(camera_bp, camera_transform_l, attach_to=ego_vehicle)
        # camera_r = world.spawn_actor(camera_bp, camera_transform_r, attach_to=ego_vehicle)
        # camera_b = world.spawn_actor(camera_bp, camera_transform_b, attach_to=ego_vehicle)

        segment_f = world.spawn_actor(segment_bp, camera_transform_f, attach_to=ego_vehicle)
        # segment_l = world.spawn_actor(segment_bp, camera_transform_l, attach_to=ego_vehicle)
        # segment_r = world.spawn_actor(segment_bp, camera_transform_r, attach_to=ego_vehicle)
        # segment_b = world.spawn_actor(segment_bp, camera_transform_b, attach_to=ego_vehicle)


        # bev = world.spawn_actor(segment_bp, camera_transform_bev, attach_to=ego_vehicle)

        output_path_f = '/home/deep/auto_vehicle/CARLA_0.9.11/outputs/front/img'
        # output_path_l = '/media/deep/DEEP/outputs/img/l'
        # output_path_r = '/media/deep/DEEP/outputs/img/r'
        # output_path_b = '/media/deep/DEEP/outputs/img/b'

        segment_output_path_f = '/home/deep/auto_vehicle/CARLA_0.9.11/outputs/front/segment'
        # segment_output_path_l = '/media/deep/DEEP/outputs/segment/l'
        # segment_output_path_r = '/media/deep/DEEP/outputs/segment/r'
        # segment_output_path_b = '/media/deep/DEEP/outputs/segment/b'


        # bev_output_path = '/media/deep/DEEP/outputs/bev'

        # Getting the current date and time
        curr_time = round(time.time()*1000)

        if not os.path.exists(output_path_f):
            os.makedirs(output_path_f)

        # if not os.path.exists(output_path_l):
        #     os.makedirs(output_path_l)

        # if not os.path.exists(output_path_r):
        #     os.makedirs(output_path_r)

        # if not os.path.exists(output_path_b):
        #     os.makedirs(output_path_b)


        if not os.path.exists(segment_output_path_f):
            os.makedirs(segment_output_path_f)

        # if not os.path.exists(segment_output_path_l):
        #     os.makedirs(segment_output_path_l)

        # if not os.path.exists(segment_output_path_r):
        #     os.makedirs(segment_output_path_r)

        # if not os.path.exists(segment_output_path_b):
        #     os.makedirs(segment_output_path_b)

        # if not os.path.exists(segment_output_path_b):
        #     os.makedirs(segment_output_path_b)

        # if not os.path.exists(bev_output_path):
        #     os.makedirs(bev_output_path)

        # set the callback function\

        # print(curr_time)


        segment_f.listen(lambda image: image.save_to_disk(os.path.join(segment_output_path_f, '%d.png' % i), carla.ColorConverter.CityScapesPalette))

        camera_f.listen(lambda image: image.save_to_disk(os.path.join(output_path_f, '%d.png' % i)))
        
        # camera_l.listen(lambda image: image.save_to_disk(os.path.join(output_path_l, '%d.png' % i)))
        # camera_r.listen(lambda image: image.save_to_disk(os.path.join(output_path_r, '%d.png' % i)))
        # camera_b.listen(lambda image: image.save_to_disk(os.path.join(output_path_b, '%d.png' % i)))

        
        # segment_l.listen(lambda image: image.save_to_disk(os.path.join(segment_output_path_l, '%d.png' % i), carla.ColorConverter.CityScapesPalette))
        # segment_r.listen(lambda image: image.save_to_disk(os.path.join(segment_output_path_r, '%d.png' % i), carla.ColorConverter.CityScapesPalette))
        # segment_b.listen(lambda image: image.save_to_disk(os.path.join(segment_output_path_b, '%d.png' % i), carla.ColorConverter.CityScapesPalette))


        # bev.listen(lambda image: image.save_to_disk(os.path.join(bev_output_path, '%d.png' % i), carla.ColorConverter.CityScapesPalette))

        sensor_list.append(camera_f)
        # sensor_list.append(camera_l)
        # sensor_list.append(camera_r)
        # sensor_list.append(camera_b)

        sensor_list.append(segment_f)
        # sensor_list.append(segment_l)
        # sensor_list.append(segment_r)
        # sensor_list.append(segment_b)
        # sensor_list.append(bev)


        
        


        while True:
            # Tick the server
            world.tick()

            # set the sectator to follow the ego vehicle
            turn = 0
            spectator = world.get_spectator()
            transform = ego_vehicle.get_transform()
            controllers_temp = []
            control = ego_vehicle.get_control()
            if control.steer > 0.1: turn = 1
            if control.steer < -0.1: turn = -1
            save_to_csv(i, control.steer, control.throttle, turn)
            spectator.set_transform(carla.Transform(transform.location + carla.Location(z=20), carla.Rotation(pitch=-90)))
            i = i+1

    finally:
        
        # print('storing controls')
        # np_array = np.array(controllers)
        # file = open(txt_path, "w+")
 
        # # Saving the array in a text file
        # content = str(np_array)
        # file.write(content)
        # file.close()
        
        world.apply_settings(original_settings)
        print('destroying actors')
        client.apply_batch([carla.command.DestroyActor(x) for x in actor_list])
        for sensor in sensor_list:
            sensor.destroy()
        print('done.')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(' - Exited by user.')
