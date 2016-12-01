from gpiozero import PWMLED
from time import sleep

if __name__ == '__main__':
	global estrella
	estrella = [PWMLED(13), PWMLED(16), PWMLED(19), PWMLED(20), PWMLED(21), PWMLED(26)]

	while True:
		for i in estrella:
			i.on()
			sleep(0.05)

		for i in estrella:
			i.off()
			sleep(0.05)

		for i in range(100):
			for j in estrella:
				j.value = i/100.0
			sleep(0.01)

		for i in range(100):
			for j in estrella:
				j.value = (100-i)/100.0
			sleep(0.01)

		for i in estrella:
			i.off()

		sleep(0.05)
