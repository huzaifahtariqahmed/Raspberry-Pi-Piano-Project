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

## Bugs
I faced trouble in outputting the sound directly from the built-in function of the python library for different frequencies such as the minor and major frequencies of each harmonic. However, it was not applicable since there was non-availability of the piezo-electric buzzer which resonates electromagnetically and produces a variety of pleasant sounds. This was overcome by using python’s TonalBuzzer library which accorded for a fixed amount of frequencies, which were then used to play each note, albeit flat.

## Learning Outcomes
This was an extremely fun-filled project which, as stated in our aim above, enabled to bridge the gap between theory and practical implications of Python. It also gave a deep insight in to a variety of such projects that have been made using the same inspiration as well as giving new ideas which I hope to implement as well.

---

### Contributors
- [Huzaifah Tariq Ahmed](https://github.com/huzaifahtariqahmed)
- Shah Jahan Sangrassi
