import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.OUT)
p = GPIO.PWM(16, 50)
p.start(7.5)
def gate_open():
   # p.ChangeDutyCycle(7.5) 
    #time.sleep(1) 
    p.ChangeDutyCycle(2.5)  
    time.sleep(1)
    p.stop()
#    GPIO.cleanup()
    
def gate_close():
    #p.ChangeDutyCycle(2.5) 
    #time.sleep(1)
    print "inside close"
    p.ChangeDutyCycle(7.0)  
    time.sleep(1)
    p.stop()
#    GPIO.cleanup()


    
    