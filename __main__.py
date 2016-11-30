from gpiozero import PWMLED
from time import sleep

if __name__ == '__main__':
	global estrella
	estrella = [PWMLED(13), PWMLED(16), PWMLED(19), PWMLED(20), PWMLED(21), PWMLED(26)]

	for i in estrella:
		i.on()

	while True:
		print 'blip'
		sleep(1)