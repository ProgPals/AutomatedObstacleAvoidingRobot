from machine import Pin, PWM  # importing PIN and PWM
import time  # importing time
import utime

# Defining motor pins
In1 = Pin(0, Pin.OUT)
In2 = Pin(1, Pin.OUT)
In3 = Pin(2, Pin.OUT)
In4 = Pin(3, Pin.OUT)
# Defining enable pins and PWM object
# Defining  Trigger and Echo pins
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

# Defining  Servo pin and PWM object
servoPin = Pin(0)
servo = PWM(servoPin)
duty_cycle = 0  # Defining and initializing duty cycle PWM

# Defining frequency for servo and enable pins
servo.freq(50)
EN_A.freq(1000)
EN_B.freq(1000)

# Setting maximum duty cycle for maximum speed
EN_A.duty_u16(65025)
EN_B.duty_u16(65025)

# Forward


def move_forward():
    In1.high()
    In2.low()
    In3.high()
    In4.low()

# Backward


def move_backward():
    In1.low()
    In2.high()
    In3.low()
    In4.high()

# Turn Right


def turn_right():
    In1.low()
    In2.low()
    In3.low()
    In4.high()

# Turn Left


def turn_left():
    In1.low()
    In2.high()
    In3.low()
    In4.low()

# Stop


def stop():
    In1.low()
    In2.low()
    In3.low()
    In4.low()

# Defining function to get distance from ultrasonic sensor


def get_distance():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    dist = (timepassed * 0.0343) / 2
    return dist

# Defining function to set servo angle


def setservo(angle):
    duty_cycle = int(angle*(7803-1950)/180) + 1950
    servo.duty_u16(duty_cycle)


setservo(90)

while True:
    distance = get_distance()  # Getting distance in cm

    # Defining direction based on conditions
    if distance < 15:
        stop()
        move_backward()
        time.sleep(1)
        stop()
        time.sleep(0.5)
        setservo(30)  # Servo angle to 30 degree
        time.sleep(1)
        right_distance = get_distance()
        # print(right_distance)
        time.sleep(0.5)
        setservo(150)  # Servo angle to 150 degree
        time.sleep(1)
        left_distance = get_distance()
        # print(left_distance)
        time.sleep(0.5)
        setservo(90)

        if right_distance > left_distance:
            turn_right()
            time.sleep(2)
            stop()
        else:
            turn_left()
            time.sleep(2)
            stop()
    else:
        move_forward()

    time.sleep(0.5)
