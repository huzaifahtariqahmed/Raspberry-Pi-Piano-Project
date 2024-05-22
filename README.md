# Raspberry Pi Piano Project - Programming Fundamentals Course Project

## Aim
To put the practicality of Python to use via interfacing it with Raspberry Pi and hence creating a piano which plays all the seven notes.

## Components
- Breadboard
- Raspberry Pi
- Jumper Wires
- Push Buttons
- Passive Buzzer

## Implementation
In our project, we created a Raspberry Pi-based piano by integrating a breadboard, jumper wires, push buttons, and a passive buzzer. Our implementation strategy involved configuring the GPIO pins on the Raspberry Pi to correspond with the buttons and buzzer. We wrote a Python script utilizing the `gpiozero` library to manage button inputs and buzzer outputs. Each button was assigned a specific musical note, and we used the `TonalBuzzer` class to play these notes. We defined functions to play each note (A, B, C, D, E, F, G) and a function to stop the buzzer sound. By mapping the button presses to these functions, we ensured that pressing a button would play the corresponding note and releasing it would stop the sound. This setup allowed us to create a simple yet functional electronic piano.
