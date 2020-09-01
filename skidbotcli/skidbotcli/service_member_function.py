from tutorial_interfaces.srv import  DriveCommand

import rclpy
from rclpy.node import Node

import smbus
import time

ADDR = 0x40
bus = smbus.SMBus(1)       # open I2C port 1

def initPWM():
  bus.write_byte_data(ADDR,0x00,0x20)   # set auto register incremet for writing  multiple bytes to PWM chip
  bus.write_byte_data(ADDR,0xfe,135)    # set repetition to about 50 hz

def writePWM(port,value):
  blk = [0x00,0x00]             # set initial values to send to PWM chip
  blk[0] = value & 0xff         # put in LSB first
  blk[1] = value >> 8           # insert MSB of value
  addr = port * 4 + 8           # calculat address for register
  bus.write_i2c_block_data(ADDR,addr,blk)       # send to PWM chip

def reverse(speed):
        for i in range(0,speed,4):
                writePWM(0,i)
                writePWM(1,0)
                writePWM(2,i)
                writePWM(3,0)

def forward(speed):
        for i in range(0,speed,4):
                 writePWM(0,0)
                 writePWM(1,i)
                 writePWM(2,0)
                 writePWM(3,i)

def right(speed):
         for i in range(0,4095,4):
                 writePWM(0,i)
                 writePWM(1,0)
                 writePWM(2,0)
                 writePWM(3,i)

def left(speed):
         for i in range(0,4095,4):
                 writePWM(0,0)
                 writePWM(1,i)
                 writePWM(2,i)
                 writePWM(3,0)

def stop():
        writePWM(0,0)
        writePWM(1,0)
        writePWM(2,0)
        writePWM(3,0)


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(DriveCommand, 'drive_command', self.drive_command_callback)

    def drive_command_callback(self, request, response):
           if (request.a == "forward"):
               forward(request.b)
           elif (request.a == "reverse"):
                reverse(request.b)
           elif (request.a == "left"):
                left(request.b)
           elif (request.a == "right"):
                right(request.b)
           else:
                stop()

           self.get_logger().info('Incoming request\na: %s b:%d c%d' % (request.a, request.b, request.c))

           response.sum = 0
           return response


def main(args=None):
    rclpy.init(args=args)
    initPWM()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()
