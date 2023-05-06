import cv2 
from tensorflow import keras
import tensorflow as tf
import numpy as np
import RPi.GPIO as GPIO
import time

path = 'edp.h5'
segment_path = 'best_model.h5'

print("Model")

model = keras.models.load_model(path)
segment = keras.models.load_model(segment_path)


GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)

servo = GPIO.PWM(11,50)

duty_intialize = 5

servo.start(0)
time.sleep(1)

key = cv2.waitKey(0)
webcam = cv2.VideoCapture(1)

while True:
    try:
        check, frame = webcam.read()

        # print(frame.size())

        img = cv2.resize(frame, (128, 128), interpolation=cv2.INTER_AREA)


        # img = cv2.cvtColor(bigger, cv2.COLOR_BGR2RGB)

        img = np.array(img)

        # cv2.imshow("Capturing", img)

        img = np.reshape(img, (-1, 128, 128, 3))

        
        segment_mask = segment.predict(img)

        segment_mask = np.array(segment_mask)

        print("Segmented")
        print(segment_mask.shape)

        segment_img = []
        for img in segment_mask:
            segment_img.append(cv2.resize(img, (220, 110)))
       
        segment_img = np.reshape(segment_img, (-1, 110, 220, 1))
        segment_img = np.array(segment_img)
        print(segment_img.shape)

        cv2.imwrite("segment.jpg", segment_img[0])

        # steer_max, steer_min

        predict_values = model.predict(segment_img)

        duty = duty_intialize + 3*predict_values

        servo.ChangeDutyCycle(duty)
        time.sleep(1)


        # print(predict_values)

        key = cv2.waitKey(1000)
              
    except(KeyboardInterrupt):
        servo.stop()
        GPIO.cleanup()
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
    