import RPi.GPIO as GPIO
import time
import datetime

button = 16
led    = 18
servo  = 12
tempo  = 0.5
hora_porcao1 = datetime.time(20, 28)

import array as horarios
h = horarios.array('H', [20, 16, 21])
m = horarios.array('H', [12, 15, 54])
w = 0

print ("Entrando no for")
for x in h:
    porcao = datetime.time(x , m[w])
    print (porcao)
    w+=1
    
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(servo, GPIO.OUT)

servoMotor = GPIO.PWM(servo, 50)
servoMotor.start(0)

try:
    while True:
        print ("Aguardando WHILE")
        hora_now = datetime.datetime.now().time()
        button_state = GPIO.input(button)
        
        if  hora_now >= hora_porcao1:
            print('Button Pressed...')
            GPIO.output(led, True)

            print ("90 degrees")
            print("HORA NOW", datetime.datetime.now().strftime('%H:%M'))
            print("Imprimindo hora_porcao1" ,hora_porcao1)
            servoMotor.ChangeDutyCycle(7.5)
            time.sleep(tempo)

            print ("45 degrees")
            servoMotor.ChangeDutyCycle(3.5)
            time.sleep(tempo)
        
            print ("PAUSE NO SERVO")
            servoMotor.ChangeDutyCycle(0.0)
            print ("ENTRA 60s")
            time.sleep(60)
            print ("SAI 60s")

        else:
            GPIO.output(led, False)
                        
except KeyboardInterrupt:
        print ('keyboard interrupt detected')
        servo.stop()
        GPIO.cleanup()
