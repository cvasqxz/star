from gpiozero import PWMLED
from time import sleep

if __name__ == '__main__':
	global estrella
	estrella = [PWMLED(13), PWMLED(16), PWMLED(19), PWMLED(20), PWMLED(21), PWMLED(26)]

	while True:
		for i in estrella:
			i.on()
			sleep(1)

		for i in estrella:
			i.off()
			sleep(1)