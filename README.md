# Laser Face Tracker

Existing Python/OpenCV face-tracking scripts and an Arduino servo-control sketch.
This repository preserves the original tracking and hardware-control code.

**Safety:** Never direct a laser at a person's face or eyes. Keep any laser
disconnected when experimenting with face tracking; use a harmless visual
indicator instead. This code does not implement laser safety interlocks.

## Project files

- `python_laser_face/face_recog.py`: webcam face detection and serial coordinate output.
- `python_laser_face/laser_control.py`: manual serial coordinate input.
- `python_laser_face/haarcascade_frontalface_default.xml`: bundled OpenCV face detector.
- `laser_control.ino`: Arduino serial input and two-servo control.

The Python scripts depend on OpenCV (`opencv-python`) and PySerial (`pyserial`).
They currently use serial port `COM4`. The face detector uses a relative cascade
path, so its working directory must be `python_laser_face`. The Arduino sketch
uses the Servo library, pins 10 and 11, and a serial baud rate of 9600.
Hardware operation has not been verified as part of publishing this repository.

## Attribution and licensing

`face_recog.py` retains its original author attribution to Guido Diepen.
The bundled cascade credits Rainer Lienhart and contains the Intel Open Source
Computer Vision Library license, copyright notice, and redistribution terms.
These notices are preserved in the original files.

No project-wide license was provided with the original folder; publication does
not replace or expand the permissions granted by existing third-party notices.
