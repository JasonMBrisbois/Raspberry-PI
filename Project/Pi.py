import pygame
import string
import pygame
from gpiozero import LED
from gpiozero import Button
from signal import pause
import time
import _thread
import RPi.GPIO as GPIO

def pushButton1(channel):
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



class Spicy:
    def __init__(self):
        self.dic = {"states": {"carLock" : True, "carOn": False, "defrost": {"back": True, "front": True}, "seatHeater": {"bDriver": False, "bPass": True, "fDriver": False, "fPass": True}}}

    def Now_running(self):
        # Set up
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(17, GPIO.OUT)
        GPIO.add_event_detect(2, GPIO.FALLING, callback=pushButton1, bouncetime=300)
        
        pygame.init()

        white = (255, 255, 255)

        X = 1000
        Y = 600

        display_surface = pygame.display.set_mode((X, Y))

        pygame.display.set_caption('Spicy Car')

        image_car = pygame.image.load(r'/home/pi/Documents/Project/Images/car.jpg')
        image_chairs = pygame.image.load(r'/home/pi/Documents/Project/Images/Chairs.jpg')
        image_fire = pygame.image.load(r'/home/pi/Documents/Project/Images/fire.jpg')
        image_lock = pygame.image.load(r'/home/pi/Documents/Project/Images/lock.jpg')
        image_on = pygame.image.load(r'/home/pi/Documents/Project/Images/on.jpg')
        image_off = pygame.image.load(r'/home/pi/Documents/Project/Images/off.jpg')

        # infinite loop
        while True:

            GPIO.setup(17, GPIO.OUT)
            display_surface.fill(white)

            # Create the method for input SUB

            #dictionary = input()

            # Practice Input



            
            # Checking States
            The_input = {"data": string, "attributes": { string: string}, "messageId": string, "publishTime": string}


            # How each state is processed
            


            display_surface.blit(image_car, (200, 100))
            display_surface.blit(image_chairs, (30, 0))
            
            # Checking for the light
            
            if GPIO.input(17):
                self.dic["states"]["defrost"]["front"] = True
# {"states": {"carLock" : True, "carOn": False, "defrost": {"back": True, "front": True}, "seatHeater": {"bDriver": False, "bPass": True, "fDriver": False, "fPass": True}}}

            if self.dic["states"]["carLock"]:
                display_surface.blit(image_lock, (440, 100))
            if self.dic["states"]["carOn"]:
                display_surface.blit(image_on, (500, 505))
            else:
                display_surface.blit(image_off, (300, 500))
            if self.dic["states"]["seatHeater"]["fDriver"]:
                display_surface.blit(image_fire, (0, 50))
            if self.dic["states"]["seatHeater"]["fPass"]:
                display_surface.blit(image_fire, (0, 150))
            if self.dic["states"]["seatHeater"]["bDriver"]:
                display_surface.blit(image_fire, (240, 50))
            if self.dic["states"]["seatHeater"]["bPass"]:
                display_surface.blit(image_fire, (240, 150))
            if self.dic["states"]["defrost"]["back"]:
                display_surface.blit(image_fire, (300, 250))
            if self.dic["states"]["defrost"]["front"]:
                display_surface.blit(image_fire, (650, 250))

            white = (255, 255, 255)
            for event in pygame.event.get():


                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pygame.display.update()
                
if __name__ == "__main__":
    car = Spicy()
    car.Now_running()
