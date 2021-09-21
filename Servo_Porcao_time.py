import RPi.GPIO as GPIO
import time
import datetime

button = 16
led    = 18
servo  = 12
tempo  = 0.5
hora_porcao1 = datetime.time(19, 55)
entrega_porcao1 = False
meia_noite =  datetime.time(19, 56)
#meia_noite2 =  datetime.time(21, 37)

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
                #formatted_date1 = time.strptime(hora_now, "%H:%M")
                #formatted_date2 = time.strftime(hora_porcao1, "%H:%M")
        button_state = GPIO.input(button)
        if hora_now == meia_noite:
            entrega_porcao1 = False
        #if  button_state == False:
        #if  'datetime.datetime' >= hora1 :
        if  hora_now >= hora_porcao1:
            entrega_porcao1 = True
            
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
