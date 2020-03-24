import pygame
import string
import pygame
<<<<<<< Updated upstream
=======
from gpiozero import LED
from gpiozero import Button
from signal import pause
import time
import _thread
import RPi.GPIO as GPIO

def pushButton1(channel,dic):
    led = LED(17)
    if not GPIO.input(17):
        print("TURN ON THE LIGHT")
        led.on()
        print("Button was pressed!")
        time.sleep(3)
    else:
        print("TURN OFF THE LIGHT")
        led.off()
        print("Button was pressed!")
        time.sleep(3)


>>>>>>> Stashed changes

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

<<<<<<< Updated upstream
# define the RGB value
# for white colour
white = (255, 255, 255)
=======
    def Now_running(self):
        # Set up
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(17, GPIO.OUT)
        GPIO.add_event_detect(2, GPIO.FALLING, callback=lambda x: pushButton1(17, self.dic), bouncetime=300)
        
        pygame.init()
>>>>>>> Stashed changes

# assigning values to X and Y variable
X = 1000
Y = 600

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Spicy Car')

# create a surface object, image is drawn on it.
image_car = pygame.image.load(r'/home/pi/Documents/Project/Images/car.jpg')
image_chairs = pygame.image.load(r'/home/pi/Documents/Project/Images/Chairs.jpg')
image_fire = pygame.image.load(r'/home/pi/Documents/Project/Images/fire.jpg')
image_lock = pygame.image.load(r'/home/pi/Documents/Project/Images/lock.jpg')
image_on = pygame.image.load(r'/home/pi/Documents/Project/Images/on.jpg')
image_off = pygame.image.load(r'/home/pi/Documents/Project/Images/off.jpg')

# infinite loop
while True:


    display_surface.fill(white)

    # Create the method for input SUB

    #dictionary = input()

    # Practice Input



    # Car dictionary
    dict = {"states": {"carLock" : True, "carOn": False, "defrost": {"back": True, "front": True}, "seatHeater": {"bDriver": False, "bPass": True, "fDriver": False, "fPass": True}}}

    # Checking States
    The_input = {"data": string, "attributes": { string: string}, "messageId": string, "publishTime": string
}


    # How each state is processed
    lock = dict['states']['carLock']
    power = dict["states"]["carOn"]
    Windsheild_Front = dict["states"]["defrost"]["front"]
    Windsheild_Back = dict["states"]["defrost"]["back"]
    FD = dict["states"]["seatHeater"]["fDriver"];
    FP = dict["states"]["seatHeater"]["fPass"];
    BD = dict["states"]["seatHeater"]["bDriver"];
    BP = dict["states"]["seatHeater"]["bPass"];

<<<<<<< Updated upstream
=======
            display_surface.blit(image_car, (200, 100))
            display_surface.blit(image_chairs, (30, 0))
            
            # Checking for the light
            
            #if GPIO.input(17):
            #    self.dic["states"]["defrost"]["front"] = True
# {"states": {"carLock" : True, "carOn": False, "defrost": {"back": True, "front": True}, "seatHeater": {"bDriver": False, "bPass": True, "fDriver": False, "fPass": True}}}
>>>>>>> Stashed changes

    display_surface.blit(image_car, (200, 100))
    display_surface.blit(image_chairs, (30, 0))

    if lock:
        display_surface.blit(image_lock, (440, 100))
    if power:
        display_surface.blit(image_on, (500, 505))
    else:
        display_surface.blit(image_off, (300, 500))
    if FD:
        display_surface.blit(image_fire, (0, 50))
    if FP:
        display_surface.blit(image_fire, (0, 150))
    if BD:
        display_surface.blit(image_fire, (240, 50))
    if BP:
        display_surface.blit(image_fire, (240, 150))
    if Windsheild_Back:
        display_surface.blit(image_fire, (300, 250))
    if Windsheild_Front:
        display_surface.blit(image_fire, (650, 250))


    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()