import RPi.GPIO as GPIO
import pygame
import sys

pygame.init()

pygame.display.set_mode((100,100))

GPIO.setmode(GPIO.BCM)

in1 = 17
in2 = 27
in3 = 13
in4 = 19

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

my_pwm1 = GPIO.PWM(in2,1000)
my_pwm2 = GPIO.PWM(in4,1000)
my_pwm1.start(0)
my_pwm2.start(0)

#this function to control motor moving forward.
def motor1_forward(a):
 GPIO.output(in1,GPIO.HIGH)
 my_pwm1.ChangeDutyCycle(100-a)
def motor1_backward(a):
 GPIO.output(in1,GPIO.LOW)
 my_pwm1.ChangeDutyCycle(a)
def motor1_stopb():
 GPIO.output(in1,GPIO.LOW)
 my_pwm1.ChangeDutyCycle(0)
def motor1_stopf():
 GPIO.output(in1,GPIO.HIGH)
 my_pwm1.ChangeDutyCycle(100)

def motor2_forward(a):
 GPIO.output(in3,GPIO.HIGH)
 my_pwm2.ChangeDutyCycle(100-a)
def motor2_backward(a):
 GPIO.output(in3,GPIO.LOW)
 my_pwm2.ChangeDutyCycle(a)
def motor2_stopb():
 GPIO.output(in3,GPIO.LOW)
 my_pwm2.ChangeDutyCycle(0)
def motor2_stopf():
 GPIO.output(in3,GPIO.HIGH)
 my_pwm2.ChangeDutyCycle(100)

while(1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)            
            my_pwm1.stop(0)
            my_pwm2.stop(0)
            sys.exit()
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            print (u'"{}" key pressed'.format(key_name))
            if event.key == pygame.K_w:
                motor1_forward(80)
                motor2_forward(80)
            if event.key == pygame.K_s:
                motor1_backward(80)
                motor2_backward(80)
            if event.key == pygame.K_a:
                motor1_forward(80)
                motor2_backward(80)
            if event.key == pygame.K_d:
                motor1_backward(80)
                motor2_forward(80)
        if event.type == pygame.KEYUP:
            key_name = pygame.key.name(event.key)
            print (u'"{}" key released'.format(key_name))
            if event.key == pygame.K_w:
                motor1_stopf()
                motor2_stopf()
            if event.key == pygame.K_s:
                motor1_stopb()
                motor2_stopb()
            if event.key == pygame.K_a:
                motor1_stopf()
                motor2_stopb()
            if event.key == pygame.K_d:
                motor1_stopb()
                motor2_stopf()
            p = pygame.key.get_pressed()
            if p[pygame.K_w]:
                motor1_forward(80)
                motor2_forward(80)
            if p[pygame.K_s]:
                motor1_backward(80)
                motor2_backward(80)
            if p[pygame.K_a]:
                motor1_forward(80)
                motor2_backward(80)
            if p[pygame.K_d]:
                motor1_backward(80)
                motor2_forward(80)
