#debugging tools for the stepper motor
#run iterCoils() on a motor to iterate over all permutations of wire arrangements
#good tool for identifying a stepper motor's inner wiring 

#Jacob Mattie, August 7, 2025


import itertools
import lgpio
from time import sleep

delayBetweenSteps = 0.0025 #seconds. Note that setting this value too low can 'freeze' the motor through what I assume is impedance
numSteps = 20000 #Roughly 1 minute per test state

#coilPins are the pinouts on the raspberry pi
coilPins = [27,23,22,24]  

startState = 0
h = None

def stepOne(state, coils):
	nextState = (state+1) % 4
	for coil in coils: 
		lgpio.gpio_write(h, coil, 0)
	lgpio.gpio_write(h, coils[nextState], 1)
	return nextState

def goNum(numSteps, state, coils, delayTime):
	for el in range(numSteps):
		state = stepOne(state, coils)
		sleep(delayTime)

def iterCoils(numCycles, delayTime, coilsList):
	newCoilsList = []
	for coil in coilsList:
		newCoilsList.append(coil)	
	print(f"Hardcoded coils arrangement: {newCoilsList}")

	for perm in itertools.permutations(newCoilsList):
		print("Cycling through coil arrangement: {perm}")
		goNum(numCycles, state, perm, delayTime)

def openHandle():
	global h
	h = lgpio.gpiochip_open(0) #should be closed at the end of the function

def closeHandle():
	global h
	lgpio.gpiochip.close(h)



if __name__ == "__main__":
	openHandle()

	x = input(f"""
    HOW TO USE: 

    This is a script to identify the proper wiring for a stepper motor through a raspberry pi.
    A stepper motor controller can be set up by:
      1. Ordering the wires  
      2. Ordering the pin sequence called by the controller. 

    These methods are functionally equivalent. 
    
    This script is designed to be used on an already-wired stepper motor. 
    Connect the driver wires to the stepper motor in any order, and this script identifies the sequence in which the microcontroller pins should be called. 

    When the motor shaft rotates smoothly, make a note of the most recent values printed. 
    This is your pin ordering. 
           
            Note: this script requires the lgpio library.
            Install this with the commands: 
            pip install lgpio
            sudo apt update
            sudo apt install lgpio

    .............................................................................
    -----------------------------------------------------------------------------
    .............................................................................


	Enter any value to run a coil permutation test. 

    This iterates over all pinout sequences to identify the correct control sequence.
    When a working sequence is found, update the 'controller.py' code variable 'coilPins' with    the pin sequence.
    
    
	Leave blank to run a test step series with hardcoded values:
		   Step Delay: {delayBetweenSteps*1000} milliseconds
		   Number of steps: {numSteps}

		   """)

	if x: 
		iterCoils(numSteps, delayBetweenSteps, coilPins)
	else: 
	    goNum(numSteps, startState, coilPins, delayBetweenSteps)	

	closeHandle()
