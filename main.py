# Import necessary libraries
#!/usr/bin/env python3

import cv2
import RPi.GPIO as GPIO
import time
import subprocess

# Define GPIO pins
TRIG_PIN = 11
ECHO_PIN = 13

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# Function to speak
def speak(text):
    subprocess.call(['espeak', text])

# Function to measure distance using ultrasonic sensor
def measure_distance():
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, GPIO.LOW)

    pulse_start = time.time()
    pulse_end = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

# Function to initialize camera
def initialize_camera():
    cap = cv2.VideoCapture(0, cv2.CAP_LIBCAMERA)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
    cap.set(cv2.CAP_PROP_MODE, 1)
    cap.set(cv2.CAP_PROP_FORMAT, 0)
    return cap

# Function to perform object detection
def detect_objects(net, classNames, img):
    classIds, confs, bbox = net.detect(img, confThreshold=0.5)
    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
            className = classNames[classId - 1].upper()
            cv2.putText(img, className, (box[0] + 10, box[1] + 30),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            speak("Object detected")
            speak(className)
    return img

# Main function
def main():
    while True:
        classNames = []
        with open('coco.names', 'rt') as f:
            classNames = f.read().rstrip('\n').split('\n')

        configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
        weightsPath = 'frozen_inference_graph.pb'

        net = cv2.dnn_DetectionModel(weightsPath, configPath)
        net.setInputSize(160, 160)  
        net.setInputScale(1.0 / 127.5)
        net.setInputMean((127.5, 127.5, 127.5))
        net.setInputSwapRB(True)

        cap = initialize_camera()

        try:
            while True:
                distance = measure_distance()
                print("Distance:", distance)

                if distance <= 60:
                    # speak("obstacle ahead")
                    ret, frame = cap.read()
                    if ret:
                        img = detect_objects(net, classNames, frame)
                        cv2.imshow("Object Detection", img)

                    if cv2.waitKey(1) == ord('q'):
                        break
                else:
                    speak("safe")

                # Add a delay to prevent the ultrasonic sensor from being read too quickly
                time.sleep(1)

        finally:
            GPIO.cleanup()
            cv2.destroyAllWindows()

if _name_ == "_main_": 
    main()