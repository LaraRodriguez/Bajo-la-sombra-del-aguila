import time 
from time import sleep
import os

if os.name == "posix":
   var = "clear"
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"
os.system(var)

election = ''

print("9:00 AM")
time.sleep(1)
print("London, August, 1939")
time.sleep(1)
print("You are in your house, peacefully, reading the newspaper and taking sips from your first tea of the morning...")
time.sleep(1)
print("The light of the morning enters in the room by a window in front of you")
time.sleep(1)
print("All of sudden, you hear the entrance's bell ringing. It seems like there's someone at the door...")
time.sleep(1)
print("What do you want to do?")
election = input()
time.sleep(1)

