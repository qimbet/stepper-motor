How to use: 

These scripts are python; intended to enable control of a stepper motor through a raspberry pi. 

These scripts use the lgpio library:

> pip install lgpio
> sudo apt update
> sudo apt install lgpio



Wire the stepper motor up according to its known voltages. Stepper motors are rugged; they can tolerate a range if you are uncertain. The order of the pins does not matter.

At the time of development of this script, we used a ULN2003A transistor array as a motor driver. The installation was such: 

	
						
					  					  +----------------------+
	 	 +-------------------+            |      ULN2003A        |
         |   Raspberry Pi    |            |   (transistor array) | 
         |                   |            |                      | 
         |   GPIO17 ---------+----------->| IN1   OUT1 ----------+----> HV Load
         |   GPIO18 ---------+----------->| IN2   OUT2 ----------+----> HV Load
         |   GPIO27 ---------+----------->| IN3   OUT3 ----------+----> HV Load
         |   GPIO22 ---------+----------->| IN4   OUT4 ----------+----> HV Load
         |                   |            |                      | 
         |          GND -----+----------->| GND                  |
         +-------------------+            | COM (to HV+)         |
                                          +-----------+----------+
                                                      |
                                                      |
                                                +-----+------+
                                                |  +14VDC    |
                                                |  Supply    |
                                                +------------+



Run the script 'motor_debug.py' to identify the proper pin sequence. 
You can keep your existing motor wiring; simply copy the 'successful' pin sequence from 'motor_debug.py' and use it to update the list coilPins in controller.py.

Done!
