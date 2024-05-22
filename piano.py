from gpiozero import TonalBuzzer, Button 
from gpiozero.tones import Tone
from time import sleep
#importing different libraries for use in the project
b=TonalBuzzer(21) #defining GPIO pin number 21 as a buzzer
#defining GPIO pin numbers in the brackets for the respective buttons
button1=Button(2) 
button2=Button(3)
button3=Button(4)
button4=Button(17)
button5=Button(27)
button6=Button(22)
button7=Button(10)
#now defining the notes or harmonics of the piano
def turner():
		b.stop()
def note1(): #A note
		b.play(Tone(440))
def note2(): #B note
		b.play(Tone(494))
def note3(): #C note
		b.play(Tone(523))
def note4(): #D note
		b.play(Tone(587))
def note5(): #E note
		b.play(Tone(659))
def note6(): #F note
		b.play(Tone(698))
def note7(): #G note
		b.play(Tone(784))
#assigning the notes to each button which will then play the corresponding note when pressed
button1.when_pressed=note1
button1.when_released=turner
button2.when_pressed=note2
button2.when_released=turner
button3.when_pressed=note3
button3.when_released=turner
button4.when_pressed=note4
button4.when_released=turner
button5.when_pressed=note5
button5.when_released=turner
button6.when_pressed=note6
button6.when_released=turner
button7.when_pressed=note7
button7.when_released=turner
