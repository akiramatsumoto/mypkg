#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Akira Matsumoto <akiram8427@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import psutil

rclpy.init()
node = Node("battery_monitor")
pub = node.create_publisher(Float32, "batterylevel", 10)
battery = psutil.sensors_battery()

def cb():
    msg = Float32()
    msg.data = battery.percent
    pub.publish(msg)
    print(msg.data)

def main():
    node.create_timer(2.0, cb)
    rclpy.spin(node)

