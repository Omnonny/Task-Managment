from assemble import assemble_robot
from time import sleep 
from random import randint

def rotateRand(min, max, angle_speed):
  angle = randint(min, max)
  angle_time = angle / angle_speed
  robot.drive.torotate(angle = angle, time_to_take = angle_time)

distance = robot.ultrasonic.distance

if distance > 1:
  robot.drive.foward(0.75)
else if distance <= 0.25:
  robot.drive.stop()
  rotateRand(0, 180, 2)
  


  
  
  
