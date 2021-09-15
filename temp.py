#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import string
import threading
import os
import smtplib

sensor=Adafruit_DHT.DHT11
dht=4

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.setwarnings(False)
 

def dht():
    print("\nInitializing DHT sensor...\n")
    time.sleep(0.5)
    while True:
        global humidity
        global temperature
        humidity, temperature=Adafruit_DHT.read_retry(11,4)
        if humidity is not None and temperature is not None:
            print('Temp:{0:0.1f}*C Humidity: {1:0.1f}%'.format(temperature,humidity))
            time.sleep(2)
            if(temperature>27):
                GPIO.setup(11,GPIO.OUT)
                print("Sprinkle Motor on")
                GPIO.output(11,GPIO.HIGH) 

                #smtpUser = 'waste2512@gmail.com'
                #smtpPass = '7411749277'


                #toAdd = 'manoj.yathindra@gmail.com'
                #fromAdd = smtpUser

                #subject = 'JallaMitra'
                #header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject
                #body = 'Your Sprinkler Motor is ON'

                #print header + '\n' + body

                #s = smtplib.SMTP('smtp.gmail.com',587)

                #s.ehlo()
                #s.starttls()
                #.ehlo()
                
                time.sleep(10)
                print("Sprinkle Motor off")
                GPIO.output(11,GPIO.LOW)
                time.sleep(300)
            
            else:
                time.sleep(2)
                print("Sprinkle Motor off")
                time.sleep(300)
        else:
            print("\nFailed to get reading...\n")
            
def soil():
    print("\nInitializing Soil Moisture Sensor...\n")
    time.sleep(2)
    while 1:
        if (GPIO.input(channel)==False):
            print("Wet Soil")
            time.sleep(300)
            
        else:
            print("Dry Soil")
            time.sleep(2)
            GPIO.setup(5,GPIO.OUT) 
            print ("Drip Motor on") 
            GPIO.output(5,GPIO.HIGH) 
            time.sleep(10) 
            print ("Drip Motor off") 
            GPIO.output(5,GPIO.LOW)
            time.sleep(300) 
   
            
print("\n====================== Starting ======================\n")
print("\nInitializing the system...\n")
time.sleep(5)
print("\nSystem is Ready\n")
time.sleep(2)
try:
    while True:
        t1=threading.Thread(target=dht)
        t2=threading.Thread(target=soil)
       
        
        
        t1.start()
        t2.start()
        
        

        t1.join()
        t2.join()
        
        
except KeyboardInterrupt:
    print("\n\nForcely Stop System\n\n")
    time.sleep(4)
    GPIO.cleanup()
    time.sleep(1)


