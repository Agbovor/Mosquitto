import paho.mqtt.client as mqtt
import time
school=input("Enter school name")
name=input("Enter name")
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:
        print("Connection failed")

Connected = False  # global variable for the state of the connection

client = mqtt.Client()
client.on_connect = on_connect
client.connect("2.tcp.eu.ngrok.io", 17913, 60)
client.loop_start()  # start the loop

while Connected != True:  # Wait for connection
        time.sleep(0.1)
        print("retrying")

# Join_Name = input("Enter Join Name: ")
# client.publish("glbcd", f'{Join_Name} Joined')

try:
    while True:
        message = input('Your message: ')
        message = school + "/" + name +":"+ message
        client.publish("glblcd", message)

except KeyboardInterrupt:
        client.disconnect()
        client.loop_stop()

