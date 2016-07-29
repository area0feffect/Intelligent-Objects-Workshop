import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)     #Define pin 18 as an output pin


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("light")
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if str(msg.payload) == "on":
    	GPIO.output(18,1)
        time.sleep(1)      #Time delay of 1 second

    if str(msg.payload) == "off":
    	GPIO.output(18,0)   
        time.sleep(1)      #Time delay of 1 second

   	#Outputs digital HIGH signal (5V) on pin 3
    print(msg.topic+" "+str(msg.payload))

 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("23.21.151.236", 1883, 60)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
