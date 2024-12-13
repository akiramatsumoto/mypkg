# ランダムな数字を出力するためのノード

import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Random(Node):
    def __init__(self):
        super().__init__("random")
        self.pub = self.create_publisher(Int16, "random_number", 10)
        self.i = 1
        self.n = []
        while 1:
            i += 1
            self.n[i] = random.randrange(10)
        self.create_timer(0.05, self.cb)


    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)


def main():
    rclpy.init()
    node = Random()
    rclpy.spin(node)
