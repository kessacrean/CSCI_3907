# Final Project Code: Plant Mate 
# Authors: Isaac Bilsel and Kessa Crean
# ECE Department GWU
# CSCI 3907: Intro to IoT and Edge Computing 
# Spring 2023
# Adapted from code given by SunFounder and from code written by Dr. Bulusu for CSCI 3907

# ====================================================================
# IMPORT MODULES =====================================================
#from flask import Flask, render_template
import logging
import datetime
import smtplib
#import PCF8591 as ADC
import time
import math
import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt
import csv #https://docs.python.org/3/library/csv.html

# =====================================================================
# INTIALIZE GPIO-PINS =================================================

TRIG = 16 #Ultrasound projector
ECHO = 15 #Ultrasound Receiver
RedLED = 12 #Red LED
GreenLED = 11 #Green LED
RainSensor = 17 #Raindrop sensor
Pump = 18 #Water pump control pin

# =====================================================================
# INTIALIZE VARIABLES =================================================

timeElapsed = 0
threshold = 25 # distance in centimeters
T = np.array([]) #ultrasonic array: time
D = np.array([]) #ultrasonic array: distance

CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}

EMAIL = "isaac.bilsel@gmail.com"
PASSWORD = "wnrboxdwjkjtqqab"


# ====================================================================
# FUNCTIONS ==========================================================

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(RedLED, GPIO.OUT)
    GPIO.setup(GreenLED, GPIO.OUT)
    GPIO.setup(RainSensor, GPIO.IN)
    GPIO.setup(Pump, GPIO.OUT)
    
    
def send_message(phone_number, carrier, message):
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
 
    server.sendmail(auth[0], recipient, message)


# Function given by SunFounder to calculate distance from sensor
def distance():
    GPIO.output(TRIG, 0)
    time.sleep(0.000002)
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        time1 = time.time()
        
    while GPIO.input(ECHO) == 1:
        time2 = time.time()

    during = time2 - time1
    return during * 340 / 2 * 100 #Returns distance in cm


# Gather sensor data and print data on terminal for 10 seconds
def loop():

        global timeElapsed, T, D
        
        while timeElapsed <= 10:
            # writes the time elapsed and distance measured
            # Turns LED to RED if object within 'threshold' distance
            dist = distance()

            print(timeElapsed, 's', dist, 'cm')
            print('')

            time.sleep(0.1)
            timeElapsed = timeElapsed+0.1
            
            D = np.append(D, dist)
            T = np.append(T, timeElapsed)
            
            global threshold
            if(dist<threshold):
                GPIO.output(11, GPIO.LOW)
                GPIO.output(12, GPIO.HIGH)
            else:
                GPIO.output(11, GPIO.HIGH)
                GPIO.output(12, GPIO.LOW)


def destroy():
    GPIO.cleanup()


# generates a plot of distance (cm) vs time (s) for ultrasonic data
def plotting():
    plt.plot(T,D)
    plt.title('Water Level Graph')
    plt.xlabel('Time <seconds>')
    plt.ylabel('Distance <Centimeters> ')
    plt.grid(True)
    plt.show()

# ====================================================================
# INTIALIZE LOGGING ==================================================

# Global logging configuration
logging.basicConfig(level=logging.WARNING)  

# Logger for this module
logger = logging.getLogger('main')

# Debugging for this file.
logger.setLevel(logging.INFO) 


# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def start():
    return render_template('initial_screen.html')
 
@app.route('/high_moisture')
def high_moisture():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    
    #  add plant statistics data here
    # We can try to graph these as well
    
    # Water Level:
    water_level = 0
    if (water_level < 0):
        pump_msg = 'Water Level Low'
    else:
        pump_msg = 'Water Level Stable'
        
    # Moisture Level:
    moisture_level = 0
    if (moisture_level < 0):
        moisture_msg = 'Low Soil Moisture'
    else:
        moisture_msg = 'Soil Moisture is Stable'
    
    templateData = {
        'time': timeString,
        'moisture_msg': moisture_msg,
        'moisture_level': moisture_level,
        'pump_msg': pump_msg,
        'water_level': water_level
        
    }
    return render_template('index.html', **templateData)

@app.route('/low_moisture')
def low_moisture():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    
    #  add plant statistics data here
    # We can try to graph these as well
    
    # Water Level:
    water_level = 0
    if (water_level < 0):
        pump_msg = 'Water Level Low'
    else:
        pump_msg = 'Water Level Stable'
        
    # Moisture Level:
    moisture_level = 0
    if (moisture_level < 0):
        moisture_msg = 'Low Soil Moisture'
    else:
        moisture_msg = 'Soil Moisture is Stable'
    
    templateData = {
        'time': timeString,
        'moisture_msg': moisture_msg,
        'moisture_level': moisture_level,
        'pump_msg': pump_msg,
        'water_level': water_level
        
    }
    return render_template('index.html', **templateData)

@app.route('/medium_moisture')
def medium_moisture():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    
    #  add plant statistics data here
    # We can try to graph these as well
    
    # Water Level:
    water_level = 0
    if (water_level < 0):
        pump_msg = 'Water Level Low'
    else:
        pump_msg = 'Water Level Stable'
        
    # Moisture Level:
    moisture_level = 0
    if (moisture_level < 0):
        moisture_msg = 'Low Soil Moisture'
    else:
        moisture_msg = 'Soil Moisture is Stable'
    
    templateData = {
        'time': timeString,
        'moisture_msg': moisture_msg,
        'moisture_level': moisture_level,
        'pump_msg': pump_msg,
        'water_level': water_level
        
    }
    return render_template('index.html', **templateData)

# ====================================================================
# MAIN DRIVER FUNCTION ===============================================
if __name__ == '__main__':

    try:

        # run() method of Flask class runs the application on the local development server.
        app.run(host="0.0.0.0", debug=True)
        
        setup()

        # !! Insert logic to test if tank is empty
        # Send text message
        # phone_number = "7743647599"
        # carrier = "verizon"
        # message = "Hey, I'm texting you to test my code"
        # send_message(phone_number, carrier, message)

        loop()
        plotting()

    except KeyboardInterrupt: #Quits out on ctrl+c
        destroy()
    finally:
	    destroy()