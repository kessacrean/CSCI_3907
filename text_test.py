import smtplib
from sense_hat import SenseHat
import time

sense = SenseHat()
 
CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}
 
EMAIL = "isaac.bilsel@gmail.com"
PASSWORD = "wnrboxdwjkjtqqab"

MAX_HUMIDITY = 80
MIN_HUMIDITY = 40

MAX_TEMP = 25
MIN_TEMP = 15
 
def send_message(phone_number, carrier, message):
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
 
    server.sendmail(auth[0], recipient, message)
 

if __name__ == "__main__":
    # if len(sys.argv) < 4:
        # print(f"Usage: python3 {sys.argv[0]} <PHONE_NUMBER> <CARRIER> <MESSAGE>")
        # sys.exit(0)
    while(true):
        
        t = sense.get_temperature()
            p = sense.get_pressure()
            h = sense.get_humidity()
            
            t = round(t,1)
            p = round(p,1)
            h = round(h,1)
            
            
            msg = "Temp = %s C, Pressure = %s mbar, Humidity =%s" % (t, p, h)
            time.sleep(5)
 

    phone_number = "7743647599"
    carrier = "verizon"
    message = "Hey, I'm texting you to test my code"
 
    send_message(phone_number, carrier, message)
    