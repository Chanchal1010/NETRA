# NETRA

Development of a Smart Stick for the Visually Impaired using Raspberry Pi

<details>
<summary>Table of Contents</summary>
  
- [Description](#description)
- [Features](#features)
- [Installations](#installations)
- [Components](#components)
- [Project Setup](#project-setup)
- [Links](#links)
- [Applications](#applications)
- [Team Members](#team-members)
  
</details>

## 📝Description

This project outlines the design, development, and implementation of a Smart Stick, a novel assistive device aimed at improving mobility and independence for the visually impaired. Leveraging the capabilities of Raspberry Pi, the Smart Stick integrates various sensors and technologies to provide real-time feedback and assistance to users navigating their surroundings. The report discusses the motivation behind the project, the methodology employed in its development, the technical specifications of the device, as well as its potential impact and future enhancements.

## 🤖Features

Object Detection: Uses an ultrasonic sensor to detect nearby objects.
Object Identification: Employs OpenCV to recognize and identify objects in real-time.

## 🔗Installations

>To run this project, you'll will have to setup Raspbian OS

## ⚙ Components

Raspberry Pi (any model with GPIO and camera support)
Ultrasonic Sensor (e.g., HC-SR04)
Camera Module (compatible with Raspberry Pi)
Power Supply
Stick (to house the components)

## 👨‍💻Project Setup

Hardware:
>Mount the Ultrasonic Sensor: Attach the sensor to the front of the stick. Connect the sensor's VCC, GND, TRIG, and ECHO pins to the corresponding GPIO pins on the Raspberry Pi.

>Mount the Camera: Attach the camera module to the stick, ensuring it has a clear view. Connect it to the Raspberry Pi's camera interface.

>Power Supply: Connect a reliable power supply to the Raspberry Pi.

Software:

Install Raspberry Pi OS: Set up the Raspberry Pi with the latest Raspberry Pi OS.

Update the System: Open a terminal and run:
```bash
sudo apt-get update
sudo apt-get upgrade
```

Install Required Libraries:
```bash
sudo apt-get install python3-opencv python3-pip
pip3 install RPi.GPIO
```

Clone the Repository:
```bash
git clone https://github.com/Chanchal1010/NETRA
```
Navigate to the project directory:
```bash
cd NETRA
```

Run the Program:
```bash
python3 NETRA.py
```

## 🔗Links

- [GitHub Repository](https://github.com/Chanchal1010/NETRA)
- [Demo Video]()

## 💸Applications

> Outdoor Mobility: The Smart Stick assists visually impaired individuals in safely navigating outdoor environments, including sidewalks, streets, and pedestrian crossings. It detects obstacles, such as vehicles, poles, or uneven terrain, and provides real-time feedback to the user to avoid collisions.

> Indoor Navigation: In indoor settings, such as buildings, shopping malls, or public facilities, the Smart Stick helps users navigate through hallways, corridors, and rooms. It can detect obstacles like furniture, walls, and doors, providing guidance and directional cues to reach desired destinations.

> Public Transportation: The Smart Stick aids visually impaired individuals in accessing public transportation systems, including bus stops, train platforms, and subway stations. It assists users in locating boarding points, navigating through crowded areas, and identifying departure times and routes.

> Obstacle Detection: Beyond navigation, the Smart Stick serves as a valuable tool for detecting obstacles in various environments, alerting users to potential hazards and barriers in their path. This includes detecting low-hanging branches, overhead obstacles, and protruding objects.

> Education and Training: The Smart Stick can be used as a training tool for orientation and mobility instructors to teach visually impaired individuals essential navigation skills and techniques. It simulates real-world scenarios and provides feedback to help users develop confidence and independence.

## 👨‍💻Team Members

- [Aparna Bhutada](https://github.com/): bhutadaaparna@gmail.com 
- [Chanchal Bahrani](https://github.com/): 10bahranichanchal@gmail.com
