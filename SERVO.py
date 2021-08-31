import RPi.GPIO as GPIO
import time

button = 16
led    = 18
servo  = 22
duty   = 0
tempo  = 0.5

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(led, GPIO.OUT)
    GPIO.setup(servo, GPIO.OUT)
    #servoMotor = GPIO.PWM(servo,50) # Note 11 is pin, 50 = 50Hz pulse
    #servoMotor.start(0)

def loop():
    while True:
        button_state = GPIO.input(button)
        if  button_state == False:
            print('Button Pressed...')
            GPIO.output(led, True)

            #global duty
            #while duty <= 1:
            servoMotor = GPIO.PWM(servo,50)
            servoMotor.start(0)

            servoMotor.ChangeDutyCycle(0)
            #duty = duty + 10
            time.sleep(tempo)

            print ("Opening 90 degrees")
            servoMotor.ChangeDutyCycle(3) ##3
            time.sleep(tempo)

            print ("Closing 0 degrees")
            servoMotor.ChangeDutyCycle(9) ##9
            time.sleep(tempo)

            servoMotor.stop()
            print ('exit loop')

        while GPIO.input(button) == False:
            time.sleep(tempo)
            #duty == 0

        else:
            GPIO.output(led, False)

def endprogram():
    GPIO.output(led, False)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print ('keyboard interrupt detected')
            endprogram()
