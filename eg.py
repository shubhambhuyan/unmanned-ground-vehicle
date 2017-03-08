# Imports
import webiopi
import time
import subprocess

# Enable debug output
webiopi.setDebug()

# Retrieve GPIO lib
GPIO = webiopi.GPIO

# Left motor GPIOs
L1=4  # H-Bridge 1
L2=17 # H-Bridge 2
#LS=25 # H-Bridge 1,2EN

# Right motor GPIOs
R1=19 # H-Bridge 3
R2=21 # H-Bridge 4
#RS=11  H-Bridge 3,4EN

#cam motors GPIOs
C1=5
C2=6

# Called by WebIOPi at script loading
def setup():
    webiopi.debug("Script with macros - Setup")
    # Setup GPIOs
    GPIO.setFunction(L1, GPIO.OUT)
    GPIO.setFunction(L2, GPIO.OUT)
    GPIO.setFunction(R1, GPIO.OUT)
    GPIO.setFunction(R2, GPIO.OUT)
    GPIO.setFunction(C1, GPIO.OUT)
    GPIO.setFunction(C2, GPIO.OUT)
    
    #GPIO.pwmWrite(LED0, 0.5)        # set to 50% ratio
    #GPIO.pwmWriteAngle(SERVO, 0)    # set to 0 (neutral)
    #GPIO.digitalWrite(LED1, GPIO.HIGH)
    
    #gpio0 = webiopi.deviceInstance("gpio0")
    #gpio0.digitalWrite(0, 0)

# Looped by WebIOPi
def loop():
    # Toggle LED each 5 seconds
    #value = not GPIO.digitalRead(LED1)
    #GPIO.digitalWrite(LED1, value)
    webiopi.sleep(1)        

# Called by WebIOPi at server shutdown
def destroy():
    #webiopi.debug("Script with macros - Destroy")
    # Reset GPIO functions
    GPIO.setFunction(L1, GPIO.IN)
    GPIO.setFunction(L2, GPIO.IN)
    GPIO.setFunction(R1, GPIO.IN)
    GPIO.setFunction(R2, GPIO.IN)
    GPIO.setFunction(R1, GPIO.IN)
    GPIO.setFunction(R2, GPIO.IN)
    #gpio0 = webiopi.deviceInstance("gpio0")
    #gpio0.digitalWrite(0, 1)

# A macro which says hello

@webiopi.macro
def clickpic():
	subprocess.call("./webcam.sh")
	#subprocess.call("webcam.sh", shell=True)
