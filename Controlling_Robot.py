from bottle import run,route
import time
import sys
import RPi.GPIO as GPIO
from threading import Thread
#from Bluetin_Echo import Echo

mode=GPIO.getmode()

GPIO.cleanup()

Leftin1=18
Leftin2=16
LeftPwm=36
sleeptime=1

Rightin1=31
Rightin2=33

RightPwm=32

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Leftin1, GPIO.OUT)
GPIO.setup(Leftin2, GPIO.OUT)
GPIO.setup(LeftPwm, GPIO.OUT)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Rightin1, GPIO.OUT)
GPIO.setup(Rightin2, GPIO.OUT)
GPIO.setup(RightPwm, GPIO.OUT)

global pulse_start
global pulse_end

TRIG = 11

ECHO = 13

GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)

# Initialise Sensor with pins, speed of sound.
#speed_of_sound = 315
#echo = Echo(TRIGGER_PIN, ECHO_PIN, speed_of_sound)


returnVal='NoObstacle'
delayy1=.3
delayy2=.6
delayy3=.9
delayy4=1.2
delayy5=1.5


#def Ultrasonicc():
#    GPIO.output(TRIG, True)

#    time.sleep(0.00001)

#    GPIO.output(TRIG, False)

#    while GPIO.input(ECHO)==0:

#      pulse_start = time.time()

#    while GPIO.input(ECHO)==1:

#      pulse_end = time.time()

 #   pulse_duration = pulse_end - pulse_start

#    distance = pulse_duration * 17150
#    distance = round(distance, 2)

#    if distance < 400:      #Check whether the distance is within range

#        print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
#        global returnVal
#        returnVal='Obstacle'
#    else:
#        print "Out Of Range"                   #display out of range
#        global returnVal
#        returnVal='NoObstacle'

#t=Thread(target=Ultrasonicc)
#t.daemon=True
#t.start()

def Stop():
    
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)
    
    GPIO.output(Leftin1, GPIO.LOW)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.LOW)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(.5)

    


def Straight():

    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)

    GPIO.output(Leftin1, GPIO.HIGH)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.HIGH)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(.8)

    GPIO.cleanup()




    ########## LEFT ON RIGHT OFF DELAYS

def one():
    
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.HIGH)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.LOW)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy1)

    GPIO.cleanup()    

    Stop()
    Straight()


def two():
    
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.HIGH)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.LOW)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy2)

    GPIO.cleanup()    

    Stop()
    Straight()


def three():
    
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.HIGH)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.LOW)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy3)

    GPIO.cleanup()    

    Stop()
    Straight()


def four():
    
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.HIGH)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.LOW)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy4)

    GPIO.cleanup()    

    Stop()
    Straight()


    ########## RIGHT ON LEFT OFF DELAYS

def five():
    
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.LOW)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.HIGH)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy1)

    GPIO.cleanup()    

    Stop()
    Straight()


def six():
    
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.LOW)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.HIGH)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy2)

    GPIO.cleanup()    

    Stop()
    Straight()


def seven():
    
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.LOW)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.HIGH)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy3)

    GPIO.cleanup()    

    Stop()
    Straight()


def eight():
    
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.LOW)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.HIGH)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy4)

    GPIO.cleanup()    

    Stop()
    Straight()

def Reverse():

    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)

    GPIO.output(Leftin1, GPIO.LOW)
    GPIO.output(Leftin2, GPIO.HIGH)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.LOW)
    GPIO.output(Rightin2, GPIO.HIGH)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(.8)

    GPIO.cleanup()    

#####################################

def Obstaclee():
    GPIO.setmode(GPIO.BOARD)                     #Set GPIO pin numbering 

    TRIG = 37                                  #Associate pin 23 to TRIG
    ECHO = 35                                  #Associate pin 24 to ECHO

    print "Distance measurement in progress"

    GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
    GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in

    

    GPIO.output(TRIG, False)                 #Set TRIG as LOW
    print "Waitng For Sensor To Settle"
    time.sleep(2)                            #Delay of 2 seconds

    GPIO.output(TRIG, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(TRIG, False)                 #Set TRIG as LOW

    while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
        pulse_start = time.time()              #Saves the last known time of LOW pulse

    while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
        pulse_end = time.time()                #Saves the last known time of HIGH pulse 

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
    distance = round(distance, 2)            #Round to two decimal points

    if distance > 2 and distance < 400:      #Check whether the distance is within range
        print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
    else:
        print "Out Of Range"                   #display out of range

      

    if(distance<25):
    ##put ultrasonic code
    ##if detected then
        print("Obstacle detected")
        Stop()
        Reverse()
        two()
        Stop()
        six()
        Stop()
        six()
        

    ##else keep the robot straight
    else:
        print("keep moving no obtacle is detected")
#GPIO.cleanup() 
    
@route('/')
def index():
    print("reached here at 0")
    time.sleep(1)
    print("timer ended")
    time.sleep(1)
    return{returnVal}


@route('/1')
def docss():
    print("reached here at 1")
    print("Right + down")
    Obstaclee()
    one()
    Obstaclee()
    return{returnVal}


@route('/2')
def docss():
    print("reached here at 2")
    print("down only")
    Obstaclee()
    two()
    Obstaclee()
    return{returnVal}

@route('/3')
def docss():
    print("reached here at 3")
    print("Left + down")
    Obstaclee()
    three()
    Obstaclee()
    return{returnVal}



@route('/4')
def docss():
    print("reached here at 4")
    Obstaclee()
    four()
    Obstaclee()
    return{returnVal}



@route('/5')
def docss():
    print("reached here at 5")
    print("left + up")

    Obstaclee()

    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.LOW)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.HIGH)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy3)

    GPIO.cleanup()    

    Stop()
    Straight()

    Obstaclee()
    #return{returnVal}
    print returnVal
    return{returnVal}


@route('/6')
def docss():
    print("reached here at 6")
    print("up only")

    Obstaclee()    
    six()

    Obstaclee()
    print("timer ended")
    time.sleep(1)
    return{returnVal}



@route('/7')
def docss():
    print("reached here at 7")
    print("right + up")
    Obstaclee()
    five()
    Obstaclee()
    return{returnVal}


@route('/0')
def docss():
    print("reached here at 0")
    print("right only")
    Obstaclee()
    Stop()
    Straight()
    Stop()
    Obstaclee()
    return{returnVal}

## Currrent is zero with previous any

@route('/00')
def docss():
    print("reached here at 00")
    Obstaclee()
    Straight()
    Stop()
    Obstaclee()
    return{returnVal}

@route('/10')

def docss():

    Obstaclee()
    
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.LOW)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.HIGH)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy2)

    GPIO.cleanup()    

    Stop()
    Straight()

    Obstaclee()
    return(returnVal)



@route('/20')
def docss():
    print("reached here at 20")

    Obstaclee()
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.LOW)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.HIGH)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy2)

    GPIO.cleanup()    

    Stop()
    Straight()

    Obstaclee()
    return{returnVal}

@route('/30')
def docss():
    print("reached here at 30")

    Obstaclee()
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.HIGH)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.LOW)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy3)

    GPIO.cleanup()    

    Stop()
    Straight()
    Obstaclee()

    return{returnVal}

@route('/40')
def docss():
    print("reached here at 40")

    Obstaclee()
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.LOW)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.HIGH)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy4)

    GPIO.cleanup()    

    Stop()
    Straight()

    Obstaclee()

    return{returnVal}

@route('/50')
def docss():
    print("reached here at 50")

    Obstaclee()
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.HIGH)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.LOW)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy3)

    GPIO.cleanup()    

    Stop()
    Straight()

    Obstaclee()
    return{returnVal}

@route('/60')
def docss():
    print("reached here at 60")

    Obstaclee()
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.HIGH)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.HIGH)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy2)

    GPIO.cleanup()    

    Stop()
    Straight()


    Obstaclee()
    return{returnVal}

@route('/70')
def docss():
    print("reached here at 70")

    Obstaclee()
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.HIGH)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.LOW)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy1)

    GPIO.cleanup()    

    Stop()
    Straight()

    Obstaclee()
    return{returnVal}



## Currrent is 1 with previous any

@route('/01')
def docss():
    print("reached here at 01")
    
    Obstaclee()
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.HIGH)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.LOW)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy1)

    GPIO.cleanup()    

    Stop()
    Straight()

    Obstaclee()
    return{returnVal}


@route('/11')
def docss():
    
    print("reached here at 11")
    print("Go straight")
    print("right + up")

    Obstaclee()
    Stop()
    Straight()

    Obstaclee()
    return{returnVal}



@route('/21')
def docss():
    print("reached here at 21")
    print("Turn left a bit")

    
    Obstaclee()
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.LOW)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.HIGH)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy1)

    GPIO.cleanup()    

    Stop()
    Straight()

    Obstaclee()
    return{returnVal}


@route('/31')
def docss():
    print("reached here at 31")

    Obstaclee()
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.HIGH)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.LOW)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy3)

    GPIO.cleanup()    

    Stop()
    Straight()

    Obstaclee()
    return{returnVal}

@route('/41')
def docss():
    print("reached here at 41")

    Obstaclee()
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.LOW)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.HIGH)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy3)

    GPIO.cleanup()    

    Stop()
    Straight()

    Obstaclee()
    return{returnVal}

@route('/51')
def docss():
    print("reached here at 51")

    Obstaclee()
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.LOW)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.HIGH)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy4)

    GPIO.cleanup()    

    Stop()
    Straight()

    Obstaclee()
    return{returnVal}    

@route('/61')
def docss():
    print("reached here at 61")

    Obstaclee()
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.HIGH)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.LOW)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy3)

    GPIO.cleanup()    

    Stop()
    Straight()
    Obstaclee()
    return{returnVal}

@route('/71')
def docss():
    print("reached here at 71")

    Obstaclee()
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.HIGH)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.LOW)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy2)

    GPIO.cleanup()    

    Stop()
    Straight()
    Obstaclee()

    return{returnVal}


## Currrent is 2 with previous any

@route('/02')
def docss():
    print("reached here at 02")
    Obstaclee()
    two()
    Obstaclee()
    return{returnVal}

@route('/12')
def docss():
    print("reached here at 12")
    Obstaclee()
    one()
    Obstaclee()
    return{returnVal}


@route('/22')
def docss():
    print("reached here at 22")
    Obstaclee()
    Stop()

    Straight()
    #return{'NoObstacle'}
    Obstaclee()
    return{returnVal}


@route('/32')
def docss():
    print("reached here at 32")
    Obstaclee()
    five()
    Obstaclee()
    return{returnVal}

@route('/42')
def docss():
    print("reached here at 42")
    Obstaclee()
    five()
    Obstaclee()
    return{returnVal}

@route('/52')
def docss():
    print("reached here at 52")
    Obstaclee()
    seven()
    Obstaclee()
    return{returnVal}

@route('/62')
def docss():
    print("reached here at 62")
    Obstaclee()
    four()
    Obstaclee()
    return{returnVal}

@route('/72')
def docss():
    print("reached here at 72")
    Obstaclee()
    three()
    Obstaclee()
    return{returnVal}

## Currrent is 3 with previous any

@route('/03')
def docss():
    print("reached here at 03")
    Obstaclee()
    one()
    Obstaclee()
    return{returnVal}

@route('/13')
def docss():
    print("reached here at 13")
    Obstaclee()
    three()
    Obstaclee()
    return{returnVal}

@route('/23')
def docss():
    print("reached here at 23")
    Obstaclee()
    one()
    Obstaclee() 
    return{returnVal}

@route('/33')
def docss():
    print("reached here at 33")
    Obstaclee()
    Stop()
    Straight()
    Obstaclee()
    return{returnVal}

@route('/43')
def docss():
    print("reached here at 43")
    Obstaclee()
    five()
    Obstaclee() 
    return{returnVal}

@route('/53')
def docss():
    print("reached here at 53")
    Obstaclee()
    six()
    Obstaclee()
    return{returnVal}

@route('/63')
def docss():
    print("reached here at 63")
    Obstaclee()
    six()
    Obstaclee()
    return{returnVal}

@route('/73')
def docss():
    print("reached here at 73")
    Obstaclee()
    four()
    Obstaclee()    
    return{returnVal}


## Currrent is 4 with previous any

@route('/04')
def docss():
    print("reached here at 04")
    Obstaclee()
    four()
    Obstaclee()
    return{returnVal}

@route('/14')
def docss():
    print("reached here at 14")
    Obstaclee()
    three()
    Obstaclee()
    return{returnVal}

@route('/24')
def docss():
    print("reached here at 24")
    Obstaclee()
    two()
    Obstaclee()
    return{returnVal}

@route('/34')
def docss():
    print("reached here at 34")
    Obstaclee()
    one()
    Obstaclee()
    return{returnVal}

@route('/44')
def docss():
    print("reached here at 44")
    Obstaclee()
    Stop()
    Straight()
    Obstaclee()
    return{returnVal}

@route('/54')
def docss():
    print("reached here at 54")
    Obstaclee()
    Leftin1=18
    Leftin2=16
    LeftPwm=36
    sleeptime=1

    Rightin1=31
    Rightin2=33
    RightPwm=32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Leftin1, GPIO.OUT)
    GPIO.setup(Leftin2, GPIO.OUT)
    GPIO.setup(LeftPwm, GPIO.OUT)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rightin1, GPIO.OUT)
    GPIO.setup(Rightin2, GPIO.OUT)
    GPIO.setup(RightPwm, GPIO.OUT)    
    GPIO.output(Leftin1, GPIO.HIGH)
    GPIO.output(Leftin2, GPIO.LOW)
    print("Left moving Forward")
    pwm1 = GPIO.PWM(LeftPwm, 100)   # Initialize PWM
    pwm1.start(50)

    GPIO.output(Rightin1, GPIO.LOW)
    GPIO.output(Rightin2, GPIO.LOW)
    print("Right moving Forward")
    pwm2 = GPIO.PWM(RightPwm, 100)   # Initialize PWM
    pwm2.start(50)

    time.sleep(delayy2)

    GPIO.cleanup()    

    Stop()
    Straight()
    Obstaclee()
    
    #return{returnVal}
    return{returnVal}

@route('/64')
def docss():
    print("reached here at 64")
    Obstaclee()
    six()
    Obstaclee()
    return{returnVal}

@route('/74')
def docss():
    print("reached here at 74")
    Obstaclee()
    seven()
    Obstaclee()
    return{returnVal}


## Currrent is 4 with previous any

@route('/05')
def docss():
    print("reached here at 05")
    Obstaclee()
    seven()
    Obstaclee()
    return{returnVal}

@route('/15')
def docss():
    print("reached here at 15")
    Obstaclee()
    eight()
    Obstaclee()
    return{returnVal}

@route('/25')
def docss():
    print("reached here at 25")

    Obstaclee()
    three()
    Obstaclee()
    return{returnVal}

@route('/35')
def docss():
    print("reached here at 35")
    Obstaclee()
    two()
    Obstaclee()
    return{returnVal}

@route('/45')
def docss():
    print("reached here at 45")
    Obstaclee()
    one()
    Obstaclee()
    return{returnVal}

@route('/55')
def docss():
    print("reached here at 55")
    Obstaclee()
    Stop()
    Straight()
    Obstaclee()
    return{returnVal}

@route('/65')
def docss():
    print("reached here at 65")
    Obstaclee()
    five()
    Obstaclee()
    return{returnVal}

@route('/75')
def docss():
    print("reached here at 75")
    Obstaclee()
    two()
    Obstaclee()
    return{returnVal}


## Currrent is 6 with previous any

@route('/06')
def docss():
    print("reached here at 06")
    Obstaclee()
    two()
    Obstaclee()
    return{returnVal}

@route('/16')
def docss():
    print("reached here at 16")
    Obstaclee()
    seven()
    Obstaclee()
    return{returnVal}

@route('/26')
def docss():
    print("reached here at 26")
    Obstaclee()
    four()
    Obstaclee()
    return{returnVal}

@route('/36')
def docss():
    print("reached here at 36")
    Obstaclee()
    two()
    Obstaclee()
    return{returnVal}

@route('/46')
def docss():
    print("reached here at 46")
    Obstaclee()
    two()
    Obstaclee()
    return{returnVal}

@route('/56')
def docss():
    print("reached here at 56")
    Obstaclee()
    one()
    Obstaclee()
    return{returnVal}

@route('/66')
def docss():
    print("reached here at 66")

    Obstaclee()
    Stop()
    Straight()
    Obstaclee()
    return{returnVal}


@route('/76')
def docss():
    print("reached here at 76")
    Obstaclee()
    five()
    Obstaclee()
    return{returnVal}




## Currrent is 7 with previous any

@route('/07')
def docss():
    print("reached here at 07")
    Obstaclee()
    five()
    Obstaclee()
    return{returnVal}


@route('/17')
def docss():
    print("reached here at 17")
    Obstaclee()
    six()
    Obstaclee()
    return{returnVal}


@route('/27')
def docss():
    print("reached here at 27")
    Obstaclee()
    seven()
    Obstaclee()
    return{returnVal}

@route('/37')
def docss():
    print("reached here at 37")
    Obstaclee()
    eight()
    Obstaclee()
    return{returnVal}

@route('/47')
def docss():
    print("reached here at 47")
    Obstaclee()
    three()
    Obstaclee()
    return{returnVal}

@route('/57')
def docss():
    print("reached here at 57")
    Obstaclee()
    two()
    Obstaclee()
    return{returnVal}

@route('/67')
def docss():
    print("reached here at 67")
    Obstaclee()
    one()
    Obstaclee()
    return{returnVal}

@route('/77')
def docss():
    print("reached here at 77")
    Obstaclee()
    Stop()
    Straight()
    Obstaclee()
    return{returnVal}




run(host='0.0.0.0',port=8080,debug=True)
GPIO.cleanup()