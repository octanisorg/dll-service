from pyA20.gpio import gpio
from pyA20.gpio import port
from time import gmtime, strftime
import time
import requests

start_time = None
final_url = "https://racks.octanis.org/api/v1/racks/1/geography/KEY"
state = 0
channel = port.PA10
gpio.init()
gpio.setcfg(channel, gpio.INPUT)
gpio.pullup(port.PA10, gpio.PULLDOWN) 
File = open("roomlog.txt", "a")

try:
  while True:
    time.sleep(2)
    prevstate =  state

    if gpio.input(port.PA10) == 1:
       state = 1
    else:
       state = 0
    if(prevstate != state):
    	print("change detected")
        if (start_time == None):
            start_time = time.time()
        File.write(strftime("%a, %d %b %Y %H:%M:%S", gmtime()) + " MED 3 2215 is " + ("opened." if state == 1 else "closed.") + "\n")
        
    else:
        if (start_time is not None):
            elapsed_time = time.time() - start_time
            if (elapsed_time >= 60):
                start_time = None
                payload = {'accessibleToPublic': state}
            	response = requests.post(final_url, data=payload)

except KeyboardInterrupt:
    print ("Goodbye.")
