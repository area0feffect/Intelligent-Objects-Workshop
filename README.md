<pre>
#      _   ___ ___   _      ___  ___   ___ ___ ___ ___ ___ _____ 
#     /_\ | _ | __| /_\    / _ \| __| | __| __| __| __/ __|_   _|
#    / _ \|   | _| / _ \  | (_) | _|  | _|| _|| _|| _| (__  | |  
#   /_/ \_|_|_|___/_/ \_\  \___/|_|   |___|_| |_| |___\___| |_|  
#
#    I N T E L L I G E N T    O B J E C T S    W O R K S H O P
#
</pre>


<br/>
###.. -. - . .-.. .-.. .. --. . -. - / --- -... .--- . -.-. - ...
###### This workshop is about the relationship between humans, machines and their ways of communication. What is beyond the internet of things? What makes things intelligent?

######We'll be mapping and building out our own networks of Raspberry Pi and establishing a custom messaging protocol between them. Humans are a key component and will facilitate the process 

<br/>
#Build Guide
* A network of Raspberry Pi, Sensors and Humans.

<br/>

##Hardware
 * Buttons, represents human input. Overrides. Lets say you have an intelligent system, but it's malfunctioning. The human element is always there.
 * Photocell, represents sensing, environmental input. Uncontrollable; we must design our system in a way to account for variability.
 * Network & Protocol, communication between the nodes. Humans are also a node.
 * The language we choose. What protocol can humans and machines both understand.
	- Moorse Code
	- Light


<br/>

####Led Setup
* 1 LED
* 220ohm Resistor
* Wires

![Led Yo!](http://i.imgur.com/71mpq7j.png)

<br/>
####A Button!!
* 1 LED
* 10k Resistor
* Wires

![Button](http://i.imgur.com/8ifGKat.png)

<br/>
<br/>

##Software
###Installating MQTT on OSX
##### 1. Install MQTT
<pre>
pip install paho-mqtt
</pre>

##### 2. Run as a virtual environment.
<pre>
virtualenv paho-mqtt
</pre>

##### 3. Active and install.
<pre>
source paho-mqtt/bin/activate
brew install mosquitto
</pre>

##### 4. Send a message!
<pre>
mosquitto_sub -h xx.xx.xxx.xxx -t topic
</pre>

<br/>

###Installing MQTT on Raspberry Pi

#####Do a bunch of commands.
<pre>
wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key
sudo apt-key add mosquitto-repo.gpg.key
cd /etc/apt/sources.list.d/
sudo wget http://repo.mosquitto.org/debian/mosquitto-wheezy.list
sudo apt-cache search mosquitto
sudo apt-get install mosquitto python-mosquitto mosquitto-clients
</pre>

#####Open port 1883
<pre>
sudo iptables -A INPUT -p tcp -m tcp --dport 1883 -j ACCEPT
</pre>

##### Use MQTT in a python script
<pre>
sudo apt-get install python-pip
sudo pip install paho-mqtt
</pre>

<br/>


##Messages Examples
#####Testing via command line
<pre>
mosquitto_sub -d -t hello/world
mosquitto_pub -d -t hello/world -m "Hello World"
mosquitto_sub -h YOUR_HOST_IP_ADDRESS -d -t hello/world
</pre>

<br/>
###breaking it down....
This example subscribes to the channel 'topic'. 
<pre>
mosquitto_sub -d -t topic
</pre>

This one subscribes to the channel 'AoE' and publishes the message "Testing 123"
<pre>
mosquitto_pub -h xx.xx.xxx.xxx -t AoE -m "Testing 123"
</pre>

This one subscribes to the channel 'NewLab' and publishes the message "Hi Bruno"

<pre>
mosquitto_pub -h xx.xx.xxx.xxx -t topic -m "Hi Bruno"
</pre>
