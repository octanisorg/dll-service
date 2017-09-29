from pyA20.gpio import gpio
from pyA20.gpio import port
import time
import requests


state = 0
channel = port.PA10
gpio.init()
gpio.setcfg(channel, gpio.INPUT)
gpio.pullup(port.PA10, gpio.PULLDOWN) 

try:
  while True:
    time.sleep(1)
    prevstate =  state
    if gpio.input(port.PA10) == 1:
	state = 1
    else:
	state = 0
    if(prevstate != state):
	print("change detected")
	final_url = "https://racks.octanis.org/api/v1/racks/1/geography/KEY"
	payload = {'accessibleToPublic': state}
	response = requests.post(final_url, data=payload)


except KeyboardInterrupt:
    print ("Goodbye.")


