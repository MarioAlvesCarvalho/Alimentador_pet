import RPi.GPIO as GPIO
import time

button = 16
led    = 18
servo  = 12
tempo  = 0.5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(servo, GPIO.OUT)

servoMotor = GPIO.PWM(servo, 50)
servoMotor.start(0)

try:
    while True:
        button_state = GPIO.input(button)
        if  button_state == False:
            print('Button Pressed...')
            GPIO.output(led, True)

            print (" 180 degrees")
            servoMotor.ChangeDutyCycle(12.0)
            time.sleep(tempo)

            print ("90 degrees")
            servoMotor.ChangeDutyCycle(7.5)
            time.sleep(tempo)

            print ("45 degrees")
            servoMotor.ChangeDutyCycle(3.5)
            time.sleep(tempo)
            
            print ("PARANDO SERVO")
            servoMotor.ChangeDutyCycle(0.0)
            
      else:
           GPIO.output(led, False)
          
except KeyboardInterrupt:
        print ('keyboard interrupt detected')
        servo.stop()
        GPIO.cleanup()
        
