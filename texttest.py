import smtplib

EMAIL = "isaac.bilsel@gmail.com"
PASSWORD = "wnrboxdwjkjtqqab"

PHONE_NUMBER = "7743647599"
CARRIER = "verizon"

MAX_HUMIDITY = 80
MIN_HUMIDITY = 40

MAX_TEMP = 25
MIN_TEMP = 15
 


def send_message(phone_number, carrier, message):
    recipient = phone_number + carrier
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
 
    server.sendmail(auth[0], recipient, message)

text = 'Environment is stable'
send_message(PHONE_NUMBER, CARRIER, text)