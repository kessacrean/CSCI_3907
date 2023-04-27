from flask import Flask, render_template
import logging
import datetime
import smtplib
import time

CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}
 
EMAIL = "isaac.bilsel@gmail.com"
PASSWORD = "wnrboxdwjkjtqqab"

def send_message(phone_number, carrier, message):
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
 
    server.sendmail(auth[0], recipient, message)
 

# ======== Initialize Logging ===========

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

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host="0.0.0.0", debug=True)
    

    # !! Insert logic to test if tank is empty
    # Send text message
    phone_number = "7743647599"
    carrier = "verizon"
    message = "Hey, I'm texting you to test my code"
 
    send_message(phone_number, carrier, message)